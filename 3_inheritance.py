# Task 3: Inheritance

class Animal:
    def speak(self):
        print("Speaks")

class Dog(Animal):
    def speak(self):
        print("Bark")
    
class Cat(Animal):
    def speak(self):
        print("Meow")

class Cow(Animal):
    def speak(self):
        print("Moo")


dog = Dog()
cat = Cat()
cow = Cow()

dog.speak()
cat.speak()
cow.speak()