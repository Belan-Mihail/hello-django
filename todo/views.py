from django.shortcuts import render, redirect
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
        form  = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


