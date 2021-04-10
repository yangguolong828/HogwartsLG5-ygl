

# 字典定义
a  = {"a": 1, "b": 2}
b = dict(a=1,b=2)

print(a)
print(type(a))
print(b)
print(type(b))

# 内置函数
# 找到key为a的值并删除该键值对
print(a.pop("a"))
print(a)

d = c.fromkeys([1,2,3], "a")
print(d)

# 列表推导式
print({i: i * 2 for i in range(1, 9)})