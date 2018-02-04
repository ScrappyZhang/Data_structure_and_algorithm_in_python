"""

堆栈实现十进制转二进制

"""
'''
@Time    : 2018/2/4 下午8:24
@Author  : scrappy_zhang
@File    : active_code_1_38.py
'''


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def divideBy2(decNumber):
    """
    :param decNumber: 要转换的十进制数
    :return: 返回二进制字符串
    """
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString


if __name__ == '__main__':
    print(divideBy2(22))
