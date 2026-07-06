# Task 2: Abstraction

class CoffeeMachine:

    def boil_water(self):
        print("Boil the water")
    
    def grind_beans(self):
        print("Grind the beans")
    
    def brew_coffee(self):
        print("Brew the coffee")
    
    def pour_coffee(self):
        print("Pour the coffee into the cup")
    
    def make_coffee(self):
        self.boil_water()
        self.grind_beans()
        self.brew_coffee()
        self.pour_coffee()

machine = CoffeeMachine()

machine.make_coffee()