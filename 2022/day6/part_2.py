import re
from collections import deque


def main():
    with open('input_test.txt', 'r') as file:

        for line in file.readlines():
            line = line.replace('\n', '')

            if line:
                virtual_max_length = len(line) - 14

                p1 = 0

                while p1 <= virtual_max_length:
                    if len(set(line[p1:p1 + 14])) == 14:
                        print(p1 + 14)
                        break

                    else:
                        p1 += 1


main()
