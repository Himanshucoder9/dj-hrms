from django.contrib import admin
from .models import *
from django.contrib import messages

# Register your models here.
admin.site.register(ItemCategory)
admin.site.register(ItemUnit)
admin.site.register(Shop)
admin.site.register(Item)
admin.site.register(ItemOrder)
admin.site.register(ItemStock)
admin.site.register(ItemIssued)


# admin.site.register(ItemReturned)


class ItemReturnedAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'returned_to', 'returned_by', 'return_date')

    def save_model(self, request, obj, form, change):
        if not obj.item.is_returnable:
            self.message_user(request, f"The item '{obj.item.name}' is not returnable.", messages.ERROR)
        else:
            super().save_model(request, obj, form, change)


admin.site.register(ItemReturned, ItemReturnedAdmin)
