from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
# We need access to the item model in this file so the first thing I'm going to do
# is right at the top. From .models import item.
from .forms import ItemForm

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

# def add_item(request):
#     return render(request, 'todo/add_item.html')
# first change

# def add_item(request):
#     I'm gonna go back to views.py. And since we set the form action to our add URL.
# we need to add an if statement in the add item view to check what type of requests
# this is.
# However if the request to this URL is a post request that would mean it came
# from someone clicking the submit button on our form. And we want to actually
# create a to-do item and then redirect back to the home page to show the user
# their updated to-do lists.
    # if request.method == "POST":
#         And remember we can get these values using the name attributes from our form.
# So to get the items name we just need to look up request.post.get.
# And the name of that attribute which in our case was item_name
        # name = request.POST.get('item_name')
#         For the checkbox it's a little bit different. Since it's just a boolean value but in
# order to check if the item is done. All we have to do is check whether the post
# data actually has a done property in it. By checking whether done in request.post
        # done = 'done' in request.POST
#         At this point we should have everything we need to actually create a new item.
# We've already got our item model imported from .models up here at the top.
# And to create an item is actually extremely simple.
# All we need to do is call item.objects.create and give it these two variables.
# So name equals name done equals done. 
        # Item.objects.create(name=name, done=done)
#         And that's it finally we need to return a redirect
# # back to the get_todo list URL name.
        # return redirect('get_todo_list')
# With the form imported we can now create an instance of it in the add_item view.
# Create a context which contains the empty form.
# And then return the context to the template.
# This means that in the add item template we can now go delete all the fields we created ourselves.
# And instead render the form just like we would any other template variable.# 
    # form = ItemForm()
    # context = {
    #     'form': form
    # }


    # return render(request, 'todo/add_item.html', context)


# Here in the request.post handler instead of trying to create the item manually.
# Let's let our new form from forms.py do it.
# To do that we can use a similar syntax to what we use to create the empty form.
# But instead here will populate the form in Django with the request.post data.
# Then we can simply call the is_valid method on the form.
# And Django will automatically compare the data submitted in the post request
# to the data required on the model.
# And make sure everything matches up.
# To save our item then all we need to do is call form.save and then redirect to the
# get_todo list view like we were before.
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)

# First along with taking in the request. This view will also take in an item ID parameter
# And that's the item ID we just attached to the Edit link.
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    # Then just like above we'll create an instance of our item form and return it to the template in the context.
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
#     I'm actually just going to copy the entire handler from the add item view and paste it in here.
# Making only one small change and that's to give our form the specific item instance we want to update.
# Everything else can remain exactly the same.
# And with that saved. We can now reload our site and see that updating items is working as expected.
    
    form = ItemForm(request.POST, instance=item)
#     To pre-populate the form with the items current details.
# We can pass an instance argument to the form.
# Telling it that it should be prefilled with the information for the item we just got from the database.
    context = {
        'form': form
    }
#     Back in the edit_item view. Let's first get a copy of the item from the database.
# We can do this using a built in django shortcut called get_object_or_404
# Which we'll use to say we want to get an instance of the item model.
# With an ID equal to the item ID that was passed into the view via the URL.
# This method will either return the item if it exists. Or a 404 page not found if not.


    return render(request, 'todo/edit_item.html', context)


# This one won't even have a template because it's just going to toggle the item status.
# And then redirect back to the to-do list.
def toggle_item(request, item_id):

#     We can then use the same logic to get the item in question.
# Change it's done status to the opposite by using not.
# Which will just flip it to the opposite of whatever it currently is.
# And then save the item.
# So this will make it so that when a user clicks toggle. Our view will get the item.
# And if it's done status is currently true it will flip it to false and vice versa.
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
