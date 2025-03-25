
num = eval(input("请输入一个正整数:"))

i = 2

print(f"{num} =",end='')

while i<=num:
    if not num%i:
        print(f" {i} *",end='')
        num/=i
    else:
        i+=1
print('\b')

