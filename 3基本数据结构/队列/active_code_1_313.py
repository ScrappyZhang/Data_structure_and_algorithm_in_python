"""
烫手山芋

游戏规则：一群人围城一圈，指定一个数字，当数到这个数时所讲数的人出局，然后游戏继续，
        直到最后一人
"""
'''
@Time    : 2018/2/4 下午4:17
@Author  : scrappy_zhang
@File    : active_code_1_313.py
'''


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


def hot_potato(namelist, num):
    """
    :param namelist:  游戏玩家
    :param num: 游戏指定数
    :return: 返回最后一个玩家
    """
    sim_queue = Queue()
    # 将所有玩家添加进队列Queue作为游戏初始玩家顺序
    for name in namelist:
        sim_queue.enqueue(name)
    # 只要人数大于1，则游戏不结束
    while sim_queue.size() > 1:
        # 将一轮游戏的玩家按先数先进的原则写入
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
            # print(sim_queue.items) # 可以查看游戏过程
        # 把每一轮最后一个玩家删除
        sim_queue.dequeue()

    return sim_queue.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
