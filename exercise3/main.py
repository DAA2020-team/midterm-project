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

    del tree[6]
    del tree[7]

    print(tree)

    del tree[5]
    print(tree)

    print("OK!")


if __name__ == '__main__':
    main()
