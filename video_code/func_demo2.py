"""
默认参数
默认参数在定义函数的时候使用k=v的形式定义。
调用函数时，如果没有传递参数，则使用默认参数。
如果传递参数的话，那么就用传递的参数
"""

def func2(a):
    print("参数a的值为", a)
func2(2)