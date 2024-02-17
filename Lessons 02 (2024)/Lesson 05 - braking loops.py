def next_square():
    i = 1
    # An Infinite loop to generate squares
    while True:
        yield i * i
        i += 1  # Next execution resumes from this point


for num in next_square():
    if num > 50:
        break
    print(num)


def my_loop_yield(my_list, min_rating):
    i_iter = 0
    for k, v in my_list.items():
        i_iter += 1
        print(f'{i_iter = }')
        if v >= min_rating:
            yield k

def my_loop_return(my_list, min_rating):
    i_iter = 0
    out = []
    for k, v in my_list.items():
        i_iter += 1
        print(f'{i_iter = }')
        if v >= min_rating:
            out.append(k)
        if len(out) == 3:
            return out


list_of_players = {"Amin": 7, "Gogo": 7, "Cheata": 6, "Adam": 6, "Asa": 5, "Nan": 4, "Tat": 5, "Aiden": 4, "Fluffy": 4, "Shimi": 5, "Chichi": 10, "Pikachu": 0,
                   "Meow": 5, "Tataz": 5, "Tarazan": 3, "King kong": 9, "Nasralla": 0, "Beebee": 0}
print()
print('my_loop_yield = ')
print(list(my_loop_yield(list_of_players, 6)))
print()
print('my_loop_return = ')
print(list(my_loop_return(list_of_players, 6)))
print()

for index, player in enumerate(my_loop_yield(list_of_players, 6)):
    print(f'player number {index + 1} = {player}')
    if index == 2:
        break
