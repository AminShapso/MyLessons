dict_math_functions = {"add": lambda n1, n2: n1 + n2,
                       "mul": lambda n1, n2: n1 * n2,
                       "pow": lambda n1, n2: n1 ** n2,
                       "dev": lambda n1, n2: n1 / n2}


for i, (key, value) in enumerate(dict_math_functions.items()):
    print(f'item number {i + 1} is: {key} = {value}')
print()

a = 2
b = 4
for func in ["add", "mul", "pow", "dev"]:
    print(f'The {func} function off {a} and {b} is {dict_math_functions[func](a , b)}')
