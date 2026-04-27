a = 1

# for each in a:
#    print(each)

# print(dir(a))


class MyCounter:
    def __init__(self, end):
        self.current = 0
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1


c = MyCounter(4)
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())

b = []

# only for understanding what a for loop does internally
# tmp = c.__iter__(c)
# each = tmp.__next__()

for each in c:
    for another in c:
        print(another)
    # b.insert(each)
