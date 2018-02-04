"""
Python实现Deque双端队列

默认首在列表右端，尾在列表左端
从前面添加和删除项是 O(1)，而从后面添加和删除是 O(n)

- Deque() 创建一个空的新 deque。它不需要参数，并返回空的 deque。
- addFront(item) 将一个新项添加到 deque 的首部。它需要 item 参数 并不返回任何内容。
- addRear(item) 将一个新项添加到 deque 的尾部。它需要 item 参数并不返回任何内容。
- removeFront() 从 deque 中删除首项。它不需要参数并返回 item。deque 被修改。
- removeRear() 从 deque 中删除尾项。它不需要参数并返回 item。deque 被修改。
- isEmpty() 测试 deque 是否为空。它不需要参数，并返回布尔值。
- size() 返回 deque 中的项数。它不需要参数，并返回一个整数。

"""
'''
@Time    : 2018/2/4 下午5:19
@Author  : scrappy_zhang
@File    : listing1_317.py
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
