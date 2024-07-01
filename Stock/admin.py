from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ItemCategory)
admin.site.register(ItemUnit)
admin.site.register(Shop)
admin.site.register(Item)
admin.site.register(ItemOrder)
admin.site.register(ItemStock)
admin.site.register(ItemIssued)