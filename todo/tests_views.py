from django.test import TestCase

# Create your tests here.
class TestDjango(TestCase):
#     Self here refers to our test Django class which because it inherits the test case class
# wi'll have a bunch of pre-built methods and functionality that we can use.
    def test_this_thing_works(self):
#         I'll use the built-in assert equal method to determine whether one equals zero.
# Obviously we know one is not equal to zero so this test should fail.
        self.assertEqual(1, 1)

    # def test_this_thing_works2(self):
    #     self.assertEqual(1, 1)
    
    # def test_this_thing_works3(self):
    #     self.assertEqual(1, 1)
    
    # def test_this_thing_works4(self):
    #     self.assertEqual(1, 1)
