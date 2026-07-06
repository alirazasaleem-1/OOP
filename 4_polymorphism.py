# Task 4: Polymorphism

class Bird:
    def move(self):
        print("Bird is flying")

class Fish:
    def move(self):
        print("Fish is swimming")

class Snake:
    def move(self):
        print("Snake is slithering")

bird = Bird()
fish = Fish()
snake = Snake()

bird.move()
fish.move()
snake.move()