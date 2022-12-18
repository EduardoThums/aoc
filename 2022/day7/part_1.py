class Node:

    def __init__(self, value, parent, node_type, size=0) -> None:
        self.value = value
        self.parent = parent
        self.size = size
        self.children = {}
        self.node_type = node_type

    # def increment_size(self, size):
    #     self.size += size


def print_filesystem(root, deepth=0):
    if root.node_type == 'dir':
        print('  ' * deepth + f'- {root.value} (dir)')

        for children in root.children.values():
            print_filesystem(children, deepth + 1)

    else:
        print('  ' * deepth + f'- {root.value} (file, size={root.size})')
        return


def calculate_sum(root):
    # if root.node_type == 'file':
    #     return 0

    for c in root.children.values():
        if c.node_type == 'dir':
            if c.size <= 100000 and c.size > 0:
                print(c.size)

            calculate_sum(c)
            # print()
            # find_solution()

    # return root.size if root.size <= 100000 else 0


def back_to_root(root):
    if root.parent is None:
        return root

    return back_to_root(root.parent)


def increment_parent(root, size):
    if root:
        root.size += size
        increment_parent(root.parent, size)

    # if root.parent:
    #     root.parent.size += size
    #     increment_parent(root.parent, size)


def main():
    root = None
    node = None

    with open('input.txt', 'r') as file:

        for line in file.readlines():
            line = line.replace('\n', '')

            if line:

                # command
                if line.startswith('$'):
                    command = line.split(' ')[1]

                    if command == 'cd':
                        folder = line.split(' ')[2]

                        if root is None:
                            root = Node(folder, None, 'dir')
                            # node =
                            continue

                        if folder == '..':
                            root = root.parent

                        else:
                            root = root.children[folder]
                            # create roote witht the / folder

                    elif command == 'ls':
                        pass
                        # insert/travel current folder

                # listing files
                else:
                    if line.startswith('d'):
                        folder = line.split(' ')[1]
                        # add folder to tree

                        if root.children.get(folder) is None:
                            root.children[folder] = Node(folder, root, 'dir')

                    else:
                        size, file_name = line.split(' ')

                        if root.children.get(file_name) is None:
                            root.children[file_name] = Node(file_name, root, 'file', int(size))
                            root.size += int(size)

                            increment_parent(root.parent, int(size))
                            # if root.parent:
                            #     root.parent.size += int(size)

                    # add file to tree
                    # increment current folder size

    root = back_to_root(root)
    # print(root.value)
    # print_filesystem(root)
    calculate_sum(root)


main()
