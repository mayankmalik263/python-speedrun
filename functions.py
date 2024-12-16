# FUNCTIONS

def my_print(s): # s is a parameter here and what happens is parameter = argument i.e, s = "Hello"
    print(s)
    
my_print("Hello") # Hello is an argument here 
# this is the value of s and it goes to s = "Hello" and then goes to the print statement and then printed

def square(num): # num is a local scope variable here
    print(num*num)

square(5)

def cube(number):
   print(number**3)

cube(5)
print(cube(5)) # None

def fourth(num):
    return num**4
print(fourth(3))

def append_in_list(lst):
    lst.append(4)
    
a = [1,2,3]
append_in_list(a)
print(a)
b = a
print(a is b)
print(a is [1,2,3,4]) # list is the same in value only but it is stored in different locations on your computer

# now if we change a
a[0] = 7
print(a)
print(b) # b will be also equal to a

from copy import deepcopy # this will make b like that if we even modify a then it will be not change b

b = deepcopy(a)
print(b)

a[2] = 12
print(a)
print(b)

q = 4
w = q
print(w,q)
q = 5
print(w,q)
def add_1(x):
    # x = 8
    x = [1,2]
    return x
print(add_1(4))

def add_2(y):
    print(y is lst_1)
    y = [1,2]
    print(y is lst_1)
    return y
lst_1 = [1,2,3]
print(add_2(lst_1))
print(lst_1)

def practice(z):
    # z.append(7)
    z = [1,2]
    z.append(7)
    return z
list_2 = [1,2,3,4,5,6]
print(practice(list_2))
print(list_2)

def add(a, b):
    return a + b
print(add(5, 9))

def addition(a,b,c=4):
    return a + b + c

print(addition(5,8))


