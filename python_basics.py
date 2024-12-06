# INTRODUCTION

print("Hello World 69")
print(type("Hello World 69"))
print(17)
print(type(17))
print("17")
print(type("17"))
print("23"+"4")
print(type("23"+"4"))
print(23+4)
print(type(23+4))

print("hello" + " mayank") ## We can do this in python like adding 2 strings
# print("hello" - " mayank") ## But we cannot do this

# MATH OPERATIONS

print(2-3)
print(type(3))
print(type(3.2))
print(type(3 + 2))
print(type(3.2 + 4.7))
print(4 - 3)
print(3.2 - 1.0)
print(4*3)
print(2.1*3.2)
print(4/3)
print(1/1)
print(3.2/1.6)
print(3//2)
print(5//2)
print(5%2)
print(7%3)
print(5*5*5)
print(5**3)

# VARIABLES

y = 5
print(y)
y = 4
print(y)
y= "tree"
print(y)
print("tree")

# BOOLEANS/CONDITIONS

print(True)
print(False)
print("True")
print(type(True))
print(4>3)
print(not True)
print(not False)
print(2>=2)
print(2!=3)
print(3!=2)
print(3==2)
print("hi"=="hi")
print(3.2>5)

# IF STATEMENTS

x = 9

if x > 7:
  print(1)
  print(2)
print(3)

# INTRODUCTION TO LISTS
grocery_list = ["banana", "orange", "blueberries"]

print(grocery_list)
grocery_list.append("fruit")
print(grocery_list)
print(type(grocery_list))

# FOR LOOPS

for i in grocery_list:
    print(i)
    
# to understand more about the 'range' function

print(list(range(5)))
    
# print(grocery_list[4]) ## this will show that the index is out of range because there's nothing on index value = 4
# print(grocery_list[1]) ##accessing items with their index values

for i in range(len(grocery_list)):
    print(grocery_list[i])
    
for i,item in enumerate(grocery_list):
    print(i+1, item)

# INCREMENT AND DECREMENT

i = 0
i += 1
print(i)
i -= 1
print(i)

# WHILE LOOPS

j = len(grocery_list) - 1
while j >= 0:
    print(grocery_list[j])
    j-=1

i = 0
while i < len(grocery_list):
    print(grocery_list[i])
    i+=1
    
if False:
    print("1")
elif False:
    print("2")
else:
    print("3")

