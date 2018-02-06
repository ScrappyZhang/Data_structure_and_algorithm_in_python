"""自动售货机硬币找零"""
'''
@Time    : 2018/2/5 下午11:00
@Author  : scrappy_zhang
@File    : activecode_1_412.py
'''


def recMC(coinValueList,change):
   #  递归
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins


# print(recMC([1,5,10,25],63))

def recDC(coinValueList,change,knownResults):
   #  递归加记忆
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   return minCoins

# print(recDC([1,5,10,25],63,[0]*64))


