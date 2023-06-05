from django.contrib import admin
from .models import Item, Bid

class BidAdmin(admin.ModelAdmin):
    list_display = ('field_with_str','updated_at')

    def field_with_str(self, obj):
        return f'{obj.item.name} - {obj.bid_placed_by.username}'
    field_with_str.short_description = 'Field with Str'
admin.site.register(Item)
admin.site.register(Bid, BidAdmin)

# Register your models here.
