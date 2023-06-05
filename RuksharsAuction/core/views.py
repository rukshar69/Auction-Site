from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm,  CustomAuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from item.models import  Item
from django.utils import timezone
# Create your views here.
@login_required
def index(request):
    #Close bids for items whose end date is before now
    items_need_to_close_bid= Item.objects.filter(is_bid_close=False,auction_end_datetime__lte=timezone.now())
    print('Items whose bids are now closing:')
    for item in items_need_to_close_bid:
        print(item.name)
        max_bid = item.bids.filter(bid_price__gt=item.minimum_bid_price).order_by('-bid_price', 'updated_at').first() #get the bid with the hightest price with the earliest time
        if max_bid is not None:
            print('Max bid: ', max_bid.bid_price, ' by: ', max_bid.bid_placed_by.username)
            max_bid.is_winner = True
            max_bid.save()
    
        # Modify the field value
        item.is_bid_close = True #closing the bid
        # Save the object to persist the changes
        item.save()

    #choose items to show on the gallery

    # GET ITEM WHOSE BIDS ARE OPEN
    items_bid_open = Item.objects.filter(is_bid_close=False,auction_end_datetime__gt=timezone.now()).order_by('-auction_end_datetime')
    # GET ITEM WHOSE BIDS ARE CLOSED
    items_bid_close = Item.objects.filter(is_bid_close=True) 
    return render(request, 'core/index.html', {
        'items_bid_open': items_bid_open,
        'items_bid_close': items_bid_close,
    })


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']  # Get the email from the form data
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)  # Authenticate using email and password
            if user is not None:
                login(request, user)
                return redirect('core:index')  # Replace 'home' with your desired redirect URL
    else:
        form = CustomAuthenticationForm()
    return render(request, 'core/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email  # Set the username as the email
            user.save()
            #login(request, user)
            return redirect('core:login')  # Replace 'home' with your desired redirect URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/signup.html', {'form': form})



def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('core:login')