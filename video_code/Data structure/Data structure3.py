"""
元組的定義
"""
# tuple_hogwarts1 = (1,2,3)
# tuple_hogwarts2 = 1,2,3
#
# print("tuple_hogwarts1", tuple_hogwarts1)
# print(type(tuple_hogwarts1))
#
# print("tuple_hogwarts2", tuple_hogwarts2)

# print(type(tuple_hogwarts2))

# 元组的不可变特性
list_hogwarts1 = [1,2,3]
list_hogwarts1[0] = "a"
print(list_hogwarts1)


tuple_hogwarts1 = (1,2,list_hogwarts1)
print(id(tuple_hogwarts1[2]))
tuple_hogwarts1[2][0] = "a"
print(id(tuple_hogwarts1[2]))
print(tuple_hogwarts1)

#元组的可用函数

a = (1,2,3,"a","a","a")
# print(a.count("a"))
print(a.index(3))