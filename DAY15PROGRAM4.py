class Vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage
    def seating_capacity(self,capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"#'f' stands for format
class Bus(Vehicle):
    #assign default value to capacity
    def seating_capacity(self,capacity=50):
        return super().seating_capacity(capacity=50)
Schoolbus=Bus("School Volvo",180,15)
print(Schoolbus.seating_capacity())

   
