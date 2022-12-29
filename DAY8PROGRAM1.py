#assert is a keyword used to validate the arguments of a function/method
#import builtins
#dir(builtins)
def KelvinToFahrenhrit(Temperature):
    assert (Temperature>=0),"Colder than absolute zero at MTICA!"
    res=((Temperature-273)*1.8)+32
    return res
try:
    print(KelvinToFahrenhrit(-50))
except Exception as ob:
    print(ob)
try:
    print(KelvinToFahrenhrit(273))
except Exception as ob:
    print(ob)
try:
    print(KelvinToFahrenhrit(505.78))
except Exception as ob:
    print(ob)
try:
    print(KelvinToFahrenhrit(-5))
except Exception as ob:
    print(ob)
print("Thank You")
