day_number = 2
with open(f'data/day{day_number}.txt', 'r') as f:
    data = f.read()

cube_limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}

games = data.strip().split('\n')
total = 0
yikes = 0
for game in games:
    possible_game = True
    game_number = int(game.split()[1][:-1])
    rounds = game.split(': ')[1]
    rounds = rounds.split('; ')
    for i, round in enumerate(rounds):
        rounds[i] = round.split(', ')
        for cube_color in cube_limits:
            print(round)
            for cubes in rounds[i]:
                cubes = cubes.split('')
                yikes += 1
                if cubes[1] == cube_color:
                    if int(cubes[0]) > cube_limits[cube_color]:
                        possible_game = False
    if possible_game == True:
        total += game_number


print(total, yikes)

