from data_structures.multi_way_search_tree import MultiWaySearchTree


def main():
    tree = MultiWaySearchTree()

    tree[17] = 104

    root = tree.root()

    print(root.keys(), root.values())

    print(root)

    print(tree.num_children(root))

    for child in tree.children(root):
        print("Here")
        print(child)

    print(tree._subtree_search(tree.root(), 65))

    print("OK!")


if __name__ == '__main__':
    main()
