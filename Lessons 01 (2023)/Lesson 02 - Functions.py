def add_one(a, x=0, y=0):
    a = a + 1
    print(f"a: {a = }")
    print(f"x: {x = }")
    return a


def add_ones(b):
    for n in b:
        print(f"b: {n = }")
    for i in range(len(b)):
        b[i] += 1
    # for n in b:
    #     n += 1
    for n in b:
        print(f"b: {n = }")
    for n in y:
        print(f"y: {n = }")
    return b


def change_string(c):
    c = "yosi"
    for n in c:
        print(f"c: {n = }")
    for n in z:
        print(f"z: {n = }")
    return c


x = 5   # variable?
y = [1, 2, 3]   # this is an object
z = "123"   # this is an object

add_one(x)
print()
add_ones(y)
print()
change_string(z)
print()
