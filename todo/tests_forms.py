from django.test import TestCase
from .forms import ItemForm

# Create your tests here.
class TestItemForm(TestCase):

    def test_item_name_is_required(self):
# We'll begin with the simple test to make sure that the name field is required in order to create an item.
# In general, you'll want to name your tests so that when they fail you can easily see what the issue is.
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
#         So I'll call this one test item name is required.
# I'll begin by instantiating a form and we'll deliberately instantiate it without a name
# to simulate a user who submitted the form without filling it out.
# This form should not be valid.
# So I'll use assert false to ensure that that's the case.
        self.assertIn('name', form.errors.keys())
#         When the form is invalid it should also send back a dictionary of fields on which
# there were errors and the Associated error messages
# Knowing this we can be even more specific by using assert in to assert
# whether or not there's a name key in the dictionary of form errors.
        self.assertEqual(form.errors['name'][0], 'This field is required.')
#         Finally to really drive the point home.
# I'll use assert equal to check whether the error message on the name field is this field is required.
# Remember to include the period at the end here as the string will need to match exactly.
# Also just a note we're using the zero index here because the form will return a list of errors on each field.
# And this verifies that the first item in that list is our string telling us the field is required.


# let's write another one to ensure the done field is not required.
# It shouldn't be since it has a default value of false on the item model.
    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test Todo Items'})
        self.assertTrue(form.is_valid())
#         In this case we'll create the form sending only a name.
# And then just test that the form is valid as it should be even without selecting a done status.


# Finally let's assume that somewhere down the line another developer comes
# along and changes the item model.
# Adding a field to it that contains some sort of information we don't want to display on the form.
# If you remember we actually defined the fields to display explicitly in the inner metaclass on the item form.
# And the reason for that is otherwise the form will display all fields on the model
# including those we might not want the user to see.
# That said we should write a test to ensure that the only fields that are displayed in
# the form are the name and done fields.

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])


#         For this test we can simply instantiate an empty form.
# And then use assert equal to check whether the form.meta.fields attribute
# is equal to a list with name and done in it.
# This will ensure that the fields are defined explicitly.
# And if someone changes the item model down the road our form won't
# accidentally display information we don't want it to.
# This will also protect against the fields being reordered. Since the list must match exactly.



# So this is a good place to explain. You can actually be more specific about what you're testing.
# We could for example run only the form tests by using python3 manage.py tests todo.test_forms
# Run a specific class of tests by adding that on  (python3 manage.py tests todo.test_forms.TestItemForm).
# or even run a specific individual test by adding on the name of the test itself. (python3 manage.py test todo.test_forms.TestItemForm.test_fields_are_explicit_in_form_metaclass)