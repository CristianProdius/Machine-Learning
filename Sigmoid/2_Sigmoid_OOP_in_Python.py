class Human:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    
    def sleeping(self):
        print("I am sleeping")


class Student(Human):
    def __init__(self, name, surname, grates, comments): #__init__ represents a class, constractor are reserved methods that helps inizialize the objects
        self.__name = name
        self.surname = surname
        self.grates = grates
        self.comments = comments

    def average_grade(self):
        avg = 0
        for value in self.grates.values():
            avg += sum(value)/len(value)
        return avg/len(self.grates.keys())
    
    def sleeping(self):
        print("Student is sleeping") #sleeping() method was overwrite here


class Teacher:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def sleeping(sefl):
        print("Teacher is sleeping")

    


human1 = Human('Alex', 'Pierce')
human1.sleeping()

grades = {'Informatics':[7,9,8], 'Math':[7,9,8]}
student1 = Student('Alex','Pierce', grades, 'Good student') #student is the constructor
student1.sleeping()

teaher1 = Teacher('Mihai', 'Afgoni')

for object in (student1, teaher1):
    object.sleeping()

#print(student1.average_grade())

#student1.name = 'Cristian' #this line change the name of the student form the class defined above
#print(student1.name)
#print(student1.grates)
#print(student1.comments)