"""
运算公式由中缀转换为后缀
"""

"""
1. 创建一个名为 opstack 的空栈以保存运算符。给输出创建一个空列表。
2. 通过拆分将输入的中缀字符串转换为标记列表。
3. 从左到右扫描标记列表。
   - 如果标记是操作数，将其附加到输出列表的末尾。
   - 如果标记是左括号，将其压到 opstack 上。
   - 如果标记是右括号，则弹出 opstack，直到删除相应的左括号。将每个运算符附加到输出列表的末尾。
   - 如果标记是运算符，*，/，+或 - ，将其压入 opstack。
        但是，首先删除已经在 opstack 中具有更高或相等优先级的任何运算符，并将它们加到输出列表中。
4. 当输入表达式被完全处理时，检查 opstack。仍然在栈上的任何运算符都可以删除并加到输出列表的末尾。

"""
'''
@Time    : 2018/2/4 下午9:07
@Author  : scrappy_zhang
@File    : active_code_1_39.py
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


def infixToPostfix(infixexpr):
    """
    :param infixexpr:要转换的公式字符串
    :return: 返回后缀字符串
    """
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()  # 运算符堆栈
    postfixList = []  # 后缀表达式列表
    tokenList = kill_space_split(infixexpr)

    for token in tokenList:
        if token.isalpha() or token.isdigit():  # 假设只有纯数字和纯字母两种数
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)  # 将左括号压入堆栈
        elif token == ')':
            topToken = opStack.pop()  # 弹出堆栈中刚进去的运算符
            while topToken != '(':  # 如果它不是左括号，则将其添加到postfixList列表，直到遇到左括号
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):  # 运算符堆栈顶端项与当前操作符比较优先级
                postfixList.append(opStack.pop())  # 当当前操作符优先级小时，把优先级大的操作符添加到postfixList列表
            opStack.push(token)  # 将运算符压入堆栈

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def kill_space_split(sorce_fix):
    """
    拆分为标记列表
    :param sorce_fix: 原始输入公式
    :return: 返回标记列表
    """
    express1 = []
    di = ''
    ai = ''
    temp = ''
    for i in sorce_fix:
        if i != ' ':
            temp += i
    print('初始公式：', temp)
    for i in temp:
        if i.isalpha():
            ai += i
        if i.isdigit():
            di += i
            if temp.index(i) == len(temp) - 1:
                express1.append(di)
        if i in '+-*/()':
            if di:
                # print(di)
                express1.append(di)
                di = ''
            if ai:
                express1.append(ai)
                ai = ''
            express1.append(i)
    # print(express1)
    return express1


if __name__ == '__main__':
    print('后缀公式：', infixToPostfix("A *B + C * D -9"))
    print("后缀公式：", infixToPostfix("( A + par ) * C - ( D - E ) * ( F + G )"))
