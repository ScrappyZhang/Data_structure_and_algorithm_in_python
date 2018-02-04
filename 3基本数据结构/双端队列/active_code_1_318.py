"""
判断一个字符串是否为回文

回文：左右对称，如：radar toot madam
"""
'''
@Time    : 2018/2/4 下午5:29
@Author  : scrappy_zhang
@File    : active_code_1_318.py
'''


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def palchecker(aString):
    """
    :param aString: 被检查的字符串
    :return: 返回布尔值，若为回文，则为真
    """
    chardeque = Deque()  # 创建一个空的双端队列
    # 将字符串字符从尾端添加到双端队列（即首段为字符串首个字符）
    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        # 首尾各退出一个字符，进行对比
        if first != last:
            stillEqual = False

    return stillEqual


print(palchecker("lsdkjfskf"))  # False
print(palchecker("radar"))  # True
