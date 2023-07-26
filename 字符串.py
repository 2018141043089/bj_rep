#切片

str = '012345678'
print(str[2])
print(str[2:5:1])
print(str[:5])
print(str[2:5:2]) #0123
print(str[::-1])#倒叙
print(str[-4:-1])


#查找 find、index、rindex、rfind、count
mystr = 'hello world and bianjie and wy'
print(mystr.find('and'))    #12
print(mystr.find('and',15,30))      #24
print(mystr.find('ands'))    #-1
#print(mystr.index('ands'))    #报错

print(mystr.rfind('and'))
print(mystr.rindex('and'))

print(mystr.count('and'))


#修改 replace split
newstr = mystr.replace('and', 'or')
print(mystr.replace('and', 'or'))
print(mystr)
print(newstr)

mystr.split('and')
newstr1 = mystr.split('and')
newstr2 = mystr.split('and', 1)
print(newstr1)
print(newstr2)
print(mystr)