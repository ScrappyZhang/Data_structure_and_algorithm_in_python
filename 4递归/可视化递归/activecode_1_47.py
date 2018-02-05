"""
turtle 模块：递归绘制螺旋图
"""
'''
@Time    : 2018/2/5 下午2:48
@Author  : scrappy_zhang
@File    : activecode_1_47.py
'''

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,300)
myWin.exitonclick()