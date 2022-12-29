num1=input("Enter a number:")
num2=input("Enter a number:")
try:
    res=int(num1)/int(num2)
except ZeroDivisionError:
    print("Exception handled by Yagnesh")
except ValueError:
    print("Exception handled by Thrilok")
except Exception as obj:
    print(obj)
else:
    print(num1, '/' ,num2, '=' ,res)
finally:
    print("Thank You")
print("Visit again at python class in MTCA")

