"""
计算列表和

for循环
"""
'''
@Time    : 2018/2/5 下午2:25
@Author  : scrappy_zhang
@File    : activecode_1_43.py
'''


def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum


print(listsum([1, 3, 5, 7, 9]))
