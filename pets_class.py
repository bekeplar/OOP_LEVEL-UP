"""Parent class"""
class Pets:
    

    dogs = []


    def __init__(self,dogs):
        self.dogs = dogs


"""Another parent class"""
class Dog:

    """Class attribute"""
    species = "mammal"

    """Initialising instance attributes"""
    def __init__(self,name,age):
        self.name = name
        self.age = age

    """Create instances of the dogs"""

dogs = [
    Dog("Tom", 6), 
    Dog("Fletcher", 7), 
    Dog("Larry", 9)
]
