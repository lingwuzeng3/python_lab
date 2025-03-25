import math
import turtle as t
#第一题
r = eval(input("请输入圆的半径:"))
area = math.pi*r*r
print("圆的面积为:",area)
#第二题
r2 = eval(input("请输入圆柱体的半径:"))
h = eval(input("请输入圆柱体的高度:"))
volume = math.pi*r*r*h
print("半径为{}高为{}的圆柱体体积为:{:.2f}".format(r,h,volume))
#第三题
t.pensize(3)
t.right(90)
t.penup()
t.forward(200)
t.pendown()
t.left(90)
r = 200
t.circle(200)
len = r*math.sqrt(3)
t.left(60)
t.forward(len)
t.left(120)
t.forward(len)
t.left(120)
t.forward(len)
#第四题
t.color('red')
for x in range(20):
    t.shape('turtle')
    t.circle(100,360)
    t.left(18)
t.done()
