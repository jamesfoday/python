# Practice script: inheritance_practice.py

class Animal:
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return f"\nClass: Animal\nName: {self.name}\nAge: {self.age}"


class Cat(Animal):
    def speak(self):
        print("Meow")

    def __str__(self):
        return f"\nClass: Cat\nName: {self.name}\nAge: {self.age}"


class Dog(Animal):
    def speak(self):
        print("Woof!")

    def __str__(self):
        return f"\nClass: Dog\nName: {self.name}\nAge: {self.age}"


class Human(Animal):
    def __init__(self, name, age):
        super().__init__(age)  # Call parent constructor to set age
        self.set_name(name)    # Set name using parent method
        self.friends = []

    def add_friend(self, friend_name):
        self.friends.append(friend_name)

    def show_friends(self):
        print(f"{self.name}'s friends:")
        for friend in self.friends:
            print(f" - {friend}")

    def speak(self):
        print(f"Hello, my name's {self.name}!")

    def __str__(self):
        friends_str = "\n".join(self.friends)
        return f"\nClass: Human\nName: {self.name}\nAge: {self.age}\nFriends:\n{friends_str}"


class Car:
    id_counter = 0

    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        self.id = Car.id_counter
        Car.id_counter += 1

    def __str__(self):
        return f"\nID: {self.id}\nName: {self.name}\nModel: {self.model}\nYear: {self.year}"


# --- Main code to test the classes ---
if __name__ == "__main__":
    # Test Animal and subclasses
    cat = Cat(3)
    cat.set_name("Stripes")
    print(cat)
    cat.speak()

    dog = Dog(6)
    dog.set_name("Bubbles")
    print(dog)
    dog.speak()

    # Test Human subclass with friends
    human = Human("Tobias", 35)
    human.add_friend("Robert")
    human.add_friend("Élise")
    human.add_friend("Abdullah")
    print(human)
    human.speak()
    human.show_friends()

    # Test Car class with unique IDs
    c0 = Car("Ford", "Shelby GT500", "2015")
    c1 = Car("Toyota", "Corolla", "2012")
    c2 = Car("BMW", "Z3", "2001")
    print(c0)
    print(c1)
    print(c2)
