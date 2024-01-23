from multipledispatch import dispatch


def my_range_1(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    my_list = []
    while start < stop:
        my_list.append(start)
        start += step
    return my_list


@dispatch(int)
def my_range_2(stop):
    print(f"my_range_2_a: {stop=}")
    return my_range_2(0, stop)


@dispatch(int, int)
def my_range_2(start, stop):
    print(f"my_range_2_b: {start=}, {stop=}")
    return my_range_2(start, stop, 1)


@dispatch(int, int, int)
def my_range_2(start, stop, step):
    print(f"my_range_2_c: {start=}, {stop=}, {step=}")
    my_list = []
    if step <= 0:
        return my_list
    if start > stop:
        return my_list
    while start < stop:
        my_list.append(start)
        start += step
    return my_list


all_data = []
all_data.append(range(6))
all_data.append(range(1, 6))
all_data.append(range(1, 6, 2))
all_data.append(my_range_1(6))
all_data.append(my_range_1(1, 6))
all_data.append(my_range_1(1, 6, 2))
all_data.append(my_range_2(6))
all_data.append(my_range_2(1, 6))
all_data.append(my_range_2(1, 6, 2))
print()

for data in all_data:
    print(data)
    print(", ".join([str(d) for d in data]))
    print()
