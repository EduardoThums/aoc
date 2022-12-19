def is_touching_head(head_x, head_y, tail_x, tail_y):
    touching_diagonally = (1 <= abs(head_y - head_y) <= 2) and (1 <= abs(head_y - head_y) <= 2)
    # touching_vertically = (0 <= abs(head_y - head_x) <= 1) or (0 <= abs(tail_y - tail_x) <= 1)

    if head_y == tail_y:
        return 0 <= abs(head_x - tail_x) <= 1

    if head_x == tail_x:
        return 0 <= abs(head_y - tail_y) <= 1

    return abs(head_y - tail_y) == 1 and abs(head_x - tail_x) == 1
    # return abs(head_x - tail_x) == 1

    # if touching_diagonally

    # print(touching_diagonally)
    # print(touching_vertically)

    return touching_diagonally
    #     return
    # if (1 <= abs(head_y - head_y) <= 2) and (1 <= abs(head_y - head_y) <= 2):
    #     return True

    # if 0 == abs(head_y - tail_y) or abs(head_x - tail_x):
    #     return True

    # return False


def move_tail_if_needed(grid, head_x, head_y, tail_x, tail_y):
    print(f'H({head_y},{head_x})')
    print(f'T({tail_y},{tail_x})')
    # print(head_x, head_y, tail_x, tail_y)

    if is_touching_head(head_x, head_y, tail_x, tail_y):
        return tail_x, tail_y

    grid[len(grid) - tail_y - 1][tail_x] = '.'

    # move up
    if head_x == tail_x and head_y < tail_y:
        tail_y += 1

    # move down
    if head_x == tail_x and head_y > tail_y:
        tail_y -= 1

    # move right
    if head_y == tail_y and head_x < tail_x:
        tail_x -= 1

    # move left
    if head_y == tail_y and head_x > tail_x:
        tail_x += 1

    # move diagonally up right
    if head_y < tail_y and head_x > tail_x:
        tail_y -= 1
        tail_x += 1

    # move diagonally up left
    if head_y < tail_y and head_x < tail_x:
        tail_y -= 1
        tail_x -= 1

    # move diagonally down right
    if head_y > tail_y and head_x > tail_x:
        tail_y += 1
        tail_x += 1

    # move diagonally down left
    if head_y > tail_y and head_x < tail_x:
        tail_y += 1
        tail_x -= 1

    # print(tail_y, tail_y)

    grid[len(grid) - tail_y - 1][tail_x] = 'T'

    return tail_x, tail_y


def display_grid(grid):
    for row in grid:

        for dot in row:
            print(dot, end='')

        print()

    print('---------')


def main():

    with open('input_test.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

        # when the H moves check if T is already touching up/down/left/right
        # yes: dont move
        # no: move to the closets position

        # build the grid before count the visited positions

    grid_x = 1
    grid_y = 1
    x = 1
    y = 1

    for line in lines:
        move, quantity = line.split(' ')
        quantity = int(quantity)

        if move == 'R':
            if x + quantity > grid_x:
                grid_x = x + quantity

            x += quantity

        elif move == 'L':
            if x - quantity <= 0:
                difference = quantity - x
                grid_x += difference
                x += difference

            x -= quantity

        elif move == 'U':
            if y + quantity > grid_y:
                grid_y = y + quantity

            y += quantity

        elif move == 'D':
            if y - quantity <= 0:
                difference = quantity - y
                grid_y += difference
                y += difference

            y -= quantity

        else:
            pass

    grid = [] * grid_y

    for _y in range(grid_y):
        row = ['.' for _ in range(grid_x)]

        grid.append(row)

    x = 0
    y = 0
    tail_x = 0
    tail_y = 0

    display_grid(grid)

    for line in lines[:2]:
        move, quantity = line.split(' ')
        quantity = int(quantity)

        if move == 'R':
            row = grid[grid_y - y - 1]

            while quantity > 0:
                row[x] = "."
                x += 1
                row[x] = "H"

                tail_x, tail_y = move_tail_if_needed(grid, x, y, tail_x, tail_y)

                display_grid(grid)

                quantity -= 1

        elif move == 'L':
            row = grid[grid_y - y - 1]

            row[x] = "."
            x -= quantity
            row[x] = "H"

            # for i in range(quantity):
            #     x -= 1
            #     row[i] = "#"

        elif move == 'U':
            while quantity > 0:
                grid[grid_y - y - 1][x] = '.'
                y += 1
                grid[grid_y - y - 1][x] = 'H'

                # display_grid(grid)

                tail_x, tail_y = move_tail_if_needed(grid, x, y, tail_x, tail_y)

                display_grid(grid)

                quantity -= 1

            # grid[grid_y - y - 1][x] = 'H'

            # y += quantity

            # while quantity > 0:
            #     grid[grid_y - y - 1][x] = '#'

            #     y += 1
            #     quantity -= 1

        elif move == 'D':
            grid[grid_y - y - 1][x] = '.'
            y -= quantity
            grid[grid_y - y - 1][x] = 'H'

            # while quantity > 0:
            #     grid[grid_y - y - 1][x] = '#'

            #     y -= 1
            #     quantity -= 1

        else:
            pass

        # display_grid(grid)

        # tail_x, tail_y = move_tail_if_needed(grid, x, y, tail_x, tail_y)

        # break

    # display_grid(grid)


main()
