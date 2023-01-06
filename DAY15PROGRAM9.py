def fun1():
    x="Yagnesh"
    def fun2():
        nonlocal x
        x="Hello"
    fun2()
    return x
print(fun1())
