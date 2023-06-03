from django.db import models
from core.models import CustomUser

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    minimum_bid_price = models.FloatField()
    image = models.ImageField(upload_to='item_images',blank=True, null=True)
    is_bid_close = models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    auction_end_datetime = models.DateTimeField()
    
    def __str__(self):
        return self.name