# pip install uint
from uint import Uint, Int
number_of_bytes = 4

# for i, (a, b) in enumerate(zip([1, '1', '1', '1', '1'], [1, '1', '1', '1', '1'])):
#     try:
#         ans = None
#         match i:
#             case 0:
#                 ans = a + b
#             case 1:
#                 ans = a + b
#             case 2:
#                 ans = int(a) + int(b)
#             case 3:
#                 ans = int(a + b)
#             case 4:
#                 ans = int(a - b)
#         print(f'{a = }     {b = }     {ans = }')
#     except TypeError:
#         print("ERROR YA EBNI, 'str' minus 'str' is not possible")


a = Int(2147483647, number_of_bytes * 8)
b = Uint(4294967295, number_of_bytes * 8)
print(f'{a = }')
print(f'{b = }')
a += 1
b += 1
print(f'(a += 1) = {a}')
print(f'(b += 1) = {b}')


#             UINT4
# 8   4   2   1  D4  D3  D2  D1  ANS
# 0   0   0   0   0   0   0   0   0
# 0   0   0   1   0   0   0   1   1
# 0   0   1   0   0   0   2   0   2
# 0   0   1   1   0   0   2   1   3
# 0   1   0   0   0   4   0   0   4
# 0   1   0   1   0   4   0   1   5
# 0   1   1   0   0   4   2   0   6
# 0   1   1   1   0   4   2   1   7
# 1   0   0   0   8   0   0   0   8
# 1   0   0   1   8   0   0   1   9
# 1   0   1   0   8   0   2   0   10
# 1   0   1   1   8   0   2   1   11
# 1   1   0   0   8   4   0   0   12
# 1   1   0   1   8   4   0   1   13
# 1   1   1   0   8   4   2   0   14
# 1   1   1   1   8   4   2   1   15
#
#
#
#               INT4
# -8  4   2   1   D4  D3  D2  D1  ANS
# 0   0   0   0   0   0   0   0   0
# 0   0   0   1   0   0   0   1   1
# 0   0   1   0   0   0   2   0   2
# 0   0   1   1   0   0   2   1   3
# 0   1   0   0   0   4   0   0   4
# 0   1   0   1   0   4   0   1   5
# 0   1   1   0   0   4   2   0   6
# 0   1   1   1   0   4   2   1   7
# 1   0   0   0   8   0   0   0   -8
# 1   0   0   1   8   0   0   1   -7
# 1   0   1   0   8   0   2   0   -6
# 1   0   1   1   8   0   2   1   -5
# 1   1   0   0   8   4   0   0   -4
# 1   1   0   1   8   4   0   1   -3
# 1   1   1   0   8   4   2   0   -2
# 1   1   1   1   8   4   2   1   -1