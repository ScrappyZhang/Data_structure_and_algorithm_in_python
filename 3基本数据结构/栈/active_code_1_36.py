"""
栈实现简单的括号数量成对匹配：

一般编程语言都需要实现括号匹配
"""
'''
@Time    : 2018/2/4 下午7:56
@Author  : scrappy_zhang
@File    : active_code_1_36.py
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


def parChecker(symbolString):
    """

    :param symbolString: 要识别的字符串
    :return: 若成对括号数量，则返回True
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            elif symbol == ")":
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

if __name__ == '__main__':
    print(parChecker('(((a))1)'))
    print(parChecker('(()'))
