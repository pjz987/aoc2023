from string import punctuation
import re

day_number = 3
with open(f'data/day{day_number}.txt', 'r') as f:
    data = f.read()

# data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""

def get_border_coords(coords:dict, digit_string:str):
    border_coords = []
    border_coords.append((coords['x'], coords['y']))
    for i in range(len(digit_string) + 2):
        border_coords.append((coords['x'] - i, coords['y'] + 1))
        border_coords.append((coords['x'] - i, coords['y'] - 1))
    border_coords.append((coords['x'] - len(digit_string) - 1, coords['y']))
    return border_coords


symbol_coords = []
legit_nums = []
illegit_nums = []

grid = data.strip().split('\n')
for y, row in enumerate(grid):
   for x, cell in enumerate(row):
       if cell in punctuation and cell != '.':
           symbol_coords.append((x,y))

print(symbol_coords)

matcher = re.compile('([0-9])+')

total = 0

for y, row in enumerate(grid):
    # print(row)
    digit_string = ''
    for x, cell in enumerate(row):
        if cell.isdigit():
            digit_string += cell
        elif digit_string:
            border_coords = get_border_coords({'x': x, 'y': y}, digit_string)
            border_coords = list(filter(
                lambda c: c[0] in range(0, 140) and c[1] in range(0, 140),
                border_coords
                ))
            # print(digit_string)
            # print(border_coords)
            before = len(legit_nums)
            for coord in border_coords:
                if coord in symbol_coords:
                    total += int(digit_string)
                    legit_nums += [digit_string]
                    break
            if before == len(legit_nums):
                illegit_nums += [digit_string]
            digit_string = ''
            

print(total)
print(legit_nums)
    

# unique_chars = list(set(data))
# unique_chars.sort()
# # print(''.join(unique_chars))

# print(illegit_nums)

