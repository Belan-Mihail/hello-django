"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo.views import get_todo_list, add_item

urlpatterns = [
    path('admin/', admin.site.urls),
#     Once that's done all that we need to do is define the url that's actually going to
# trigger the say hello function and return the http response to the browser.
# To do that we use the built-in path function which typically takes three arguments.
# It takes the url that the user is going to type in. In our case we're going to say hello.
# It takes the view function that it's going to return.
# Which is our say_hello function.
# And it takes a name parameter which we'll get to a bit later but for right now we'll just call it hello
    # path('hello/', say_hello, name='hello')
    
    path('', get_todo_list, name='get_todo_list'),

#     And instead, I'm gonna replace it with just an empty string.
# This means that we don't need to specify any particular URL in order to hit that Python function
# so this is gonna act as our home page.


    path('add', add_item, name='add')
#     Lastly we need a new URL to access this template because right now
# if we click the link to add an item we'll get a page not found error.
# So I'm gonna go to urls.py and copy the URL for the home page.
# Change this URL to add
]
