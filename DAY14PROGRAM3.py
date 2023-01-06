class animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color
class cat(animal):
    def mew(self):
        print("cat meows")
class dog(animal):
    def bark(self):
        print("woof")
if __name__ == "__main__":
    print(__name__)
    pet1=dog("tommy","brown")
    pet2=cat("lucy","white")
    pet1.bark()
    pet2.mew()
    print(pet1.name)
    print(pet2.name)
