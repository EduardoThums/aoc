class Node:

    def __init__(self, value, parent, node_type, size=0) -> None:
        self.value = value
        self.parent = parent
        self.size = size
        self.children = {}
        self.node_type = node_type
        self.has_subfolder = False


def print_filesystem(root, deepth=0):
    if root.node_type == 'dir':
        print('  ' * deepth + f'- {root.value} (dir)')

        for children in root.children.values():
            print_filesystem(children, deepth + 1)

    else:
        print('  ' * deepth + f'- {root.value} (file, size={root.size})')
        return

# 1. find the sum of all folders
# 2. find the smallest that is enough to  the difference in (available - used)


def find_used_space(root):
    total = 0

    if root.node_type == 'file':
        return 0

    if not root.has_subfolder:
        return root.size

    for c in root.children.values():
        total += find_used_space(c)

    return total


def find_lacking_space(root, lacking_space, arr):
    if root.node_type == 'file':
        return

    if root.size >= lacking_space:
        print('here')
        arr.append(root.size)

    for c in root.children.values():
        find_lacking_space(c, lacking_space, arr)


def back_to_root(root):
    if root.parent is None:
        return root

    return back_to_root(root.parent)


def increment_parent(root, size):
    if root:
        root.size += size
        increment_parent(root.parent, size)


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
                            root.has_subfolder = True
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
                            root.has_subfolder = True

                    else:
                        size, file_name = line.split(' ')

                        if root.children.get(file_name) is None:
                            root.children[file_name] = Node(file_name, root, 'file', int(size))
                            root.size += int(size)

                            increment_parent(root.parent, int(size))

    root = back_to_root(root)
    available_space = 70_000_000
    used_space = root.size
    free_space = available_space - used_space
    lacking_space = 30_000_000 - free_space

    arr = []
    find_lacking_space(root, lacking_space, arr)
    print(min(arr))


main()
