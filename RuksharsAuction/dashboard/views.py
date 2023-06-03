from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from item.models import Item

@login_required
def index(request):
    #Close bids for items whose end date is before now
    items_need_to_close_bid= Item.objects.filter(is_bid_close=False,created_by=request.user, auction_end_datetime__lte=timezone.now())
    print('Items whose bids are now closing:')
    for item in items_need_to_close_bid:
        print(item.name)
        # Modify the field value
        item.is_bid_close = True #closing the bid
        # Save the object to persist the changes
        item.save()

    # GET ITEM WHOSE BIDS ARE OPEN
    items_bid_open = Item.objects.filter(is_bid_close=False, created_by=request.user).order_by('-auction_end_datetime')
    # GET ITEM WHOSE BIDS ARE CLOSED
    items_bid_close = Item.objects.filter(is_bid_close=True, created_by=request.user) 
    return render(request, 'dashboard/index.html', {
        'items_bid_open': items_bid_open,
        'items_bid_close': items_bid_close,
    })