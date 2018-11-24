class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.val = 0
    def can_add(self, v):
        y = self.val +v
        return y <= self.capacity
    def add(self, v):
        if MoneyBox.can_add(self, v):
            self.val += v

x = MoneyBox(5)
x.add(2)
x.add(3)
x.add(1)