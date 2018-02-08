"""基于字符的项（如字符串）创建哈希函数"""


"""
**********************
哈希函数必须是高效的
**********************
"""

'''
@Time    : 2018/2/8 上午10:53
@Author  : scrappy_zhang
@File    : listing_1_55.py
'''


def hash(astring, tablesize):
    # 纯粹的ascii值相加
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])

    return sum % tablesize


def hash_weight(astring, tablesize):
    # 增加位置权值
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos]) * (pos + 1)

    return sum % tablesize


if __name__ == '__main__':
    str1 = 'zhang'
    str2 = 'angzh'
    print(hash(str1, 11))
    print(hash(str2, 11))
    print(hash_weight(str1, 11))
    print(hash_weight(str2, 11))
