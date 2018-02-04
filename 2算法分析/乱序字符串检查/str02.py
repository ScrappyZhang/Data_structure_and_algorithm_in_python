"""
检查两个字符串是否为乱序字符串：排序和比较

先将两个字符进行排序，然后对比是否相等

算法复杂度：

首先你可能认为这个算法是 O(n)，因为只有一个简单的迭代来比较排序后的 n 个字符。但是，调用 Python 排序不是没有成本。
正如我们将在后面的章节中看到的，排序通常是 O(n^2) 或 O(nlogn)。所以排序操作比迭代花费更多。最后该算法跟排序过程有同样的量级。
"""
'''
@Time    : 2018/2/4 下午2:44
@Author  : scrappy_zhang
@File    : str02.py
'''

def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagramSolution2('abcde','edcba'))