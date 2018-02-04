"""栈"""
'''
"""
- Stack() 创建一个空的新栈。 它不需要参数，并返回一个空栈。
- push(item)将一个新项添加到栈的顶部。它需要 item 做参数并不返回任何内容。
- pop() 从栈中删除顶部项。它不需要参数并返回 item 。栈被修改。
- peek() 从栈返回顶部项，但不会删除它。不需要参数。 不修改栈。
- isEmpty() 测试栈是否为空。不需要参数，并返回布尔值。
- size() 返回栈中的 item 数量。不需要参数，并返回一个整数。

"""
@Time    : 2018/2/4 下午7:24
@Author  : scrappy_zhang
@File    : active_code_1_35.py
'''

"""
假定列表的结尾将保存栈的顶部元素。
随着栈增长（push 操作），新项将被添加到列表的末尾。 
pop 也操作列表末尾的元素
"""

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