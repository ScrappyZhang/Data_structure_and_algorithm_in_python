"""

堆栈实现进制转换


整个算法将分成三个部分：

1. 将原始数字减少为一系列单个位数字。
2. 使用查找将单个位数字数字转换为字符串。
3. 将单个位字符串连接在一起以形成最终结果。

先分割出来的是低位数，压入堆栈，


当在 Python 中调用函数时，会分配一个栈来处理函数的局部变量。
当函数返回时，返回值留在栈的顶部，以供调用函数访问。

栈帧还为函数使用的变量提供了一个作用域。 即使我们重复地调用相同的函数，
每次调用都会为函数本地的变量创建一个新的作用域。
"""
'''
@Time    : 2018/2/5 下午2:40
@Author  : scrappy_zhang
@File    : activecode_1_46.py
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


def toStr(n, base):
    """
    堆栈实现进制转换
    :param n: 要转换的数
    :param base: 要转换的进制
    :return: 结果
    """
    rStack = Stack()
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res


if __name__ == '__main__':
    print(toStr(1453, 16))
