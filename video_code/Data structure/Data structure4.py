"""
集合的定义和内置函数
"""

# 集合的定义
a = {1,2,3}
b = {1,4,5}
i = set()
print(len(i))#打印集合长度

# 集合的内置函数
print(type(a))
print(type(b))#打印类型
print(a.union(b))#打印集合并集
print(a.intersection(b))#打印集合交集
print(a.difference(b))#打印集合差集
a .add("a")#添加元素
print(a)

#去重
c = "asdjhasdkkadjwejfadjkhsak"
print(set(c))