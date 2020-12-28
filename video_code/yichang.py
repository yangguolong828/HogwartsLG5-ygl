
try:
    num1 = int (input("请输入一个除数"))
    num2 = int (input("请输入一个被除数"))
    print(num1/num2)
# except ZeroDivisionError:
#     print("被除数不能为0")
# except ValueError:
#     print("输入的数据需要是数值型整数")
except:
    print("这是一个能用型异常")
finally:
    print("无论发生什么都执行此操作")