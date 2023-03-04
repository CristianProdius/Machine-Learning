class Pet():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I dont know what to speak")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meaw")
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old, and I am {self.color}")

p = Pet("Jora", 49)
#p.show()
p.speak()
d = Dog("Tolea", 9)
d.speak()
c = Cat("Alex", 5, "brown")
c.show()
c.speak()

