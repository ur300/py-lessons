import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def __init__(self):
        self.lst = []

    def append(self, msg):
        self.log(msg)
        list.append(self, msg)

lst1 = LoggableList()
lst1.append('dasdas')
lst1.append('d111222')
print(lst1)