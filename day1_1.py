day_number = 1
with open(f'data/day{day_number}.txt', 'r') as f:
    data = f.read()

data = data.strip().split('\n')

total = 0

for line in data:
    calibration_value = ''
    for char in line:
        if char.isdigit():
            calibration_value += char
            break
    for char in line[::-1]:
        if char.isdigit():
            calibration_value += char
            break
    total += int(calibration_value)

print(total)