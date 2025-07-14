class Fruit:
    def __init__(self):
        self.name = "apple"
        self.colour = "red"

my_fruit = Fruit()

my_fruit.name = "kiwi"
my_fruit.colour = "green"

print(my_fruit.name)
print(my_fruit.colour)

class Fruit:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    def details(self):
        print("my " + self.name + " is " + self.colour)

apple = Fruit("apple", "red")
banana = Fruit("banana", "yellow")
apple.details()