from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm , BidPlacementForm
from .models import Item, Bid

# Create your views here.
@login_required
def new_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('dashboard:index')
    else:
        form = NewItemForm()
    #form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item_bids = item.bids.all() #get all bids for this item
    max_bid = item.bids.filter(is_winner = True).first() #get the bid with the hightest price with the earliest time
    print('People who placed bids on item: ', item.name)
    for b in item_bids:
        print(':',b.bid_placed_by.username)
    if max_bid is not None:
        print('Max bid: ', max_bid.bid_price, ' by: ', max_bid.bid_placed_by.username)
    

    #get bid for this item by the current user
    bid = Bid.objects.filter(item = item, bid_placed_by = request.user).first()

    bid_json = {}#storing info of bid to display on frontend
    if request.user.username != item.created_by.username:
        if bid is None : 
            print('No bids by User: ', request.user.username, ' for this item: ', item.name)
            bid_json = {'bid_available':False, 'bid_price':''} #if bid_available is False front end shows 'user made no bid yet!'
        else:
            print('user: ',request.user.username, ' bid: ', bid.bid_price)
            bid_json = {'bid_available':True, 'bid_price':bid.bid_price}#if bid_available is true front end shows current bid price for this item
        

    return render(request, 'item/detail.html', {
        'item': item,
        'bid':bid_json,
        'bids':item_bids,
        'max_bid':max_bid
    })

@login_required
def submit_bid(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item_bids = item.bids.all() #get all bids for this item
    #get bid for this item by the current user
    bid = Bid.objects.filter(item = item, bid_placed_by = request.user).first()

    bid_json = {}#storing info of bid to display on frontend
    if request.user.username != item.created_by.username:
        if bid is None : 
            print('No bids by User: ', request.user.username, ' for this item: ', item.name)
            bid_json = {'bid_available':False, 'bid_price':''} #if bid_available is False front end shows 'user made no bid yet!'
        else:
            print('user: ',request.user.username, ' bid: ', bid.bid_price)
            bid_json = {'bid_available':True, 'bid_price':bid.bid_price}#if bid_available is true front end shows current bid price for this item
        

    if request.method == 'POST':
        if bid is None:
            form = BidPlacementForm(request.POST)
        else:
            form = BidPlacementForm(request.POST, instance=bid)

        if form.is_valid():
            
            if bid is None: #if no bid placed before
                bid = form.save(commit=False)
                bid.item = item 
                bid.bid_placed_by = request.user
                bid.save()
            else:
                form.save()

            return redirect('item:detail', pk=item.id)
            #return redirect('core:index')
    else:
        form = BidPlacementForm()

    return render(request, 'item/place_bid.html', {
        'item': item,
        'bid':bid_json,
        'bid_placement_form':form,
        'bids':item_bids
    })