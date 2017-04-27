classmates=['Niqihang','Lixiaoqi','Yewensen']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
#当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。

#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print(classmates[-1])
#以此类推，可以获取倒数第2个、倒数第3个：
print(classmates[-2])
print(classmates[-3])

#list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('Zhuzutong')
print(classmates)
#也可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(1,'Luodelong')
print(classmates)
#要删除list末尾的元素，用pop()方法：
classmates.pop()
print(classmates)
#要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1)
print(classmates)
#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1]='Qinjie'
print(classmates)

#list里面的元素的数据类型也可以不同，比如：
L=['Niqihang',123,True]
print(L)
#list元素也可以是另一个list，比如：
s=[['Niqhang','Qinjie'],'Zhuzutong',123]
print(len(s))
#要注意s只有3个元素，其中s[0]又是一个list，如果拆开写就更容易理解了：
p=['Niqihang','Qinjie']
s=[p,123,True]
#要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到。
print(s[0][1])

#如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
L=[]
print(len(L))