def checkEvenOdd(num1):
    assert(num1>0),"Negative numbers"
    if num1%2==0:
        return "Even"
    else:
        return "Odd"
for i in range(2):
    num=int(input("Enter a number:"))
    try:
        print(num,"is",checkEvenOdd(num))
    except AssertionError as obj:
        print(obj)

