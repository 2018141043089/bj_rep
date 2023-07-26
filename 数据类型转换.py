num1 = 1
str1 = '10'
print(type(float(num1)))
print(type(float(str1)))
print(float(str1))
print(type(str(num1)))

list = [10, 20, 30]
print(tuple(list))#列表转换为元组

#eval()——计算字符串中的有效python表达时，并返回一个对象
#其实就是把字符串中的数据转换为它原本的类型
str2 = '1'
str3 = '10.2'
str4 = '(10,20,30)'
str5 = '{10,20,30}'
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))



num = input('请输入数字：')
print(num)
print(type(num))
print(type(int(num)))






