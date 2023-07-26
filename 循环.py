i = 0
while i < 5:
    print('wy handsome')
    i += 1

#100内数字求和
k = 1
result = 0
while k <= 100:
    result = result + k
    k += 1
print(result)

#100内偶数求和
j = 1
result1 = 0
while j <= 100:
    if j % 2 == 0:
        result1 += j
    j += 1
print(result1)


#break，某些条件成立，退出整个循环
a = 1
while a <= 5:
    if a == 4:
        print('吃饱了不吃了')
        break
    print(f'吃了第{a}个苹果')
    a += 1

#continue，某些条件成立，跳过整个循环
c = 1
while c <= 5:
    if c == 3:
        print('这个苹果不能吃了')
        c += 1
        continue
    print(f'吃了第{c}个苹果')
    c += 1

#for循环
str1 = 'bianjie'
for i in str1:
    if i == 'j':
        break
    print(i)

str2 = 'bianjie'
for i in str2:
    if i == 'j':
        continue
    print(i)

#while else循环
o = 1
while o <= 5:
    if o == 3:
        break  #break直接退出整个while-else
    print('吃饱了我')
    o += 1
else:
    print('真的很开心')

v = 1
while v <= 5:
    if v == 3:
        v += 1
        continue  #break直接退出整个while-else
    print(f'吃了{v}次了')
    v += 1
else:
    print('真的很开心')


#for else
chuan = 'bianjie'
for z in chuan:
    print(z)
else:
    print('循环正常解释执行的else代码')












