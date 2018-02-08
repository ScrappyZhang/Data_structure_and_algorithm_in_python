"""贪婪法"""
'''
@Time    : 2018/2/5 下午11:22
@Author  : scrappy_zhang
@File    : activecode_3_412.py
'''
usedcoin = []


def find_coin(coinValueList, change):
    if len(coinValueList) == 1:
        usedcoin.append(coinValueList[0])
        return change
    if change > max(coinValueList):
        temp = change % max(coinValueList)
        coinValueList.remove(max(coinValueList))
        usedcoin.append(max(coinValueList))
        coins = change // max(coinValueList) + find_coin(coinValueList, temp)
    else:
        coinValueList.remove(max(coinValueList))
        coins = find_coin(coinValueList, change)
    return coins


print(find_coin([1, 5, 10, 21, 25], 63))
print(usedcoin)
