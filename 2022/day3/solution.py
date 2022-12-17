from string import ascii_letters
# print({a: i for i, a in enumerate(ascii_letters, 1)})

priority = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52
}


class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    # if root.value == value:
        # if not same_compartment:
        #     return root

        # else:
        #     acc += value

        # return root

    if root.value > value:
        root.left = insert(root.left, value)

    elif root.value < value:
        root.right = insert(root.right, value)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)
    # print(root.value)


def search(root, value, acc):
    if root:
        print(root.value)
        if root.value == value:
            acc += value
            return

        else:
            if root.value > value:
                search(root.left, value, acc)

            else:
                search(root.right, value, acc)


def optimized():

    with open('input.txt', 'r') as file:
        total = 0
        root = None
        # current_node = None

        for line in file.readlines():
            line = line.replace('\n', '')

            if line:
                # insert()
                l = int(len(line) / 2)
                p1 = line[:l]

                for i in line[:l]:
                    root = insert(root, priority.get(i))

                for i in line[l:]:
                    search(root, priority.get(i), total)
                # print(root.value)

                print(total)

                # search(root, )

            break


def on2_part_1():
    with open('input.txt', 'r') as file:
        total = 0
        root = None
        # current_node = None

        for line in file.readlines():
            line = line.replace('\n', '')

            if line:
                # insert()
                l = int(len(line) / 2)
                p1 = line[:l]
                p2 = line[l:]

                for i in p1:
                    if i in p2:
                        total += priority.get(i)
                        break

                # print
                    # for j in p2:
                    #     if i ==

                # for i in line[:l]:
                #     root = insert(root, priority.get(i))

                # for i in line[l:]:
                #     search(root, priority.get(i), total)
                # print(root.value)

                # print(total)

                # search(root, )

        print(total)


def part_2():
    with open('input.txt', 'r') as file:
        total = 0
        hm = {}

        for j, line in enumerate(file.readlines(), start=1):
            line = line.replace('\n', '')

            for i in set(line):
                if not hm.get(i):
                    hm[i] = 1

                else:
                    hm[i] += 1

            if j % 3 == 0:

                for k, v in hm.items():
                    if v == 3:
                        total += priority.get(k)

                hm = {}

        print(total)


part_2()
