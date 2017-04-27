#循环
#要计算1+2+3，我们可以直接写表达式：1 + 2 + 3要计算1+2+3+...+10，勉强也能写出来。

#但是，要计算1+2+3+...+10000，直接写表达式就不可能了。

#为了让计算机能计算成千上万次的重复运算，我们就需要循环语句。

#Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：
names=['Niqhang','Zhuzutong','Lixiaoqi','Luodelong']
for name in names:
    print(name)

#所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。

#再比如我们想计算1-10的整数之和，可以用一个sum变量做累加：
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print(sum)

#如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
print(list(range(5)))

#range(101)就可以生成0-100的整数序列，计算如下：
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)
#在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出。

#在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：

n=1
while n<=100:
    if n>10:
        break
    print(n)
    n=n+1
print('END')
#可见break的作用是提前结束循环。

#continue
#在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
n=0
while n<10:
    n=n+1
    if n%2==0:
        continue
    print(n)
#可见continue的作用是提前结束本轮循环，并直接开始下一轮循环。
