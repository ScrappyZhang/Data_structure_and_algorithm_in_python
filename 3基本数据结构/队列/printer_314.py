"""
打印机等待时间案例


为了为这种情况建模，我们需要使用一些概率。例如，学生可以打印长度从 1 到 20 页的纸张。
如果从 1 到 20 的每个长度有同样的可能性，则可以通过使用 1 和 20 之间的随机数来模拟打印任务的实际长度。
这意味着出现从 1 到 20 的任何长度的机会是平等的。

如果实验室中有 10 个学生，每人打印两次，则平均每小时有 20 个打印任务。
在任何给定的秒，打印任务将被创建的机会是什么？ 回答这个问题的方法是考虑任务与时间的比率。
每小时 20 个任务意味着平均每 180 秒将有一个任务


1. 创建打印任务的队列，每个任务都有个时间戳。队列启动的时候为空。
2. 每秒（currentSecond）：
   - 是否创建新的打印任务？如果是，将 currentSecond 作为时间戳添加到队列。
   - 如果打印机不忙并且有任务在等待
     - 从打印机队列中删除一个任务并将其分配给打印机
     - 从 currentSecond 中减去时间戳，以计算该任务的等待时间。
     - 将该任务的等待时间附件到列表中稍后处理。
     - 根据打印任务的页数，确定需要多少时间。
   - 打印机需要一秒打印，所以得从该任务的所需的等待时间减去一秒。
   - 如果任务已经完成，换句话说，所需的时间已经达到零，打印机空闲。
3. 模拟完成后，从生成的等待时间列表中计算平均等待时间。

"""
'''
@Time    : 2018/2/4 下午4:44
@Author  : scrappy_zhang
@File    : printer_314.py
'''
import random


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


class Printer:
    """
    打印机类：初始化、tick内部定时器递减到打印机空闲、
            busy 繁忙
            startNext 下一个任务开始
    """

    def __init__(self, ppm):
        self.pagerate = ppm  # 打印速度
        self.currentTask = None  # 当前任务
        self.timeRemaining = 0  # 当前任务剩余时间

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate  # 下一个任务打印需要时间


class Task:
    """
    创建任务
    表示单个打印任务。创建任务时，随机数生成器将提供 1 到 20 页的长度
    """

    def __init__(self, time):
        self.timestamp = time  # 时间戳
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):  # 等待时间
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):
    """

    :param numSeconds: 模拟的时间长度，单位为秒
    :param pagesPerMinute: 打印速度ppm
    :return:
    """
    labprinter = Printer(pagesPerMinute)  # 创建实验室打印机对象
    printQueue = Queue()  # 创建打印队列
    waitingtimes = [] # 统计等待时间列表

    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task) # 任务添加进打印队列

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue() # 删除可以打印的任务
            waitingtimes.append(nexttask.waitTime(currentSecond))  # 统计等待时间
            labprinter.startNext(nexttask) # 打印机开始打印

        labprinter.tick()
    # 平均等待时间
    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))


def newPrintTask():
    # 创建新任务，当数字为180时，则为新任务
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

# 每分钟五页的页面速率运行模拟 60 分钟
for i in range(10):
    simulation(3600, 5)
