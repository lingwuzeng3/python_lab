#初始化字符串
from operator import index

s = r'http://sports.sina.com.cn/'

#字符中字母t出现的数字
print(s.count('t'))

#字符串的所有'.'替换成'-'
s = s.replace('.','-')
print(s)
#提取字符串sports和sina
ind1 = s.find('sport')
print(s[ind1:ind1+len('sports')])
ind2 = s.rfind('sina')
print(s[ind2+len('sina')-1:ind2-1:-1])
#将字符串的字母全变成大写
s = s.upper()
print(s)

#输出字符串总字符个数
print(len(s))

#在字符串后面添加子字符串index
s+='index'
print(s)
