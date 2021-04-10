name = "hogwarts"
age = 5
num = 3.1415926
list1 = [1,2,3,4,5]
dict1 = {"name": "tom", "gender": "male"}
namelist = ['tom','jerry','tony','buluse']

print('my name is %s, my age is %d, num is %f'%(name, age, num))
print('my name is {1}, my age is {2}, num is {0}'.format(num, name, age))
print('my list is {}, dict is {}'.format(list1, dict1))
# *namelist--列表解包
print('we name : {}、 {}  and {}'.format(*namelist))
# **dict1--字典解包
print('my name is {name}, gender is {gender}'.format(**dict1))
