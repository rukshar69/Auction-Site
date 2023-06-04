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
    

# Bids placed by users
class Bid(models.Model):
    bid_price = models.FloatField()
    item = models.ForeignKey(Item,related_name='bids',on_delete=models.CASCADE)
    bid_placed_by = models.ForeignKey(CustomUser, related_name='bids', on_delete=models.CASCADE)
    bid_placed_at = models.DateTimeField(auto_now_add=True)
    is_winner = models.BooleanField(default=False) #did the user win the bid
    def __str__(self):
        return self.item.name + '_' + self.bid_placed_by.username

#stores info. of bidwinner
# class BidWinner(models.Model):
#     winning_bid_price = models.FloatField()
#     auctioned_item = models.ForeignKey(Item,related_name='bidwinners',on_delete=models.CASCADE)
#     winner_user = models.ForeignKey(CustomUser, related_name='bidwinners', on_delete=models.CASCADE)
#     def __str__(self):
#         return self.auctioned_item