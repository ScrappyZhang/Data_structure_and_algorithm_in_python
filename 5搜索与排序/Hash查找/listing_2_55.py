"""

创建一个实现 Map 抽象数据类型的HashTable 类


- Map() 创建一个新的 map 。它返回一个空的 map 集合。
- put(key，val) 向 map 中添加一个新的键值对。如果键已经在 map 中，那么用新值替换旧值。
- get(key) 给定一个键，返回存储在 map 中的值或 None。
- del 使用 del map[key] 形式的语句从 map 中删除键值对。
- len() 返回存储在 map 中的键值对的数量。
- in 返回 True 对于 key in map 语句，如果给定的键在 map 中，否则为False。

"""
'''
@Time    : 2018/2/8 上午11:53
@Author  : scrappy_zhang
@File    : listing_2_55.py
'''


class HashTable:
    def __init__(self):
        self.size = 11  # 初始哈希表大小，建议为质数
        self.slots = [None] * self.size  # 保存键
        self.data = [None] * self.size  # 保存值

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            # 若哈希表中不存在该值，则将其添加到向阳村位置
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))  # 加1 rehash 函数的线性探测
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):
        # 哈希函数：简单除余法
        return key % size

    def rehash(self, oldhash, size):
        #  加1 rehash 函数的线性探测
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while (self.slots[position] != None) and (not found) and (not stop):
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    # HashTable类提供了附加的字典功能。
    # 重载__getitem__和__setitem__方法以允许使用[]访问。
    # 这意味着一旦创建了HashTable，索引操作符将可用。
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


if __name__ == '__main__':
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H.slots)
    print(H.data)
    H[20] = 'duck'
    print(H.data)
    print(H[77])