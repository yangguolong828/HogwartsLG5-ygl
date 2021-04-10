a,b = 0,1
while a < 10:
    print(a)
    print(b)
    a,b = b, a+b
    print("a的值为",a, "b的值为",b)
