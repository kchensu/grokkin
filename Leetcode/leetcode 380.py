
import random


class RandomizedSet(object):
    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, value):
        res = value not in self.numMap
        if res:
            # insert value with its index
            self.numMap[value] = len(self.numList)
            self.numList.append(value)
        return res

    def remove(self, value):
        res = value in self.numMap
        if res:
            index = self.numMap[value]
            lastValue = self.numList[-1]
            self.numList[index] = lastValue
            self.numList.pop()

            # update the hashmap
            self.numMap[lastValue] = index
            del self.numMap[value]
        return res

    def getRandom(self):
        return random.choice(self.numList) if len(self.numList) > 0 else []


obj = RandomizedSet()
# print(obj.getRandom())
print(obj.insert(1))
print(obj.remove(1))
# print(obj.insert(2))
# print(obj.getRandom())
# print(obj.remove(2))
# print(obj.insert(2))
# print(obj.getRandom())
