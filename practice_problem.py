# Practice: Create student class that takes name, & marks of 3 subjects as arguments in constructor Then create a method to print the average.

class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name 
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def Average(self):
        average = (self.marks1 + self.marks2 + self.marks3) / 3 
        return average 

s1 = Student("Ali", 97, 98, 99)
print(s1.Average())