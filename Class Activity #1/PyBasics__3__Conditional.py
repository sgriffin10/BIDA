#Conditional Statements
#IF..ELSE
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#shorthand
print("b is greater than a") if b > a else print("a and b are equal") if a == b else print("a is greater than b")

# #WHILE Loop
# i = 1
# while i < 6:
#   print(i)
#   # i += 1


# #With the break statement we can stop the loop even if the while condition is true
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# #With the continue statement we can stop the current iteration, and continue with the next
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# # FOR Loops
# #A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

# for x in "banana":
#     print(x)


# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)
for x in "banana":
    print(x)


for x in range(6):
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
