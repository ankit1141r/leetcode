class RandomizedSet:

    def __init__(self):
        self.lst=[]
        self.map={}

    def insert(self, val: int) -> bool:
        if val in self.lst:
            return False 
        self.lst.append(val)
        self.map[val]=len(self.lst)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        idx=self.map[val]
        last_val=self.lst[-1]
        self.lst[idx]=last_val
        self.map[last_val]=idx
        self.lst.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()