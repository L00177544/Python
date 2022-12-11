"""
Simple Class
"""
# Create a class
class TomClass():
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting):
        print("Running constructor for TomClass")
        # Create attributes and set initial values
        self.message = my_greeting
    def my_method(self):
        print(self.message)
my_class1 = TomClass("Morning Tomasz!")
my_class1.my_method()
print(type(my_class1))

class TomClass2():
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting):
        print("Running constructor for TomClass2")
        # Create attributes and set initial values
        self.message = my_greeting
    def my_method(self):
        print(self.message)
my_class2 = TomClass2("Hello Tomasz!")
my_class2.my_method()
print(type(my_class2))