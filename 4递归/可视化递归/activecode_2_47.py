"""
turtle 模块：递归绘制树
"""
'''
@Time    : 2018/2/5 下午2:54
@Author  : scrappy_zhang
@File    : activecode_2_47.py
'''

import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-10,t)
        t.left(40)
        tree(branchLen-10,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(70,t)
    myWin.exitonclick()

main()