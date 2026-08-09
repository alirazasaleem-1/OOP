# Practice: Create student class that takes name, & marks of 3 subjects as arguments in constructor Then create a method to print the average.

class Student:
    def __init__(self,name: str, marks: list):
        self.name = name 
        self.marks = marks 

    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val 
        print(f"Hi {self.name}, Your average socre is {sum/3} ")

s1 = Student("Ali", [98, 97, 99])
s1.get_avg()