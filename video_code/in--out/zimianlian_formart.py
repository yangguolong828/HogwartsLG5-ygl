name = 'ygl'
age = 20
list1 = [1,2,3,4]
dic1 = {'name' :'tom', 'gender': 'male'}

print('my list is {1}, dict is {0}'.format(list1,dic1))
print('my name is {1},age is {0}'.format(name,age))

namelist = ['lili','tom','jerry']
print('we name : {} 、{} and {} '.format(*namelist))

print('my name is {name}, gender is {gender}'.format(**dic1))