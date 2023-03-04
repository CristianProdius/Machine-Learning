class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 -100

    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, course, max_students):
        self.course = course
        self.max_students = max_students
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)
    

s1 = Student("Cristian", 19, 99)
s2 = Student("Jora", 20, 69)
s3 = Student("Bobic", 19, 75)

course = Course("Science", 2)
course.add_students(s1)
course.add_students(s2)

print(course.add_students(s3))
print(course.get_average_grade())