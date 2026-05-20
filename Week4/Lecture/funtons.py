def insert_db(*args, **kwargs):
    print(type(args))
    print(args)
    print("insert called")

    # if 1 == "1":
    #    print("true")
    # else:
    #   print("false")

    return b()


def b():
    return c()
    print("b completed")


def c():
    print("c completed")
    return "c"


# print(insert_db(999,a=1, b=2, c=3, d=4))
z = 1


def a():
    global z
    z = 2
    print(z)


# z = 3
# a()
# print(z

# Rule 1: object should be assignable to a variable
a = 1


def func1():
    print("func1")
    return 1


z = func1
# z()


# Rule 2: object should be passable into functions
def some(param):
    print(param())


# some(z)

# some(1)


# Rule 3: object should be returnable from a fucntion:
def some1():
    z = 1

    def another_function():
        print("another")
        nonlocal z

    return another_function


result = some1()
print(type(result))
print(result.__name__)


# 1()
#
def my_timer(func):

    def return_function(*args, **kwargs):
        print("return of decorator")
        # time  =
        func(*args, **kwargs)
        # time =

    return return_function
    # return 1


# @clean_commas
# @remove_special_char
@my_timer
def my_func(param):
    print(param)
    print("my func called")


@my_timer
def insert_db(param1, param2, param):
    print("insert db called")


# my_func(1)
# insert_db(1, 2, 3)
# result = my_decorator(my_func)
# result()
#
#
#
values = [1, 2, 3, 4]
new_values = []
for eachvalue in values:
    new_values.append(eachvalue**2)

print(new_values)


def square_numbers(value):
    return value**2


new_values = list(map(square_numbers, values))
print(new_values)

new_values_1 = list(map(lambda x: x**2, values))
print(new_values_1)

g = lambda f, g: f**2

a = [x for x in range(1_000_000) if x % 2 == 0]
