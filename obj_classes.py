# class = factory that makes humans

class human:
    """"
#:    The __init__ method in the human class is a special method in Python known as a constructor. 
##    It is automatically called when a new instance (object) of the class is created. 
##    The primary purpose of the __init__ method is to initialize the attributes of the object with the values provided when the object is instantiated.

#  @ In the context of the human class:
#      - The __init__ method takes three parameters: self, name, and age.
#      - self refers to the instance of the class that is being created.
#      - name and age are the values that are passed when creating a new human object.
#      - Inside the __init__ method, the attributes _name and _age of the instance are set to the values of name and age, respectively. 
#      - This allows each human object to have its own unique name and age.
    """
    def __init__(self, name, age): # so self is not an error here self in python refers to the human that we have created here
        # means ki self is the object of the class that we have created
        self._name = name
        self._age = age

    def __str__(self):
        return "A human with the name: " + self._name + " and age: " + str(self._age)
    
    # def __repr__(self):
    #     return "Hi"
    # def add_age(self):
    #     return self._age*2 
    def older_younger_than(self, age):
        if self._age > age:
            print("Our age is greater than their's")
        elif self._age == age:
            print("Our age is equal to their's")
        else:
            print("Our age is less than their's")
h1 = human(age = 18,name = "Mayank") # so we have made a human here
h2 = human("Manmeet",19) # and this is the value of the object we gave every time in the class, 
                         # we have to give the values of the parameters that we have defined in the class
# h1 and h2 are instances which are used at the moment of creation of the object
# h1 and h2 are objects of the class human
print(h1.__str__()) 
print(h2)
# print(h1.add_age(), h2.add_age())
h2.older_younger_than(18) # means ki h2 ki age zayada h hamari inputted argument age se i.e. is 18 and h2's age is 19

#: WELL:- the human class has 3 methods or "functions"
## 1. __init__ method: This is a special method in Python known as a constructor
## 2. __str__ method: This method is used to return a string representation of the message
## 3. __repr__ method: This method is used to return a string representation of the message(for google colab only)