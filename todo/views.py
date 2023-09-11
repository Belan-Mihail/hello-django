from django.shortcuts import render

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
    return render(request, 'todo/todo_list.html')
    # return HttpResponse('<h1>Hello!</h1><p>This is text</p>')
# This is basically just a shortcut to writing a really long HTTP response filled with lots of HTML
# Instead of writing all that HTML as a string in Python
# We can write it in an actual HTML file and pass it to the render function to let Django do the work.
