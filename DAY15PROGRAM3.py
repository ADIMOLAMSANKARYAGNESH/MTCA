class Vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage
class Bus(Vehicle):
    pass
Schoolbus=Bus("School Volvo",180,15)
print("Vehicle Name:",Schoolbus.name,"\nSpeed:",Schoolbus.maxspeed,"\nMileage:",Schoolbus.mileage)

