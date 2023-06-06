# Auction-Site

# Challenges

## Step 1
Django's default User model uses **username** for login. In order to change the login input to **email** I had to create a [custom user model](https://github.com/rukshar69/Auction-Site/blob/main/RuksharsAuction/core/models.py) from Django's *AbstractUser* class. Additionally, I had to construct my own [login view](https://github.com/rukshar69/Auction-Site/blob/main/RuksharsAuction/core/views.py#L35) instead of using Django's default **auth_views.LoginView**

## Step 2
To add **auction end datetime** using a calendar interface while adding a new item, I had to install a package named [django-tempus-dominus](https://github.com/FlipperPA/django-tempus-dominus). I had to construct a [custom Django form](https://github.com/rukshar69/Auction-Site/blob/main/RuksharsAuction/item/forms.py#L24) to incorporate this package to enable date time input using a calendar. Additionally, font-awesome, Bootstrap 4 and jQuery scripts were included in the HTML files to enable this datetime picker.

## Step 5
For admin login, you can login using your superuser credential at the *login/* endpoint. As admin, you'll see an additional button **Admin Dashboard**. By clicking on this, you can view total currently running auctions and total action value at the moment.

## Step 7
Learning [pythonanywhere](https://www.pythonanywhere.com/) to deploy the Django app there.

# Packages
- [django-tempus-dominus](https://github.com/FlipperPA/django-tempus-dominus) for adding calendar-based date time picker for front end.
- TailwindCSS is used for prettier front end rendering