"""
更精准的符号匹配

如下面的均为不匹配符号：
( [ ) ]
( ( ( ) ] ) )
[ { ( ) ]
如下面的才算匹配符号：
{ { ( [ ] [ ] ) } ( ) }
[ [ { { ( ( ) ) } } ] ]
[ ] [ ] [ ] ( ) { }

"""
'''
@Time    : 2018/2/4 下午8:03
@Author  : scrappy_zhang
@File    : active_code_1_37.py
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
    :return: 若符号匹配，则返回True
    """
    s = Stack()
    balanced = True
    index = 0
    leftpar = '([{'
    rightpar = ')]}'
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in leftpar:
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            if symbol in rightpar:
                if rightpar.index(symbol) != leftpar.index(s.peek()):
                    return False
                else:
                    s.pop()
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


if __name__ == '__main__':
    print(parChecker('{{([111][222])}00()}'))
    print(parChecker('[{()]'))
