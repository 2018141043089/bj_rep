#coding=utf-8
import sys
print(sys.version)

'''
准备数据
格式化符号输出数据
'''



age = 18
name = "tom"
weight = 75.5
stu_id1 = 1
stu_id2 = 1000

#我的年龄是X岁——整数 %d
print('我的年龄是%d岁' % age)

#我的名字是X——字符串 %s
print('我的名字是%s' % name)

#我的体重是X公斤——浮点数 %f
print('我的体重是%.2f公斤' % weight)     #.2表示小数点后是两位数字，否则则默认保留6位小数

#我的学号是X——整数 %d
print('我的学号是%03d公斤' % stu_id1)     #解决位数对齐的问题，不足的补全
print('我的学号是%03d公斤' % stu_id2)     #超出的原样输出

#我的名字是X，今年X岁了
print('我的名字是%s，今年%d岁' % (name, age))
print('我的名字是%s，明年%d岁' % (name, age+1))

print('我的名字是%s，今年%s岁，体重%s公斤' % (name, age, weight))

#f'{表达式}'
#print(f'我的名字是{name}，今年{age}，体重{weight}')
#print(f'我的名字是{name}，今年{age}，明年{age + 1}, 体重{weight}')

#转义字符
print('hello\npython')
print('\tpython')
#print('hello', end="\t")
#print('world', end="\n")
#print('hello', end="\t")
#print('python', end="……")