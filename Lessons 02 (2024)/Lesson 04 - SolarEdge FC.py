import math
import random
import statistics
from itertools import combinations


list_of_players = {"Amin": 7, "Gogo": 7, "Cheata": 6, "Adam": 6, "Asa": 5, "Nan": 4, "Tat": 5, "Aiden": 4, "Fluffy": 4}


# iteration_counter = 756756
# time = 01:27:80.0000
# yield
# min_sum_ratio = (0.0, 0.4344039811047981)
# min_sd_ratio = (4.358898943540674, 0.2696100478085411)
# min_ratio = (0.0, 0.4344039811047981)
# 84 * 20 * 1 = 1680 / 3 = 560
# check SD

class Player:
    min_rating = 0
    max_rating = 10

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.played_with = {}
        self.played_against = {}
        self.performance = 0

    def new_game(self, played_with, played_against, performance):
        self.played_with.update(played_with)
        self.played_against.update(played_against)
        self.performance += performance

    def calculate_new_rating(self, performance_weight):
        temp_rating = self.rating + (self.performance * performance_weight)
        if temp_rating > self.max_rating:
            self.rating = self.max_rating
        elif temp_rating < self.min_rating:
            self.rating = self.min_rating
        else:
            self.rating = temp_rating

    def get_player(self):
        return self.name, self.rating


def group_distribution(total_players):
    if total_players % 3 == 0:
        return [total_players // 3] * 3
    elif total_players % 3 == 1:
        return [total_players // 3 + 1] + [total_players // 3] * 2
    else:
        return [total_players // 3 + 1] * 2 + [total_players // 3]


def find_close_sum_groups(players, group_sizes, sum_pass, sd_pass):
    print(f'\nfind_close_sum_groups({len(players) = }, {group_sizes = }, {sum_pass = }, {sd_pass = })')
    print(f'Number of possible combinations = {math.comb(sum(group_sizes), group_sizes[0]) * math.comb(sum(group_sizes[:2]), group_sizes[1]) * math.comb(group_sizes[1], group_sizes[2])}')
    players = [player.get_player() for player in players]
    random.shuffle(players)
    all_combinations = list(combinations(players, group_sizes[0]))

    iteration_counter = 0
    min_sum_ratio = (2**63-1, 0)
    min_sd_ratio = (0, 2**63-1)
    min_ratio = (2**63-1, 2**63-1)
    for group_1 in all_combinations:
        # print(f'{iteration_counter = }')
        remaining_players_1 = [player for player in players if player not in group_1]
        for group_2 in combinations(remaining_players_1, group_sizes[1]):
            remaining_players_2 = [player for player in remaining_players_1 if player not in group_2]
            for group_3 in combinations(remaining_players_2, group_sizes[2]):
                iteration_counter += 1

                group_1 = dict(group_1)
                group_2 = dict(group_2)
                group_3 = dict(group_3)
                if len(group_3) < len(group_2):
                    group_3.update({"MANA": max(*group_1.values(), *group_2.values())})
                elif len(group_1) > len(group_2):
                    group_2.update({"MANA": max(*group_1.values(), *group_3.values())})
                    group_3.update({"MANA": max(*group_1.values(), *group_2.values())})

                sum_1 = sum(group_1.values())
                sum_2 = sum(group_2.values())
                sum_3 = sum(group_3.values())
                avg_1 = statistics.mean(group_1.values())
                avg_2 = statistics.mean(group_2.values())
                avg_3 = statistics.mean(group_3.values())
                sd_1 = statistics.stdev(group_1.values())
                sd_2 = statistics.stdev(group_2.values())
                sd_3 = statistics.stdev(group_3.values())

                sum_ratio = statistics.stdev([sum_1, sum_2, sum_3])
                sd_ratio = statistics.stdev([sd_1, sd_2, sd_3])
                ratio = (sum_ratio + sd_ratio) / 2
                if sum_ratio < min_sum_ratio[0]:
                    min_sum_ratio = (sum_ratio, sd_ratio)
                if sd_ratio < min_sd_ratio[1]:
                    min_sd_ratio = (sum_ratio, sd_ratio)
                if ratio < statistics.mean(min_ratio):
                    min_ratio = (sum_ratio, sd_ratio)

                if sum_ratio <= sum_pass and sd_ratio <= sd_pass:
                    group_1 = dict(sorted(group_1.items()))
                    group_2 = dict(sorted(group_2.items()))
                    group_3 = dict(sorted(group_3.items()))
                    print(f'{iteration_counter = }')
                    print(f'{min_sum_ratio = }')
                    print(f'{min_sd_ratio = }')
                    print(f'{min_ratio = }\n')
                    return [(group_1, sum_1, avg_1, sd_1), (group_2, sum_2, avg_2, sd_2), (group_3, sum_3, avg_3, sd_3)]
    print(f'{iteration_counter = }')
    print(f'{min_sum_ratio = }')
    print(f'{min_sd_ratio = }')
    print(f'{min_ratio = }\n')
    return None     # If no close sum groups are found, return None


players_class = [Player(name, score) for name, score in list_of_players.items()]
group_sizes = group_distribution(len(players_class))
sum_pass = 0
# sum_pass = 0.2
# sd_pass = 0.5
sd_pass = 0.3
result = find_close_sum_groups(players_class, group_sizes, sum_pass, sd_pass)
if result:
    for g_index, group in enumerate(result):
        print(f'Group {g_index + 1} (Sum = {group[1]}, Avg = {group[2]:.1f}, SD = {group[3]:.1f}) =\n{group[0]}\n'.replace(", '", "\n").replace("{", '').replace('}', '').replace("'", ''))
else:
    print("Close sum groups not found.")
