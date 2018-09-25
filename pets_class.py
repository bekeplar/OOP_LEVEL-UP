"""Parent class"""

class Pets:
    
    dogs = []


    def __init__(self,dogs):
        self.dogs = dogs


"""Another parent class separate from pet"""
class Dog:

    """Class attribute"""
    species = "mammal"

    """Initialising instance attributes"""
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.hungry = True


    """Instance method"""
    def eat(self):
        self.is_hungry = False

    are_dogs_hungry = False
    for dog in Pets.dogs:
        if dog.is_hungry:
            are_dogs_hungry = True

    if are_dogs_hungry:
        print("My dogs are hungry.")
    else:
           print("My dogs are not hungry.")   



    """Create instances of the dogs"""


Pets.dogs = [
    Dog("Tom", 6), 
    Dog("Fletcher", 7), 
    Dog("Larry", 9)
]
