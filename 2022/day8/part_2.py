total = 0


def calc_scenic_score(value, direction, lines, row, column):
    global total

    try:
        if direction == 'up':
            row -= 1

        elif direction == 'down':
            row += 1

        elif direction == 'left':
            column -= 1

        elif direction == 'right':
            column += 1

        edge = lines[row][column]

        if row < 0 or column < 0:
            return max(total, 0)

        if not edge.replace('\n', ''):
            return max(total, 0)

        if value >= int(edge):
            total += 1

            if value > int(edge):
                calc_scenic_score(value, direction, lines, row, column)

        # if value >= int(edge):
        #     total += 1

        return max(total, 0)

    except IndexError:
        return max(total, 0)


def main():
    global total

    with open('input.txt', 'r') as file:
        lines = file.readlines()

    highest = 0

    for row, line in enumerate(lines):
        line = line.replace('\n', '')

        for column, value in enumerate(line):
            value = int(value)

            up = calc_scenic_score(value, 'up', lines, row, column)
            total = 0

            down = calc_scenic_score(value, 'down', lines, row, column)
            total = 0
            right = calc_scenic_score(value, 'right', lines, row, column)
            total = 0
            left = calc_scenic_score(value, 'left', lines, row, column)
            total = 0

            score = up * down * right * left

            if highest < score:
                highest = score

    print(highest)


main()
