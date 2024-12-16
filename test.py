a = [1,2,3]
b = [1,2,3]

print(a is b)

"""
The code returns False because the is operator checks for object identity, 
meaning it checks whether a and b refer to the same object in memory.

In your code, a and b are two separate lists that contain the same elements, but they are distinct objects. 
When you create a and b, Python allocates separate memory for each list, so they have different identities. 
Therefore, a is b evaluates to False.
"""
