""""
练习：如果我们想生成一个平方列表，比如[1,4,9...]，使用for循环应该怎么写，使用列表生成式又应该怎么写呢?
"""
list_square = []
for i in range(4):
    list_square.append(i**2)
print(list_square)

# 0-4平方值
list_square2 = [i**2 for i in range(4)]
print("list_square2 =", list_square2)

# 0-4平方值除1之外
list_square3 = [i**2 for i in range(4) if i !=1]
print(list_square3)

list_square4 = [i*j for i in range(1,4) for j in range(1,4)]
print(list_square4)