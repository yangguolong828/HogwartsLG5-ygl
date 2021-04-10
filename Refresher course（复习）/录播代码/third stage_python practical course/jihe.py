

# 集合的定义
a = {1}
b = set()
print(len(b))

print(type(a))
print(type(b))


# 集合的内置函数
aa = {1,2,3}
bb = {1,2,4}

# 求并集
print("aa的并集是",aa.union(bb))

# 求交集
print("aa的交集是",aa.intersection(bb))

#求差集
print("aa的差集是",aa.difference(bb))

# 添加集合元素
aa.add("a")
print(aa)