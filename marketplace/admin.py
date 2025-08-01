


from django.contrib import admin
from .models import Item, Transaction, ItemImage

class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 1

class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInline]

admin.site.register(Item, ItemAdmin)
admin.site.register(Transaction)
admin.site.register(ItemImage)
