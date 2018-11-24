class Buffer:
    def __init__(self):
        self.part_size = 5
        self.part = []

    def add(self, *a):
        self.part.extend(list(a))
        while len(self.part) >= self.part_size:
            new_part = self.part[0:self.part_size]
            self.part = self.part[self.part_size:]
            print(sum(new_part))

    def get_current_part(self):
            print(self.part)

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15)
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40)
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) –
buf.get_current_part() # вернуть [1]