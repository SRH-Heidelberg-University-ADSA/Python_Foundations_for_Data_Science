class StackOverflow:
    def __init__(self, feature1, feature2):
        self.feature1 = feature1
        self.fearure2 = feature2

    def change_feature1(self, new_value):
        if new_value > 0:
            self.feature1 = feature1
        else:
            print("not possible")


u1 = StackOverflow(23, 45)
u2 = StackOverflow(34, 56)

print(u1.feature1)
print(u2.feature1)

u1.change_feature1(-1000)

# u1.feature1 = -10000
print(u1.feature1)

print(type(u1))

a = "1"
print(dir(a))
