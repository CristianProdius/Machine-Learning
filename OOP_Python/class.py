class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    """def add_one(self, x):
        return x+1
    
    def bark(self):
        print("Bark")"""

d = Dog("Tim", 42)
d.set_age(14)
print(d.get_age())


#d.bark()      #calllinf the bark method from the class dog
#print(d.add_one(5)) 
#print(type(d))