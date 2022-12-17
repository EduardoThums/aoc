import re
from collections import deque


def main():
    stacks = {}

    with open('input.txt', 'r') as file:
        output = ''

        # lines = file.readlines()
        stacks = {
            '1': deque('N Q L S C Z P T'[::-1].split()),
            '2': deque('G C H V T P L'[::-1].split()),
            '3': deque('F Z C D'[::-1].split()),
            '4': deque('C V M L D T W G'[::-1].split()),
            '5': deque('C W P'[::-1].split()),
            '6': deque('Z S T C D J F P'[::-1].split()),
            '7': deque('D B G W V'[::-1].split()),
            '8': deque('W H Q S J N'[::-1].split()),
            '9': deque('V L S F Q C R'[::-1].split()),
        }

        for line in file.readlines():
            line = line.replace('\n', '')

            if line:
                quantity, source, dest = re.search(r'move ([0-9]+) from ([0-9]+) to ([0-9]+)', line).groups()

                source_stack = stacks.get(source)
                dest_stack = stacks.get(dest)

                for _ in range(0, int(quantity)):
                    dest_stack.append(source_stack.pop())

            # break

        # print(stacks)

        for q in stacks.values():
            print(q.pop(), end='')


main()
