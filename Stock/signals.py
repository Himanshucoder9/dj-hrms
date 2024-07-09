from Stock.models import ItemOrder, ItemStock, ItemIssued, ItemReturned
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError


@receiver(post_save, sender=ItemOrder)
def update_stock_on_order(sender, instance, created, **kwargs):
    if created and instance.status == 'received':
        item_stock, created = ItemStock.objects.get_or_create(item=instance.item, company=instance.company)
        item_stock.stock_quantity += instance.quantity
        item_stock.save()


@receiver(post_save, sender=ItemIssued)
def update_stock_on_issue(sender, instance, created, **kwargs):
    if created:
        item_stock = ItemStock.objects.get(item=instance.item)
        item_stock.stock_quantity -= instance.quantity
        item_stock.save()


@receiver(post_save, sender=ItemReturned)
def update_stock_on_return(sender, instance, created, **kwargs):
    if created:
        item_stock = ItemStock.objects.get(item=instance.item)
        item_stock.stock_quantity += instance.quantity
        item_stock.save()

        # Decrease the quantity of the corresponding issued item
        issued_item = instance.issued_item
        issued_item.quantity -= instance.quantity
        issued_item.save()


@receiver(pre_save, sender=ItemReturned)
def check_item_returnable(sender, instance, **kwargs):
    if not instance.item.is_returnable:
        raise ValidationError(f"The item '{instance.item.name}' is not returnable.")












# @receiver(post_save, sender=ItemIssued)
# def notify_low_stock(sender, instance, created, **kwargs):
#     if created:
#         item_stock = ItemStock.objects.get(item=instance.item)
#         if item_stock.stock_quantity <= item_stock.reorder_level:
#             # Replace with your notification logic, e.g., sending an email or creating a notification record
#             send_mail(
#                 'Stock Alert',
#                 f'Stock of {instance.item.name} is low. Please refill.',
#                 'from@example.com',
#                 [instance.item.company.admin_email],  # Adjust recipient based on your setup
#                 fail_silently=False,
#             )
