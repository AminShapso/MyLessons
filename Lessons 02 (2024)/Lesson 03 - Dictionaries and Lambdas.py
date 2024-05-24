import pandas as pd


def addition(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def power(n1, n2):
    return n1 ** n2


def division(n1, n2):
    return n1 / n2


def olala(n1):
    return str(n1) + '-olala'


dict_math_functions = {"add": lambda n1, n2: n1 + n2,
                       "mul": lambda n1, n2: n1 * n2,
                       "pow": lambda n1, n2: n1 ** n2,
                       "div": lambda n1, n2: n1 / n2}

a = 2
b = 4
df = pd.DataFrame({'column A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'column B': [0, 0, 2, 2, 0, 0, 4, 4, 0, 0]})

for key in ["add", "mul", "pow", "div"]:
    print(f'The {key} function of {a} and {b} is {dict_math_functions[key](a, b)}')
print()
print(f'The addition of {a} and {b} is {addition(a, b)}')
print(f'The multiply of {a} and {b} is {multiply(a, b)}')
print(f'The power of {a} and {b} is {power(a, b)}')
print(f'The division of {a} and {b} is {division(a, b)}')
print()

print(df)
print(f'new df is {df.map(olala)}')
print(f'new df is {df.map(lambda s: str(s) + '-olala')}')
for key in ["add", "mul", "pow", "div"]:
    print(f'The {key} function of the df is {df.map(lambda n: dict_math_functions[key](n, 2))}')
