"""
实现无序列表： 链表


1、在每个项中保持一些明确的信息，即下一个项的位置；
2、最后一项需要知道自己是最后的一个；
3、第一个位置必须被明确,新项的位置

实现以下五种方法：
- List() 创建一个新的空列表。它不需要参数，并返回一个空列表。
- add(item) 向列表中添加一个新项。它需要 item 作为参数，并不返回任何内容。假定该 item 不在列表中。
- remove(item) 从列表中删除该项。它需要 item 作为参数并修改列表。不存在则返回False，存在返回True。
- search(item) 搜索列表中的项目。它需要 item 作为参数，并返回一个布尔值。
- isEmpty() 检查列表是否为空。它不需要参数，并返回布尔值。
- size（）返回列表中的项数。它不需要参数，并返回一个整数。


"""
'''
@Time    : 2018/2/4 下午5:46
@Author  : scrappy_zhang
@File    : listing_321.py
'''

"""
链表实现的基本构造块是节点
# 每个节点对象必须至少保存两个信息：
    1.节点必须包含列表项本身
    2.每个节点必须保存对下一个节点的引用
"""


class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


"""
UnorderedList 类   无序列表

1.必须保持对第一个节点的引用  head

2.链表的各种操作

    空操作：检查链表头是否是 None 的引用即可
    添加元素：将新项作为链表的第一项，现有项将需要链接到这个新项后
    长度：遍历计数，知道head=None
    寻找： 若存在返回为真
    删除： 找到那个元素，删除该节点，并将它之前的项指向它之后的项
"""


class UnorderedList:
    def __init__(self):
        self.head = None

    def show(self):
        current = self.head
        data = ']'
        while current != None:
            temp = str(current.getData())
            data = temp + ',' + data
            current = current.getNext()
        data = '[' + data
        return data


    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        count = 1
        # 寻找该元素
        while not found and (count < self.size()):
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
            count += 1
        # 没找到则不存在返回False
        if count == self.size():
            return False
        # 若找到该元素，删除该节点,返回True
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return True


mylist = UnorderedList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
print(mylist.show())
x = mylist.remove(5)
print(x)
