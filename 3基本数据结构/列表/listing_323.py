"""
python实现有序链表

元素由升序或降序排列的链表

"""
'''
@Time    : 2018/2/4 下午6:42
@Author  : scrappy_zhang
@File    : listing_323.py
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
OrderedList 类   有序列表   下标越小，值越小

1.必须保持对第一个节点的引用  head

2.链表的各种操作

    空操作：检查链表头是否是 None 的引用即可
    添加元素：将新项作为链表的第一项，现有项将需要链接到这个新项后
    长度：遍历计数，知道head=None
    寻找： 若存在返回为真
    删除： 找到那个元素，删除该节点，并将它之前的项指向它之后的项
"""


class OrderedList:
    def __init__(self):
        self.head = None

    def show(self):
        current = self.head
        data = '['
        while current != None:
            temp = str(current.getData())
            data = data + temp + ','
            current = current.getNext()
        data = data + ']'
        return data


    def isEmpty(self):
        return self.head == None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

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
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
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


mylist = OrderedList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(11)
print(mylist.show())
x = mylist.remove(5)
print(x)