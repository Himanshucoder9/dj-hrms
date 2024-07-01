from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from Stock.models import ItemOrder,ItemStock,ItemIssued

@receiver(post_save, sender=ItemOrder)
def update_stock_on_order(sender, instance, created, **kwargs):
    if created and instance.status == 'received':
        item_stock, created = ItemStock.objects.get_or_create(item=instance.item, company=instance.company)
        item_stock.stock_quantity += instance.quantity
        item_stock.save()


@receiver(post_save, sender=ItemIssued)
def update_stock_on_issue(sender, instance, created, **kwargs):
    if created:
        # Update out_quantity in ItemStock
        item_stock, created = ItemStock.objects.get_or_create(item=instance.item, company=instance.company)
        item_stock.stock_quantity -= instance.out_quantity
        item_stock.save()

@receiver(post_save, sender=ItemIssued)
def update_stock_on_return(sender, instance, created, **kwargs):
    if not created and instance.return_date is not None:
        # Update in_quantity in ItemStock
        item_stock, created = ItemStock.objects.get_or_create(item=instance.item, company=instance.company)
        item_stock.stock_quantity += instance.in_quantity
        item_stock.save()

@receiver(post_delete, sender=ItemIssued)
def revert_stock_on_delete(sender, instance, **kwargs):
    # If an ItemIssued is deleted, revert stock changes
    item_stock, created = ItemStock.objects.get_or_create(item=instance.item, company=instance.company)
    item_stock.stock_quantity += instance.out_quantity  # Revert out_quantity
    if instance.return_date is not None:
        item_stock.stock_quantity -= instance.in_quantity  # Revert in_quantity if returned
    item_stock.save()

