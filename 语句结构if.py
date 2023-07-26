#if语句
age = int(input('请输入年龄：'))
if age >= 18:
    print(f'您输入的年龄是{age}，可以上网')
else:
    print(f'您输入的年龄是{age}，回家写作业去')

age1 = int(input('请输入年龄：'))
#多重条件
if age1 < 18:
    print(f'您输入的年龄是{age1}，童工')
elif 18 <= age1 <= 60:
    print(f'您输入的年龄是{age1}，合法')
elif age1 > 60:
    print(f'您输入的年龄是{age1}，退休年龄')

