"""
探索迷宫
"""

"""
四种基本情况：

1. 乌龟撞到了墙。由于这一格被墙壁占据，不能进行进一步的探索。
2. 乌龟找到一个已经探索过的格。我们不想继续从这个位置探索，否则会陷入循环。
3. 我们发现了一个外边缘，没有被墙壁占据。换句话说，我们发现了迷宫的一个出口。
4. 我们探索了一格在四个方向上都没有成功。


++++++++++++++++++++++
+000+000++0++00000+000
+0+000+0000000+++0+0++
+0+0+00++00++++000+0++
+++0++++++0000+++0+00+
+0000000000++00++0000+
+++++0++++++000+++++0+
+00000+000+++++++00+0+
+0+++++++000000S0+000+
+0000000000000000+0+++
++++++++++++++++++0+++

0代表空白区

"""

'''
@Time    : 2018/2/5 下午3:31
@Author  : scrappy_zhang
@File    : activecode_1_411.py
'''

import turtle

PART_OF_PATH = 'p'
TRIED = '.'
OBSTACLE = '+'  # 墙
DEAD_END = '-'


class Maze:
    def __init__(self, mazeFileName):
        rowsInMaze = 0  # 行数
        columnsInMaze = 0  # 列数
        self.mazelist = []  # 迷宫数据列表
        mazeFile = open(mazeFileName, 'r')  # 打开迷宫文件
        # rowsInMaze = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line.strip():
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze  # 起始行
                    self.startCol = col  # 起始列
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            # print(rowsInMaze)
            columnsInMaze = len(rowList)
            # print(columnsInMaze)
        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        # 坐标转换
        self.xTranslate = 0
        self.yTranslate = 0
        self.xTranslate = -columnsInMaze / 2
        self.yTranslate = rowsInMaze / 2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(columnsInMaze - 1) / 2 - .5, -(rowsInMaze - 1) / 2 + .5,
                                    (columnsInMaze - 1) / 2 - .5, (rowsInMaze - 1) / 2 + .5)  # 画布设置

    def drawMaze(self):
        """绘制地图"""
        self.t.speed(10)
        self.wn.tracer(0)
        # print(self.rowsInMaze,self.columnsInMaze)
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenteredBox(x + self.xTranslate, -y + self.yTranslate, 'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)

    def drawCenteredBox(self, x, y, color):
        """+号绘制墙"""
        self.t.up()
        self.t.goto(x - .5, y - .5)  # 从方框左下角开始画
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)  # 边长为1
            self.t.right(90)
        self.t.end_fill()

    def moveTurtle(self, x, y):
        # 位置移动
        self.t.up()
        self.t.setheading(self.t.towards(x + self.xTranslate, -y + self.yTranslate))
        self.t.goto(x + self.xTranslate, -y + self.yTranslate)

    def dropBreadcrumb(self, color):
        self.t.dot(10, color)

    def updatePosition(self, row, col, val=None):
        """更新和标记乌龟位置"""
        if val:
            self.mazelist[row][col] = val
        self.moveTurtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)

    def isExit(self, row, col):
        # 判断是否到达边界，即出口
        return (row == 0 or
                row == self.rowsInMaze - 1 or
                col == 0 or
                col == self.columnsInMaze - 1)

    def __getitem__(self, idx):
        return self.mazelist[idx]


def searchFrom(maze, startRow, startColumn):
    # try each of four directions from this point until we find a way out.
    # base Case return values:
    #  1. 如果是墙则返回False
    maze.updatePosition(startRow, startColumn)
    if maze[startRow][startColumn] == OBSTACLE:
        return False
    # 2. 如果走过该单元或者尽头，则返回False
    if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn] == DEAD_END:
        return False
    # 3. 如果到达边界，即出口，则返回True
    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, TRIED)
    # Otherwise, use logical short circuiting to try each direction
    # in turn (if needed) 东西南北分别尝试， 注意or
    found = searchFrom(maze, startRow - 1, startColumn) or \
            searchFrom(maze, startRow + 1, startColumn) or \
            searchFrom(maze, startRow, startColumn - 1) or \
            searchFrom(maze, startRow, startColumn + 1)
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found


myMaze = Maze('maze2.txt')
myMaze.drawMaze()
myMaze.updatePosition(myMaze.startRow, myMaze.startCol)

searchFrom(myMaze, myMaze.startRow, myMaze.startCol)
for i in myMaze.mazelist:
    print(''.join(i))
