#在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A'))
print(ord('倪'))
print(chr(66))
print(chr(25991))
#如果知道字符的整数编码，还可以用十六进制这么写str：
print('\u4e2d\u6587')
