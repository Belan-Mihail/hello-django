from django.shortcuts import render
from .models import Item
# We need access to the item model in this file so the first thing I'm going to do
# is right at the top. From .models import item.

# Create your views here.
# So that instead of returning this long string of HTML
# It returns our template instead.
# We can accomplish that using the render function which was imported into
# this views.py file when we created our app originally.
# The render function takes an HTTP request and a template name as it's two arguments
# And it actually returns an HTTP response like this. which renders that template.
# So instead of returning this HTTP response let's return render.
# Give it the request. And then in quotes we will give it
# todo/todo_list.html
def get_todo_list(request):
#     In the get_todo list function. we can then get what's called a query set of all the
# items in the database.
# By creating a variable. Let's call it item. Equal to item.objects.all
    items = Item.objects.all()
#     Next I'm going to create a variable called context. Which is just going to be a
# dictionary with all of our items in it.
# So it needs a key of items. And that value is going to be our items variable that we just created.
    context = {
        'items': items
    }
#     And finally I'm going to add that context as a third argument to the render function.
# And this will ensure that we have access to it in our todo list .html template.
    return render(request, 'todo/todo_list.html', context)
    # return HttpResponse('<h1>Hello!</h1><p>This is text</p>')
# This is basically just a shortcut to writing a really long HTTP response filled with lots of HTML
# Instead of writing all that HTML as a string in Python
# We can write it in an actual HTML file and pass it to the render function to let Django do the work.


# So we need to find a way to get those items from the database into a template.
# Remember that in the Model View template design pattern
# The views represent the programming logic that allows users to interact with
# the database through the templates that they see.