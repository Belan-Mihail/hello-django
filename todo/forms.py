# This works perfectly fine but creating
# forms manually leaves our application open to errors if we don't validate them properly.
# For example if we create a form and forget to mark one of the fields as required.
# But that field is required on the database model. Django would try to create an item
# in our database with the missing field which could result in an error on the front-end
# To alleviate this issue. In Django it's possible to create forms directly from the model itself.
# And allow Django to handle all the form validation.

from django import forms
from .models import Item

#  we need our item model.
# Just like when we created the item model itself.
# Our form will be a class that inherits a built-in Django class to give it some basic functionality.
# To set it up we need to create a new class.

class ItemForm(forms.ModelForm):
#     To tell the form which model it's going to be associated with.
# We need to provide an inner class called meta.
# This inner class just gives our form some information about itself.
# Like which fields it should render how it should display error messages and so on. 
# In this class the only thing I'm going to define our model. Which is going to be our item model.
# And fields which will tell it we want to display the name in done fields from the model.
# The idea of creating this form in Django is that rather than writing an
# entire form ourselves in HTML.
# We can simply render it out as a template variable.
    class Meta:
        model = Item
        fields = ['name', 'done']

