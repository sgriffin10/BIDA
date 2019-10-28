#Variables
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

#To combine both text and a variable, Python uses the + character:
x = "awesome"
print("Python is " + x)

#If you try to combine a string and a number, Python will give you an error:
# Uncomment the 3 lines below to test this out.
# Select the lines you want to uncomment and click Control-/ (i.e. control + forward slash)
# x = 5
# y = "John"
# print(x + y)

#To verify the type of any object in Python, use the type() function:
x = 1    # int
y = 2.8  # float
z = "Hello"   # complex
print(type(x))
print(type(y))
print(type(z))

#Casting: Specify a Variable Type
y = int(2.8) # y will be 2
print(y)