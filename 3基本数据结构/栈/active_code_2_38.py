"""
堆栈实现十进制转二进制、十六进制、八进制等
"""
'''
@Time    : 2018/2/4 下午8:30
@Author  : scrappy_zhang
@File    : active_code_2_38.py
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


def baseConverter(decNumber, base):
    """
    :param decNumber: 要转换的十进制数
    :param base: 需要的进制
    :return: 结果
    """
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base
    strtype = {2: '0B', 8: "0o", 16: "0x", 10:"0d"}
    newString = strtype[base]
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString


if __name__ == '__main__':
    print(baseConverter(55, 2))
