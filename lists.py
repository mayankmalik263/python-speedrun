l = [1,2,3]
l.append(4) # just adds the given argument/value to the end of the list

print(l)
l.insert(0, "Hi") # this will place the value in the given index that you put in it
print(l)
l.append(4)
print(l.count(4)) # this return the occurrence of the given argument in the list
l.reverse() # reverse actually reverses the list instead of just returning the reverse of the list
print(l)
l.remove(3) # this actually removes the character from the actual list
print(l)
# HAVE TO THE LIST SLICING MYSELF it wasn't given in the tutorial

l = []

for i in range(5): # this goes from 0 to 4 --> 0 1 2 3 4
    for j in range(3): # and then for 0 this loop will run from 0 1 2 
        if (i+j) % 2 == 0:
            l.append(i+j)
print(l)
        # so the explanation of the code can be as following
'''
        For i = 0:
            j = 0: 0 + 0 = 0 (even) → append 0
            j = 1: 0 + 1 = 1 (odd) → do not append
            j = 2: 0 + 2 = 2 (even) → append 2
        For i = 1:
            j = 0: 1 + 0 = 1 (odd) → do not append
            j = 1: 1 + 1 = 2 (even) → append 2
            j = 2: 1 + 2 = 3 (odd) → do not append
        For i = 2:
            j = 0: 2 + 0 = 2 (even) → append 2
            j = 1: 2 + 1 = 3 (odd) → do not append
            j = 2: 2 + 2 = 4 (even) → append 4
        For i = 3:
            j = 0: 3 + 0 = 3 (odd) → do not append
            j = 1: 3 + 1 = 4 (even) → append 4
            j = 2: 3 + 2 = 5 (odd) → do not append
        For i = 4:
            j = 0: 4 + 0 = 4 (even) → append 4
            j = 1: 4 + 1 = 5 (odd) → do not append
            j = 2: 4 + 2 = 6 (even) → append 6
            
Final Output:

After all iterations, the list l would contain the values [0, 2, 2, 2, 4, 4, 4, 6].
'''