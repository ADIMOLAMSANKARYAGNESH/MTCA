def div(a,b):
    assert(isinstance(a,int) or isinstance(a,float)),'First argument should be either integer or float'
    assert(isinstance(b,int) or isinstance(b,float)),'Second argument should be either integer or float'
    assert(b!=0),"Division by zero is not defined"
    return a/b
try:
    print(div(55,0))
except AssertionError as obj:
    print(obj)
try:
    print(div(20,5))
except AssertionError as obj:
    print(obj)
try:
    print(div('hello',20))
except AssertionError as obj:
    print(obj)
try:
    print(div(100,'hello'))
except AssertionError as obj:
    print(obj)
