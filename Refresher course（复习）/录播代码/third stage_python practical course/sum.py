"""
计算1-100 求和
加入分支结构实现1-100偶数求和
实现1-100偶数和
"""

def sum1():
    result = 0
    for i in range(101):
        result=result+1
    print(result)

def sum2():
    result = 0
    for i in range(101):
        if i%2==0:
            result = result + 1
    print(result)

def sum3():
    result = 0
    for i in range(2,101,2):
        result = result + 1
    print(result)
