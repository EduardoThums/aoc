from collections import namedtuple


class Tail:

    def __init__(self, name, y, x) -> None:
        self.name = name
        self.y = y
        self.x = x


visited_positions = ['0,0']


def is_touching(head_x, head_y, tail):
    return (0 <= abs(head_x - tail.x) <= 1) and (0 <= abs(head_y - tail.y) <= 1)


def move_tail_if_needed(head_y, head_x, tail):
    if is_touching(head_x, head_y, tail):
        return

    # move down
    if head_y < tail.y and head_x == tail.x:
        tail.y -= 1

    # move up
    elif head_y > tail.y and head_x == tail.x:
        tail.y += 1

    # move right
    elif head_y == tail.y and head_x > tail.x:
        tail.x += 1

    # move left
    elif head_y == tail.y and head_x < tail.x:
        tail.x -= 1

    # move down right
    elif head_y < tail.y and head_x > tail.x:
        tail.y -= 1
        tail.x += 1

    # move down left
    elif head_y < tail.y and head_x < tail.x:
        tail.y -= 1
        tail.x -= 1

    # move up right
    elif head_y > tail.y and head_x > tail.x:
        tail.y += 1
        tail.x += 1

    # move up left
    elif head_y > tail.y and head_x < tail.x:
        tail.y += 1
        tail.x -= 1

    mark_position_as_visited(tail)


def mark_position_as_visited(tail):
    global visited_positions

    if tail.name == '9':
        visited_positions.append(f'{tail.y},{tail.x}')


def display_grid(grid):
    for row in grid:

        for dot in row:
            print(dot, end='')

        print()

    print('---------')


def main():

    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    head = Tail('H', 0, 0)
    # tails = [Tail('H', 0, 0)]
    tails = [Tail(str(i), 0, 0) for i in range(1, 10)]
    # virtual_length = len(tails) - 1

    for line in lines:
        direction, quantity = line.split()
        quantity = int(quantity)

        if direction == 'R':

            while quantity > 0:
                head.x += 1
                head_y, head_x = head.y, head.x

                for tail in tails:
                    move_tail_if_needed(head_y, head_x, tail)
                    head_y, head_x = tail.y, tail.x

                quantity -= 1

        elif direction == 'L':
            while quantity > 0:
                head.x -= 1
                head_y, head_x = head.y, head.x

                for tail in tails:
                    move_tail_if_needed(head_y, head_x, tail)
                    head_y, head_x = tail.y, tail.x

                quantity -= 1

        elif direction == 'U':
            while quantity > 0:
                head.y += 1
                head_y, head_x = head.y, head.x

                for tail in tails:
                    move_tail_if_needed(head_y, head_x, tail)
                    head_y, head_x = tail.y, tail.x

                quantity -= 1

        elif direction == 'D':
            while quantity > 0:
                head.y -= 1
                head_y, head_x = head.y, head.x

                for tail in tails:
                    move_tail_if_needed(head_y, head_x, tail)
                    head_y, head_x = tail.y, tail.x

                quantity -= 1

    print(len(set(visited_positions)))


main()
