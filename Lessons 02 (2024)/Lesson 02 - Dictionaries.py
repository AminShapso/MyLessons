dict_output_messages = {"error": "You have an error",
                        "a": "The winner is player number 1",
                        "b": "The winner is player number 2",
                        "tie": "The game is a tie between player number 1 and 2"}


for i, (key, value) in enumerate(dict_output_messages.items()):
    print(f'item number {i + 1} is: {key} = {value}')
print()


for a, b in zip([5, 10, 7, "mana"], [8, 8, 7, 0]):
    if not (type(a) == int or type(a) == float) or not (type(b) == int or type(b) == float):
        print(dict_output_messages["error"])
    elif a > b:
        print(dict_output_messages["a"])
    elif a < b:
        print(dict_output_messages["b"])
    else:
        print(dict_output_messages["tie"])


dict_random = {True: False,
               "": "Hello my name is Igor",
               0: 123,
               (1, 2): [1, 2, 3],
               # []: [1, 2, 3],   # list is unhashable
               None: None}
print()
for i, (key, value) in enumerate(dict_random.items()):
    print(f'item number {i + 1} is: {key} = {value}')
print()
