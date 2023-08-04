final_scores = [116, 124, 115, 102, 111, 106]
print(len(final_scores))

def count_matches(final_scores):
    print('A Lakers 6 meccset játszott le a fináléban.')

count_matches(final_scores)

first_quarter = [2, 2, 2, 1, 1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1]


def count_points(first_quarter):
    print(first_quarter.count(1))
    print(first_quarter.count(2))
    print(first_quarter.count(3))   

count_points(first_quarter)

def print_number_of_three_pointers(first_quarter):
    print(first_quarter.count(3))

print_number_of_three_pointers(first_quarter)

print('A(z) első negyedben 1 darab hárompontos dobás volt.')


def get_min_score(final_scores):
    print(min(final_scores))

get_min_score(final_scores)

def get_max_score(final_scores):
    print(max(final_scores))

get_max_score(final_scores)

def print_final_stat(final_scores):
    print('A fináléban játszott mérkőzések közül a legalacsonyabb pontszámú meccs eredménye: 102.')
    print('A fináléban játszott mérkőzések közül a legmagasabb pontszámú meccs eredménye: 124.')

print_final_stat(final_scores)


def get_game_number(final_scores):
    print(final_scores.index(102))
    print(final_scores.index(124))

get_game_number(final_scores)

print('A fináléban játszott mérkőzések közül a legalacsonyabb pontszámú a 4. meccs volt 102 ponttal.')
print('A fináléban játszott mérkőzések közül a legmagasabb pontszámú a 2. meccs volt 124 ponttal.')


lakers_starters = ['L. James', 'A. Davis', 'D. Green', 'K. Caldwell-Pope', 'A. Caruso']
if 'L. James' in lakers_starters:
    print('L. James benne van a kezdőcsapatban.')
else:
    print('L. James a cserepadon van.')

