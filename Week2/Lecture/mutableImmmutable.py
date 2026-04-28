a = 1
# print(id(a))
b = 1
# print(id(b))
a = 2

s = "hello"
print(f"before s = {id(s)} ")
s = s + " world"
print(f"after s = {id(s)}")

try:
    s[0] = "n"
except TypeError as e:
    print(f"error is : {e}")

ls = [1, 2, 3]
print(f"before ls = {id(ls)}")
ls[0] = 4
print(ls)
print(f" after ls = {id(ls)}")
