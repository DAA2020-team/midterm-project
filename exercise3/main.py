from random import shuffle, seed

from data_structures.multi_way_search_tree import MultiWaySearchTree


def main():
    seed(2020)

    tree = MultiWaySearchTree()

    tree[17] = 104

    root = tree.root()

    print("*** Check root ***")
    print(root.keys(), root.values())
    print(root)
    print(tree.num_children(root))

    for child in tree.children(root):
        print("Here")
        print(child)

    x = 16
    print(f"*** Search {x} ***")
    print(tree._subtree_search(tree.root(), x))

    possible_keys = list(range(100))
    shuffle(possible_keys)
    for i in range(100):
        x = possible_keys[i]

        print(f"*** Insert {x} ***")
        tree[x] = int(str(x) * 2)
        # print(tree)

    for i in range(43, 49):
        del tree[i]

    del tree[49]

    for i in range(51, 53):
        del tree[i]

    print(tree)

    del tree[54]
    print(tree)

    for i in range(57, 61):
        del tree[i]

    print(tree)

    for i in range(63, 65):
        del tree[i]

    print(tree)

    for i in range(67, 73):
        print("Deleting " + str(i))
        del tree[i]
        print(tree)

    del tree[50]
    print(tree)

    del tree[73]
    print(tree)

    del tree[61]
    print(tree)

    del tree[53]
    print(tree)

    del tree[62]
    print(tree)

    del tree[65]
    print(tree)

    for i in range(75, 81):
        del tree[i]

    print(tree)

    del tree[55]
    print(tree)


    print("OK!")


if __name__ == '__main__':
    main()
