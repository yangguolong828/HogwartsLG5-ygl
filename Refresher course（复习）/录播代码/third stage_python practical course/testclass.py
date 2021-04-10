

#创建一个人类
#通过class关键字，进行定义了一个类  class Person:
#类变量
class Person:
    # 类变量
    name = "default"
    age = 0
    gender = 'male'
    weight = 0

    # 构造方法，在类实例化的时候被调用
    def __init__(self, name,age,gender, weight):
        # self.变量名的方式，访问的问题，叫做实例变量
        self. name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    # def set_param(self, name):
    #     self name = name

    # def set_age(self,age):
    #     self.age = age

    @classmethod
    def eat(self):
        print(f"{self.name}  eating")
        print("xxxx")
    def play(self):
        print(f"{self.name} playing")
    def jump(self):
        print(f"{self.name} jump")

# 类方法和实例方法的区别
# 类方法不能访问实例方法
# 类方法使用实例方法需要在实例方法上加装饰器 @classmethod

Person.eat()
zs = Person('zhangsan',20,'nan',130)
zs.eat()
# 类变量和实例变量的区别
# 类变量是需要类来访问的，实例变量需要实例来访问

"""print(Person.name)
Person.name = 'tom'
print(Person.name)

zs = Person('zhangsan',20,'nan',130)
print(zs.name)
zs.name = 'lili'
print(zs.name)"""

# 类的实例化，创建了一个实例
# zs = Person('张三', 20, '男', 130)
# print(zs.name)
# zs.name = '王五'
# print(zs.name)
# zs.eat()
# zs.set_param('张三')
# zs.set_age(20)
# print(f"张三 的姓名是：{zs.name}, 张三的年龄是：{zs.age}")