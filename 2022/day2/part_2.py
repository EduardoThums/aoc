# rock - 1
# paper - 2
# scissor - 3

# paper > rock > scisor
strategy = {
    'AX': 0 + 3,  # rock x lose
    'AY': 3 + 1,  # rock x draw
    'AZ': 6 + 2,  # rock x win
    'BX': 0 + 1,  # paper x lose
    'BY': 3 + 2,  # paper x draw
    'BZ': 6 + 3,  # paper x win
    'CX': 0 + 2,  # scissor x lose
    'CY': 3 + 3,  # scissor x draw
    'CZ': 6 + 1,  # scissor x win
}

with open('input.txt', 'r') as file:
    total = 0

    for line in file.readlines():
        line = line.replace('\n', '')

        if line:
            total += strategy.get(line.replace(' ', ''))

    print(total)
