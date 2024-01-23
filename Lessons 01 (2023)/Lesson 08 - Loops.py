import numpy as np

test_number = 5
list_nums = [1, 2, 3, 4, 5]
stum_string = "stum string"
range_nums = range(1, 6)
range_floats = np.arange(1, 4, 0.5)


match test_number:
    case 0:
        for c in stum_string:
            print(f"{c = }")

    case 1:
        for i_num, num in enumerate(list_nums):
            print(f"{i_num = }")
            print(f"{num = }")

    case 2:
        length = len(stum_string)
        print(f"{length = }")
        stum_loop = range(length)

        for i in range(len(stum_string)):
            print(f"{i = }")
            print(f"{stum_string[i] = }")

    case 3:
        i = 0
        while i < len(stum_string):
            print(f"{i = }")
            print(f"{stum_string[i] = }")
            i += 1

    case 4:
        i = 0
        babol = True
        while babol:
            i -= 1
            if i < -10:
                babol = False
            print(f"{i = }")

    case 5:
        break_point_a = 5
        continue_point_a = 5
        break_point_b = ""
        continue_point_b = "E"
        for i in [1, 2, 3]:
            if i == break_point_a:
                break
            elif i == continue_point_a:
                continue
            for j in "ACEG":
                if j == break_point_b:
                    break
                elif j == continue_point_b:
                    continue
                print(f"{i = }   +   {j = }")
            print("loop is finished")

        print()

        break_point_a = 5
        continue_point_a = 2
        break_point_b = ""
        continue_point_b = ""
        for i in [1, 2, 3]:
            if i == break_point_a:
                break
            elif i == continue_point_a:
                continue
            for j in "ACEG":
                if j == break_point_b:
                    break
                elif j == continue_point_b:
                    continue
                print(f"{i = }   +   {j = }")
            print("loop is finished")

    case 6:
        for i, (a, b) in enumerate(zip(list_nums, stum_string)):
            print(f"{i = } {a = } {b = }")

    case _:   # default
        print(f"{test_number = } is not found")
