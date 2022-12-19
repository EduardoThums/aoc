visited_positions = ['0,0']


def is_touching(head_x, head_y, tail_x, tail_y):
    return (0 <= abs(head_x - tail_x) <= 1) and (0 <= abs(head_y - tail_y) <= 1)


def move_tail_if_needed(head_x, head_y, tail_x, tail_y):
    if is_touching(head_x, head_y, tail_x, tail_y):
        return tail_x, tail_y

    # move down
    if head_y < tail_y and head_x == tail_x:
        tail_y -= 1

    # move up
    elif head_y > tail_y and head_x == tail_x:
        tail_y += 1

    # move right
    elif head_y == tail_y and head_x > tail_x:
        tail_x += 1

    # move left
    elif head_y == tail_y and head_x < tail_x:
        tail_x -= 1

    # move down right
    elif head_y < tail_y and head_x > tail_x:
        tail_y -= 1
        tail_x += 1

    # move down left
    elif head_y < tail_y and head_x < tail_x:
        tail_y -= 1
        tail_x -= 1

    # move up right
    elif head_y > tail_y and head_x > tail_x:
        tail_y += 1
        tail_x += 1

    # move up left
    elif head_y > tail_y and head_x < tail_x:
        tail_y += 1
        tail_x -= 1

    mark_position_as_visited(tail_y, tail_x)

    return tail_x, tail_y


def mark_position_as_visited(tail_y, tail_x):
    global visited_positions

    visited_positions.append(f'{tail_y},{tail_x}')


def display_grid(grid):
    for row in grid:

        for dot in row:
            print(dot, end='')

        print()

    print('---------')


def main():

    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    head_x = 0
    head_y = 0
    tail_x = 0
    tail_y = 0

    for line in lines:
        direction, quantity = line.split()
        quantity = int(quantity)

        if direction == 'R':

            while quantity > 0:
                head_x += 1

                tail_x, tail_y = move_tail_if_needed(head_x, head_y, tail_x, tail_y)

                quantity -= 1

        elif direction == 'L':
            while quantity > 0:
                head_x -= 1

                tail_x, tail_y = move_tail_if_needed(head_x, head_y, tail_x, tail_y)

                quantity -= 1

        elif direction == 'U':
            while quantity > 0:
                head_y += 1

                tail_x, tail_y = move_tail_if_needed(head_x, head_y, tail_x, tail_y)

                quantity -= 1

        elif direction == 'D':
            while quantity > 0:
                head_y -= 1

                tail_x, tail_y = move_tail_if_needed(head_x, head_y, tail_x, tail_y)

                quantity -= 1

    print(len(set(visited_positions)))


main()
