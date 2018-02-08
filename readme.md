这里是对来自http://interactivepython.org/runestone/static/pythonds/index.html

系列文章的源代码整理。《Problem Solving with Algorithms and Data Structures using Python》



笔者在该网站阅读学习这一书籍时，重新整理了相应的代码，每个文件均可单独运行。

例如：

在2.4节的乱序字符串检查，原作者的第一段代码没有首先进行字符串长度判断；

在3.6节中的检查，纯粹为括号匹配，若有数字则不能判断，添加了此功能；

在3.9节公式匹配中优化了代码功能；

等等。



以下为代码功能说明：

## [2算法分析](./2算法分析/)

##### 乱序字符串检查

- str01.py 逐个字符依次对照检查
- str02.py 先将两个字符进行排序，然后对比是否相等
- str03.py 穷举法说明

##### 列表

- list0_n.py 对比append和拼接（+）的复杂度：append的复杂度为O(1),拼接的复杂度为O(k)
- listing4.py 对比pop(0)和pop(0)的复杂度：pop(0) 是 O(n), pop()是 O(1)

##### 字典

- listing.py 对比字典和列表的contains方法复杂度：列表O(n)，字典O(1)

## [3基本数据结构](./3基本数据结构/)

##### 列表

- listing_321.py 实现无序列表：1、在每个项中保持一些明确的信息，即下一个项的位置；2、最后一项需要知道自己是最后的一个；3、第一个位置必须被明确,新项的位置。
- listing_323.py 实现有序列表：升序排列的列表，第一个元素最小

##### 双端队列

- listing1_317.py python列表实现Deque双端队列
- active_code_1_318.py 采用双端队列来判断一个字符串是否为回文：（回文：左右对称：如radar toot madam）

##### 栈

- active_code_1_35.py python列表实现栈
- active_code_1_36.py 栈实现简单的括号数量成对匹配
- active_code_1_37.py 栈实现更精准的有效括号成对匹配
- active_code_1_38.py 堆栈实现十进制转二进制
- active_code_1_39.py 运算公式由中缀转换为后缀：
  初始公式： A*B+C*D-9
  后缀公式： A B * C D * + 9 -
  初始公式： (A+par)*C-(D-E)*(F+G)
  后缀公式： A par + C * D E - F G + * -
- active_code_2_38.py 堆栈实现十进制转二进制、十六进制、八进制等
- active_code_2_39.py 运算公式由中缀转换为后缀,并计算
  初始公式： (72+8)/(3+2)
  后缀公式： 72 8 + 3 2 + /
  运算结果为： 16.0

##### 队列

- listing1_312.py python列表实现队列（队首在列表末端、队尾为列表首段）
- actvie_code_1_313.py 通过队列识别烫手山芋游戏最后一个存活的玩家
- printer_314.py 打印机等待时间案例 

## [递归](./4递归/)

##### 整数列表和

- actvie_code_1_43.py 通过for循环计算列表和
- actvie_code_2_43.py 通过递归实现计算列表和

##### 进制转换

- actvie_code_1_45.py 递归实现任意进制转换
- actvie_code_1_46.py 堆栈实现进制转换

##### 可视化递归

- actvie_code_1_47.py turtle 模块：递归绘制螺旋图
- actvie_code_2_47.py turtle 模块：递归绘制树

##### 谢尔宾斯基三角形

- actvie_code_1_48.py turtle 模块：递归绘制谢尔宾斯基三角形

##### 汉诺塔游戏

- actvie_code_1_410.py 汉诺塔游戏

##### 探索迷宫

- actvie_code_1_411.py 迷宫游戏
- maze2.txt 迷宫地图文件

##### 动态规划

- actvie_code_1_412.py 自动售货机硬币找零：递归加记忆实现
- actvie_code_3_412.py 自动售货机硬币找零：贪婪法
- actvie_code_2_412.py 自动售货机硬币找零：动态规划

## [5搜索与排序](./5搜索与排序/)











