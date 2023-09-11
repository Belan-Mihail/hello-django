from django.db import models

# There's a key thing you need to understand here though. And that's that by itself this class won't do anything
# We need to use something called class inheritance to give it some functionality.
# You'll see at the top of this file there is already an item called models imported from django.db
# What this means is that we're literally importing the model's folder from the
# Django / DB directory in our project site-packages.
# And by doing so we gain access to everything in that folder.
# Just like when we imported our view function in urls.py

# You could even go into base.py And find the literal class definition for model.
# So all this functionality that's defined in the model's folder and all its files
# is accessible to us just by importing models from django.db
# And that's what will give us the ability to start our own model with all of that base functionality.
# To do that I'm going to inherit the base model class by putting models.model
# here in the parentheses so that our item class can do everything the built-in Django model class can do.

# For now just remember that if you need functionality from one class to be available in another.
# All you need to do is inherit the one you need.

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
#     All that's left to do is define the attributes that our individual items will have.
# We can skip the Id field that we had in our spreadsheet since Django will create that for us automatically.
# But we do need to define a name field and a done status field.

# You might remember that Django uses migrations to handle
# database operations. So what we need to do is use the command python3 manage.py
# by make migrations in order to make a migration file. 

# python3 manage.py makemigrations

# We can also use the python3 manage.py show migrations
# command to see that we do in fact have an unapplied migration on our to-do app now.
# And to apply it all we need to do is run python3 manage.py migrate


    # def __string__(self):
#         And all it's going to do is just return self.name.
# So this is going to return the item class's name attribute which in our case
# is going to be the name that we put into the form.
        # return self.name

# By default all models that inherit this base model class will use its built-in string
# method to display their class name followed by the word object.
# Just so that there's sort of a generic way to display them.
# And you can actually see this method defined in the base model class in django.db.models.base.
# If you want to take a look. You can see the string method right here.
# It returns object. And then the primary key. So that's what we see in the admin panel.
# To change that we need to actually override that string method with our own.
# And we can do that just by redefining it here in our own class.