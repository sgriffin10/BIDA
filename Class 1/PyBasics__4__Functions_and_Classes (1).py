#
# # Functions
#
# # A function is a block of code which only runs when it is called.
# # You can pass data, known as parameters, into a function.
# # A function can return data as a result.
#
# def my_function():
#   print("Hello from a function")
#
# my_function()
#
# #The following example has a function with one parameter (fname)
# def my_function1(fname):
#   print(fname + " Refsnes")
#
# my_function1("Emil")
# my_function1("Tobias")
# my_function1("Linus")
#
# #If we call the function without parameter, it uses the default value
# def my_function(country = "Norway"):
#   print("I am from " + country)
#
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")
#
# #To let a function return a value, use the return statement
# def my_function(x):
#   return 5 * x
#
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))


# # Classes
#
# class Dog():
# #Represent a dog.
#  def __init__(self, name):
#  #Initialize dog object.
#     self.name = name
#  def sit(self):
#  #Simulate sitting.
#     print(self.name + " is sitting.")
# my_dog = Dog('Peso')
# print(my_dog.name + " is a great dog!")
# my_dog.sit()
#
# # Inheritance
# class SARDog(Dog):
# #Represent a search dog.
#  def __init__(self, name):
# #Initialize the sardog.
#     super().__init__(name)
#  def search(self):
# #Simulate searching.
#     print(self.name + " is searching.")
# my_dog = SARDog('Willie')
# print(my_dog.name + " is a search dog.")
# my_dog.sit()
# my_dog.search()
