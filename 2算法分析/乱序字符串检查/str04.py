"""
检查两个字符串是否为乱序字符串：技术和比较

利用两个乱序字符串具有相同数目的 a, b, c 等字符的事实。我们首先计算的是每个字母出现的次数。
由于有 26 个可能的字符，我们就用 一个长度为 26 的列表，每个可能的字符占一个位置。
每次看到一个特定的字符，就增加该位置的计数器。
最后如果两个列表的计数器一样，则字符串为乱序字符串


算法复杂度： T(n) = 2n+26
            0(n)


            但它需要额外的存储来保存两个字符计数列表.
"""
'''
@Time    : 2018/2/4 下午2:51
@Author  : scrappy_zhang
@File    : str04.py
'''


def anagramSolution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    # 统计字母出现次数，遍历N次(字符串长度)
    for i in range(len(s1)):
        # ord返回the Unicode
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK


print(anagramSolution4('apple', 'pleap'))
