import sys

num = 1

while True:
    big = sys.getsizeof(num)
    print("num = {},sizeof为{}".format(num,big))
    num*=2
    if num>=sys.maxsize:
        break

