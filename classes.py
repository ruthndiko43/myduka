class Student:
    def __init__(self,name,student_no,course):
        self.name = name
        self.student_no = student_no
        self.course = course

    def study(self,unit):
        print(f"{self.name} studies {unit}")

    def sleeps(self,time):
        print(f"{self.name} sleeps at {time}")

    def eats(self,food):
        print(f"{self.name} eats {food}")

    def get_details(self):
        print("User details")
        print(f"Name:{self.name} - Student No:{self.student_no} - Course:{self.course}")
        print("---------------------------------")


#object 1
student1 = Student("Jack","S101","Computer Science")
print(type(student1))
print(student1)
student1.get_details()
student1.study("Web Development")
student1.sleeps("10pm")
student1.eats("apples")


#object 2
student2 = Student("Jane","S102","Data Science")
print(type(student2))
student2.get_details()
student2.study("OOP")
student2.sleeps("11pm")
student2.eats("cake")