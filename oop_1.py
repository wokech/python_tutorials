# Define class

class Person:
    def __init__(self, first_name, last_name):
        self.fn = first_name
        self.ln = last_name
        self.full_name = f"{first_name} {last_name}"

    def introduction(self):
        print(self)
        print(f"Hello! My name is {self.full_name}. I am a human... Trust me.")

    @classmethod
    def help(cls):
        print(cls)
        print("Do you really need help, or are you just testing me?")

p = Person("Daniel", "Pleh")
p.introduction()
Person.help()
p.help()

# Create object
p = Person("MJ", "Watamu")

# Access attributes

print(f"First name = {p.fn}")
print(f"Last name = {p.ln}")
print(f"Full name = {p.full_name}")

# Class vs Instance Things

class Person:
    counter = 0 # Class attribute, number of Person objects

    def __init__(self, name):
        self.full_name = name # Instance attribute
        Person.counter += 1 # Increment the class attribute

    def introduction(self):
        # Instance method uses self to access the instance attribute
        print(f"\nHello! My name is {self.full_name}. I am human... Trust me.")

    @classmethod
    def population(cls):
        # Class method uses cls to access the class attribute
        print(f"The current population is {cls.counter}")

p1 = Person("Jeff Schroeder")
p1.introduction() # Calling an instance method
p1.population() # Calling a class method via an instance

p2 = Person("Juergen Pichler")
p2.introduction() 
Person.population() # Calling a class method via the class

p3 = Person("Andrew T")
p4 = Person("James V")

p4.coin = 123081723

Person.version = 1.0

print("\n", dir(p3))
print("\n", dir(p4)) # coin only appears in p4
print("\n", dir(Person))

