from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from item.models import Item

def close_bids():
    #Close bids for items whose end date is before now
    items_need_to_close_bid= Item.objects.filter(is_bid_close=False,auction_end_datetime__lte=timezone.now())
    print('Items whose bids are now closing:')
    for item in items_need_to_close_bid:
        print(item.name)
        max_bid = item.bids.filter(bid_price__gt=item.minimum_bid_price, updated_at__lte=item.auction_end_datetime).order_by('-bid_price', 'updated_at').first() #get the bid with the hightest price with the earliest time
        if max_bid is not None:
            print('Max bid: ', max_bid.bid_price, ' by: ', max_bid.bid_placed_by.username)
            max_bid.is_winner = True
            max_bid.save()
        # Modify the field value
        item.is_bid_close = True #closing the bid
        # Save the object to persist the changes
        item.save()

@login_required
def index(request):
    close_bids()

    # GET ITEM WHOSE BIDS ARE OPEN
    items_bid_open = Item.objects.filter(is_bid_close=False, created_by=request.user).order_by('-auction_end_datetime')
    # GET ITEM WHOSE BIDS ARE CLOSED
    items_bid_close = Item.objects.filter(is_bid_close=True, created_by=request.user) 
    return render(request, 'dashboard/index.html', {
        'items_bid_open': items_bid_open,
        'items_bid_close': items_bid_close,
    })

@login_required
def admin_dashboard(request):

    close_bids()
    
    #TOTAL AUCTIONS CURRENTLY RUNNING   
    total_auctions = Item.objects.filter(is_bid_close=False).count()
    print( 'total_auctions: ',total_auctions)

    #TOTAL AUCTION VALUE
    total_auction_value = 0
    currently_running_auctions =  Item.objects.filter(is_bid_close=False)
    for item in currently_running_auctions:
        max_bid = item.bids.filter(bid_price__gt=item.minimum_bid_price).order_by('-bid_price', 'updated_at').first() #get the bid with the hightest price with the earliest time
        if max_bid is not None:
            total_auction_value += max_bid.bid_price
    print('total auction val: ', total_auction_value)
    return render(request, 'dashboard/admin_dashboard.html', {
        'total_auctions': total_auctions,
        'total_auction_value':total_auction_value,
    })