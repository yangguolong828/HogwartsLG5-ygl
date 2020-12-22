"""
字典的定义和内置函数
"""

# 字典的定义：dict{key ： value}
hogwart_dict = {"a":1,"b":2}
hogwart_dict2 = dict(a=1,b=2)

print("hogwarts_dict",hogwart_dict)
print(type(hogwart_dict))
print("hogwarts_dict2",hogwart_dict2)
print(type(hogwart_dict2))

#字典的内置函数
print(hogwart_dict.keys())
print(hogwart_dict.values())
# 返回被删除的键值对
print(hogwart_dict.pop("a"))
#删除掉上面的键值对后剩余的元素
print(hogwart_dict)
a = {}
b = a.fromkeys([1,2,3],"a")
print(b)

