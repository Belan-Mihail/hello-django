from django.contrib import admin
from .models import Item
# Even though the items table has been created and we could start creating
# items programmatically now.
# We won't be able to see our items in the admin until we expose them.
# To do that we need to register our model in the todo apps admin.py file.


# Register your models here.
admin.site.register(Item)

# And then we're going to use the admin.site.register function.
# To actually register our item model.