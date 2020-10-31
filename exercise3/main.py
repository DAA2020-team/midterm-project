from random import shuffle

from data_structures.multi_way_search_tree import MultiWaySearchTree


def main():
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

    possible_keys = list(range(101))
    shuffle(possible_keys)
    for i in range(100):
        x = possible_keys[i]

        print(f"*** Insert {x} ***")
        tree[x] = x
        # print(tree)

    print(tree)
    print("OK!")


if __name__ == '__main__':
    main()
