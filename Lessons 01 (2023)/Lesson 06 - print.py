a = 100
b = 2.2
c = a * b
d = a + b
e = 1 / 1

# different type of prints:
print('Results:')
print()
print('a = ' + str(a))
print('b =', b, sep=' ')
print(f'c = {c}')
d = str(d)
print('d = ' + d)
print(f'{e = }')

# different type of formating:
print()
print(f'1.115111 = {1.115111}')
print(f'int(1.115111) = {int(1.115111)}')
print(f'1.115111:.2f = {1.115111:.2f}')
print(f'1.115111:.3f = {1.115111:.3f}')
print(f'1:03d = {1:03d}')
