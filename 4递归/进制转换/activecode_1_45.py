"""
递归实现进制转换


整个算法将分成三个部分：

1. 将原始数字减少为一系列单个位数字。
2. 使用查找将单个位数字数字转换为字符串。
3. 将单个位字符串连接在一起以形成最终结果。


"""
'''
@Time    : 2018/2/5 下午2:35
@Author  : scrappy_zhang
@File    : activecode_1_45.py
'''


def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]  # 注意字符串方向


print(toStr(1453, 8))
