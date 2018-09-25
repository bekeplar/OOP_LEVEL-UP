"""Parent class"""
class Pets:
    

    dogs = []


    def __init__(self,dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())
    


"""Another parent class"""
class Dog:

    """Class attribute"""
    species = "mammal"
    is_hungry = True

    """Initialising instance attributes"""
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.is_hungry = True

    """Instance method"""
    def eat(self):
        self.is_hungry = False


    

    def walk(self):
        return "%s is walking!" % (self.name)

    
    """Create instances of the dogs"""
pets = Pets(dogs = [
    Dog("Tom", 6), 
    Dog("Fletcher", 7), 
    Dog("Larry", 9)
])

are_dogs_hungry = False
for dog in pets.dogs:
    if dog.is_hungry:
        are_dogs_hungry = True

if are_dogs_hungry:
    print("My dogs are hungry.")
else:
        print("My dogs are not hungry.") 

pets.walk() 


#output