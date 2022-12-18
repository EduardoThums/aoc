class Tree:

    def __init__(self, value, up, right, down, left) -> None:
        self.value = value
        self.up = up
        self.right = right
        self.down = down
        self.left = left

    def is_visible(self):
        is_visible_from_up = self.value < self.up.value if self.up else True
        is_visible_from_right = self.value < self.right.value if self.right else True
        is_visible_from_down = self.value < self.down.value if self.down else True
        is_visible_from_left = self.value < self.left.value if self.left else True

        return is_visible_from_up or is_visible_from_right or is_visible_from_down or is_visible_from_left


def check_if_visible(value, direction, lines, row, column):
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
            return True

        if not edge.replace('\n', ''):
            return True

        if value <= int(edge):
            return False

        return check_if_visible(value, direction, lines, row, column)

    except IndexError:
        return True


def main():

    with open('input.txt', 'r') as file:
        lines = file.readlines()

    visible = 0

    for row, line in enumerate(lines):
        line = line.replace('\n', '')

        for column, value in enumerate(line):
            value = int(value)

            if check_if_visible(value, 'up', lines, row, column):
                visible += 1
                continue

            if check_if_visible(value, 'down', lines, row, column):
                visible += 1
                continue

            if check_if_visible(value, 'left', lines, row, column):
                visible += 1
                continue

            if check_if_visible(value, 'right', lines, row, column):
                visible += 1
                continue

    print(visible)


main()
