favorite_team = ['Armstrong, BJ', 'Cartwright, Bill', 'Grant, Horace', 'Hodges, Craig', 'Hopson, Dennis', 'Jordan, Michael', 'King, Stacey', 'Levingston, Cliff', 'Paxson, John', 'Perdue, Will', 'Pippen, Scottie', 'Williams, Scott']
print(favorite_team[0])
print(favorite_team[1])
print(favorite_team[-1])
print(favorite_team[-2])
print(favorite_team[-3])


def get_middle_people(favorite_team):
    print(favorite_team[7:13])

get_middle_people(favorite_team)





def add_new_player(favorite_team):
    favorite_team.append('Toni Kukoc')
    print(favorite_team)

add_new_player(favorite_team)

def add_captain(favorite_team):
    favorite_team.insert(0, 'Jordan, Michael')
    print(favorite_team)

add_captain(favorite_team)

def remove_player(favorite_team):
    favorite_team.remove('Hopson, Dennis')
    print(favorite_team)

remove_player(favorite_team)

def delete_player(favorite_team):
    del favorite_team[5]
    print(favorite_team)

delete_player(favorite_team)

def print_player_names(favorite_team):
    for player_names in favorite_team:
        print(player_names)

print_player_names(favorite_team)











