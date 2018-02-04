"""
检查两个字符串是否为乱序字符串：检查

逐个字符依次对照检查

算法复杂度O（n^2）
"""
'''
@Time    : 2018/2/4 下午2:29
@Author  : scrappy_zhang
@File    : str01.py
'''


def anagramSolution1(s1, s2):
    # 先判断长度
    if (len(s1) != len(s2)):
        return False
    # 字符串为不可变类型，需要转换为列表，以便后续替换
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        # 将S2中每个元素与S1[pos1]相比较，若相同，则将found设为True
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        # 将S2中对应相同的第一个元素设为None
        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK


print(anagramSolution1('abcd', 'dcba'))
