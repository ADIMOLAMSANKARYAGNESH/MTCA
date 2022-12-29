def Factorial(num):
    assert(isinstance(num,int)),"Factorial is not defined for non-integer"
    assert(num>=0),"Factorial of negative number is not defined"
    if num==0:
        return 1
    else:
        return num*Factorial(num-1)
try:
    print(Factorial(-5))
except Exception as obj:
    print(obj)
try:
    print(Factorial(5.5))
except Exception as obj:
    print(obj)
try:
    print(Factorial('today'))
except Exception as obj:
    print(obj)
try:
    print(Factorial(5))
except Exception as obj:
    print(obj)
print("Thank You")
