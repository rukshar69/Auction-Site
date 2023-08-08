# Auction-Site

## Features

Live Demo in PythonAnywhere: [http://rukshar69.pythonanywhere.com/](http://rukshar69.pythonanywhere.com/)

- Login, SignUp, and Logout mechanism. SignUp and Login is done using email instead of the default username.
- The [homepage](http://rukshar69.pythonanywhere.com/) shows the currently open bid items and the closed bid items
- The [Create Auction item](http://rukshar69.pythonanywhere.com/items/new/) takes the user to the item creation page. Here, the user sets the item's name, description, min. bid price, auction end date, and item image.
- The [My Posted Items](http://rukshar69.pythonanywhere.com/dashboard/) page shows the currently logged in user's active and closed bid items. 
- Clicking on an item card from the dashboard allows other users to view the details of that item and place bids or update previously posted bids. This page also lists the previously placed bids. When the auction date is over, users will no longer be able to place bids but they can still view the item detail and **who won the bid**.
- If logged in as an Admin(email: admin@gmail.com and password: admin123##), the [Admin Dashboard](http://rukshar69.pythonanywhere.com/dashboard/admin_dashboard/) page shows the total number of active bids and the total highest bid price of all the active bids.

# Challenges

## Step 1
Django's default User model uses **username** for login. In order to change the login input to **email** I had to create a [custom user model](https://github.com/rukshar69/Auction-Site/blob/main/RuksharsAuction/core/models.py) from Django's *AbstractUser* class. Additionally, I had to construct my own [login view](https://github.com/rukshar69/Auction-Site/blob/main/RuksharsAuction/core/views.py#L35) instead of using Django's default **auth_views.LoginView**

## Step 2
To add **auction end datetime** using a calendar interface while adding a new item, I had to install a package named [django-tempus-dominus](https://github.com/FlipperPA/django-tempus-dominus). I had to construct a [custom Django form](https://github.com/rukshar69/Auction-Site/blob/main/RuksharsAuction/item/forms.py#L24) to incorporate this package to enable date time input using a calendar. Additionally, font-awesome, Bootstrap 4 and jQuery scripts were included in the HTML files to enable this datetime picker.

## Step 3
For admin login, you can login using your superuser credential at the *login/* endpoint. As admin, you'll see an additional button **Admin Dashboard**. By clicking on this, you can view total currently running auctions and total action value at the moment. Admin credential: email: **admin@gmail.com** and password: **admin123##**

## Step 4
Learning [pythonanywhere](https://www.pythonanywhere.com/) to deploy the Django app there.

# Packages
- Python 3.10
- [django-tempus-dominus](https://github.com/FlipperPA/django-tempus-dominus) for adding calendar-based date time picker for front end.
- TailwindCSS is used for prettier front end rendering

# Video Demo
Drive Link: https://drive.google.com/file/d/1QKJiDHEU1cDzsSGYZL6F26DvYObSd1TQ/view?usp=sharing 