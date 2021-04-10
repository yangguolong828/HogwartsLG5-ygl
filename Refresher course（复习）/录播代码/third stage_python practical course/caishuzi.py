"""
猜数字游戏
计算机出一个1-100之间的随机数字由人来猜
计算机根据人猜的数字分别给出提示：大一点/小一点/猜对了
"""
import random


computer_num = random.randint(1,100)
while True:
    person_num = int(input("请输入一个数字"))
    if person_num > computer_num:
        print("小一点")
    elif person_num < computer_num:
        print("大一点")
    elif person_num == computer_num:
        print("猜对了")
        break
