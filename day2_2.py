day_number = 2
with open(f'data/day{day_number}.txt', 'r') as f:
    data = f.read()

games = data.strip().split('\n')
total = 0
for game in games:
    game_number = int(game.split()[1][:-1])
    rounds = game.split(': ')[1]
    rounds = rounds.split('; ')
    cube_values = {'red': [], 'green': [], 'blue': []}
    for i, round in enumerate(rounds):
        rounds[i] = round.split(', ')
        for cube_color in cube_values:
            for cubes in rounds[i]:
                cubes = cubes.split()
                if cubes[1] == cube_color:
                    cube_values[cube_color].append(int(cubes[0]))
    # print(game_number, cube_values)
    power = 1
    if cube_values['red']:
        red = max(cube_values['red'])
        power *= red
    if cube_values['green']:
        green = max(cube_values['green'])
        power *= green
    if cube_values['blue']:
        blue = max(cube_values['blue'])
        power *= blue
    total += power
    print(game)
    print(red, green, blue, power)


print(total)

