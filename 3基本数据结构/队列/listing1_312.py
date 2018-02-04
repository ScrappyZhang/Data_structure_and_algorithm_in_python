"""
python列表实现队列

队首为列表末端、队尾为列表首端。

此时入队复杂度为O(n)
    出队复杂度为O(1)  （回想下pop(i)）


- Queue() 创建一个空的新队列。 它不需要参数，并返回一个空队列。
- enqueue(item) 将新项添加到队尾。 它需要 item 作为参数，并不返回任何内容。
- dequeue() 从队首移除项。它不需要参数并返回 item。 队列被修改。
- isEmpty() 查看队列是否为空。它不需要参数，并返回布尔值。
- size() 返回队列中的项数。它不需要参数，并返回一个整数。

"""
'''
@Time    : 2018/2/4 下午4:12
@Author  : scrappy_zhang
@File    : listing1_312.py
'''

"""
python自带FIFO队列模块

queue.Queue
"""


class Queue:
    """队列FIFO"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        # 是否为空
        return self.items == []

    def enqueue(self, item):
        # 入队
        self.items.insert(0, item)

    def dequeue(self):
        # 出队
        return self.items.pop()

    def size(self):
        # 队列大小
        return len(self.items)
