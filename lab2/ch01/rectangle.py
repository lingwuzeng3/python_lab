
length = eval(input("请输入长方体的长："))
width = eval(input("请输入长方体的宽："))
height = eval(input("请输入长方体的高："))

area = 2*(length*width+width*height+height*length)
volume = length*height*width

print(f"长方体的面积为{area},体积为{volume}")

