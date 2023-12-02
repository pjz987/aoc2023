day_number = 1
with open(f'data/day{day_number}.txt', 'r') as f:
    data = f.read()

data = data.strip().split('\n')

def get_first_digit(line):
    for i, char in enumerate(line):
        if char.isdigit():
            return char, i

def get_first_word(line, reversed=False):
    for number in numbers:
        if not reversed:
            number['i'] = line.find(number['name'])
        elif reversed:
            number['i'] = line[::-1].find(number['name'][::-1])
    filtered_numbers = list(filter(lambda n: n['i'] >= 0, numbers))
    sorted_numbers = sorted(filtered_numbers, key=lambda n: n['i'])
    if sorted_numbers:
        return str(sorted_numbers[0]['value']), sorted_numbers[0]['i']


numbers = [
    {'value': 0, 'i': None, 'name': 'zero'},
    {'value': 1, 'i': None, 'name': 'one'},
    {'value': 2, 'i': None, 'name': 'two'},
    {'value': 3, 'i': None, 'name': 'three'},
    {'value': 4, 'i': None, 'name': 'four'},
    {'value': 5, 'i': None, 'name': 'five'},
    {'value': 6, 'i': None, 'name': 'six'},
    {'value': 7, 'i': None, 'name': 'seven'},
    {'value': 8, 'i': None, 'name': 'eight'},
    {'value': 9, 'i': None, 'name': 'nine'},
]

total = 0

for line in data:
    first_values = []
    last_values = []
    first_digit, first_digit_i = get_first_digit(line)
    first_values.append((first_digit, first_digit_i))
    last_digit, last_digit_i = get_first_digit(line[::-1])
    last_values.append((last_digit, last_digit_i))
    # calibration_value = first_digit + last_digit
    # total += int(calibration_value)
    # print(line, first_digit, last_digit, calibration_value)
    print(line)
    first_word = get_first_word(line)
    if first_word is not None:
        first_values.append(first_word)
    last_word = get_first_word(line, True)
    if last_word is not None:
        last_values.append(last_word)
    first_number = min(first_values, key=lambda value: value[1])
    last_number = min(last_values, key=lambda value: value[1])
    print(first_number, last_number)

    calibration_value = int(first_number[0] + last_number[0])
    total += calibration_value



print(total)