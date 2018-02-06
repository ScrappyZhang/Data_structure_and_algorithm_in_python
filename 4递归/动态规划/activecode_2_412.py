"""自动售货机硬币找零"""
'''
@Time    : 2018/2/5 下午11:13
@Author  : scrappy_zhang
@File    : activecode_2_412.py
'''

def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
    # :param coinValueList: 硬币列表
    # :param change: 要找零的总数
    # :param minCoins: 最小的硬币数
    # :param coinsUsed: 用过的硬币
    # :return: 返回硬币数

   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()