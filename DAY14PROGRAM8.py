class rohith:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,ob):
        return rohith(self.x+ob.x,self.y+ob.y)
    def __sub__(self,other):
        return rohith(self.x-other.x,self.y-other.y)
first=rohith(5,7)
second=rohith(3,8)
result=first+second
print(result.x)
print(result.y)
result=first-second
print(result.x)
print(result.y)
