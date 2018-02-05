"""汉诺塔游戏"""
'''
@Time    : 2018/2/5 下午3:16
@Author  : scrappy_zhang
@File    : activecode_1_410.py
'''

"""
fromPole, toPole, withPole
起始杆、目标杆、中间杆、


这里是如何使用中间杆将塔从起始杆移动到目标杆的步骤：

1. 使用目标杆将 height-1 的塔移动到中间杆。（此时目标为中间杆、中间为目标杆、起始为起始杆）
2. 将剩余的盘子移动到目标杆。
3. 使用起始杆将 height-1 的塔从中间杆移动到目标杆。（此时目标为目标感、中间为起始杆、起始为中间杆）


"""

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

moveTower(4,'左','右','中',)