# shapes:
# A Y - rock
# B X - paper
# C Z - scisor

# points:
# A - 1
# B - 2
# C - 3

# result:
# lose - 0
# draw - 3
# win - 6

points = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

translation = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissor',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissor',
}

# paper > rock > scisor
outcome = {
    'AY': 8,  # rock x paper
    'AX': 4,  # rock x rock
    'AZ': 3,  # rock x scissor
    'BY': 5,  # paper x paper
    'BX': 1,  # paper x rock
    'BZ': 9,  # paper x scissor
    'CY': 2,  # scissor x paper
    'CX': 7,  # scissor x rock
    'CZ': 6,  # scissor x scissor
}

# for l in ['A', 'B', 'C']:
#     for r in ['Y', 'X', 'Z']:
#         total = points.get(r) + outcome.get(f'{l}{r}')

#         print(total)
# print(f'{translation.get(l)} x {translation.get(r)}')


with open('input.txt', 'r') as file:
    total = 0

    for line in file.readlines():
        line = line.replace('\n', '')

        if line:
            total += outcome.get(line.replace(' ', ''))
            # c += int(line)

    print(total)
