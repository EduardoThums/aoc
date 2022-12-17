import re
from collections import deque


def main():
    # c = 4

    with open('input.txt', 'r') as file:

        for line in file.readlines():
            line = line.replace('\n', '')

            if line:
                virtual_max_length = len(line) - 4

                p1 = 0
                p2 = 1
                p3 = 2
                p4 = 3

                while p4 <= virtual_max_length:
                    p1_unique = line[p1] != line[p2] and line[p1] != line[p3] and line[p1] != line[p4]
                    p2_unique = line[p2] != line[p1] and line[p2] != line[p3] and line[p2] != line[p4]
                    p3_unique = line[p3] != line[p1] and line[p3] != line[p2] and line[p3] != line[p4]
                    p4_unique = line[p4] != line[p1] and line[p4] != line[p2] and line[p4] != line[p3]

                    if p1_unique and p2_unique and p3_unique and p4_unique:
                        # print(line[p1])
                        # print(line[p2])
                        # print(line[p3])
                        # print(line[p4])
                        print(p4 + 1)
                        break

                    else:
                        p1 += 1
                        p2 += 1
                        p3 += 1
                        p4 += 1


main()
