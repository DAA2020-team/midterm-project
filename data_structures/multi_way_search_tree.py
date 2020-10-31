from math import ceil
from typing import Tuple, List

from .map_base import MapBase
from .tree import Tree

from utils import binary_search


class MultiWaySearchTree(Tree, MapBase):
    """
    Sorted map implementation using a multi-way seach tree, with parametrizable dimensions.
    """

    # ------------------------------- NESTED _Item CLASS -------------------------------

    class _Item(MapBase._Item):
        """Lightweight composite to store key-value pairs as map items."""

        def __repr__(self):
            """Returns the string representation of an Item: (key-value)"""
            return repr({self._key: self._value})

    # -------------------------- NESTED PRIVATE _Node CLASS --------------------------

    class _Node:
        """
        Lightweight, nonpublic class for storing a node.
        a is the minimum number of children for each node, thus the minimum number of keys for each node is a - 1
        b is the maximum number of children for each node, thus the maximum number of keys for each node is b - 1
        elements is a list of _Item: _Item is a (key-value) pair
        parent is the node's parent
        children is a list of _Node, i.e. links to the node's children
        """

        __slots__ = '_a', '_b', '_elements', '_parent', '_children'

        def __init__(self, a: int, b: int, elements: List, parent=None, children=None):
            if elements is None or not a - 1 <= len(elements) <= b - 1:
                raise ValueError(f"size of elements must be in [{a - 1}, {b - 1}]. Found {len(elements)}")
            self._a = a
            self._b = b
            self._elements = elements
            self._parent = parent
            self._children = children if children is not None else [None] * (len(self._elements) + 1)

        def __repr__(self):
            """Returns the string representation of the Node"""
            return repr(self._elements)

        def __len__(self):
            return len(self._elements)

    # ------------------------------- NESTED Position CLASS -------------------------------

    class Position(Tree.Position):
        """
        An abstraction representing the location of a single element within a tree.
        Note that two position instaces may represent the same inherent location in a tree.
        Therefore, users should always rely on syntax 'p == q' rather than 'p is q' when testing
        equivalence of positions.
        """

        __slots__ = '_container', '_node'

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._elements

        def keys(self):
            """Return key of map's key-value pair."""
            return [item._key for item in self.element()]

        def values(self):
            """Return value of map's key-value pair."""
            return [item._value for item in self.element()]

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __repr__(self):
            """Returns the string representation of the Position"""
            return repr(self._node)

        def is_empty(self):
            return len(self) == 0

        def is_full(self):
            return len(self) == self._node._b - 1

        def is_overflow(self):
            return len(self) > self._node._b - 1

        def __len__(self):
            return len(self.element())

    # ------------------------------- utility methods -------------------------------

    def _validate(self, p) -> _Node:
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node) -> Position:
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    # ------------------------------- CONSTRUCTOR -------------------------------

    __slots__ = '_a', '_b', '_root', '_size'

    def __init__(self, a=2, b=8):
        """
        Constructor
        :param a: minimum number of children of each node
        :param b: maximum number of children of each node
        """
        if not 2 <= a <= ceil((b - 1) / 2):
            raise ValueError(f"a must be in [2, {ceil((b - 1) / 2)}]. Found {a}")
        self._a = a
        self._b = b
        self._root = None
        self._size = 0

    # -------------------------- PRIVATE METHODS --------------------------

    def _add_root(self, e: _Item):
        """
        Places element e at the root of an empty tree and return new Position.
        Raise ValueError if tree is non-empty.
        """
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(self._a, self._b, [e])
        return self._make_position(self._root)

    def _subtree_search(self, p: Position, k) -> Tuple[bool, Position, int]:
        """
        Searches key k in the subtree rooted at p.
        Returns:
            True if k is found, False otherwise
            Position of p's subtree having key k,
            index of the key k in the keys list of the position,
            or last node and index searched.
        """
        # Validate
        node = self._validate(p)

        # Binary-search k in node p
        found, index = binary_search(p.keys(), k)

        # Successful search
        if found:
            return True, p, index

        # Next position to search in is the child next to p.keys()[index]
        next_position = self._make_position(node._children[index + 1])
        if next_position is None:
            return False, p, index + 1
        return self._subtree_search(next_position, k)

    def _subtree_repr(self, p: Position, level: int, children_counter: int) -> str:
        """Returns the string representation of the subtree rooted at p"""
        string = ""
        self._validate(p)
        if level == 0:
            num_children = self.num_children(p)
            if num_children == 0:
                string += f"{'  ' * level}level {level}:  {p}\n"
            else:
                string += f"{'  ' * level}level {level}:  {p}, {num_children} children:\n"
        else:
            num_children = self.num_children(p)
            if num_children == 0:
                string += f"{'  ' * level}level {level}, child {children_counter}:  {p}\n"
            else:
                string += f"{'  ' * level}level {level}, child {children_counter}:  {p}, " \
                          f"{self.num_children(p)} children:\n"
        children_counter = 0
        for child in self.children(p):
            string += self._subtree_repr(child, level + 1, children_counter)
            children_counter += 1
        return string

    def _split(self, p: Position) -> Tuple[_Node, _Item, _Node]:
        """
        Splits p in smaller node, median item and bigger node
        :param p: position to split
        :return:
            smaller node: Node: position with keys smaller than median key
            median item: Item: item with median key and value
            bigger node: Node: position with keys bigger than median key
        """
        self._validate(p)
        # Consider the keys saved in node p
        keys = p.keys()[:]
        values = p.values()[:]
        # We split keys and values in three parts:
        #   the median key (km) and median value (vm),
        #   keys and values smaller than the km and vm (ks and vs),
        #   and keys and values larger than the km and vm (kb and vb)
        median = len(keys) // 2
        km, vm = keys[median], values[median]
        ks, vs = keys[:median], values[:median]
        kb, vb = keys[median + 1:], values[median + 1:]
        # With ks and vs we create a new node
        smaller_node = self._Node(self._a, self._b, [self._Item(k, v) for k, v in zip(ks, vs)])
        for j in range(median + 1):  # j parses all children of smaller_node: they are median + 1
            smaller_node._children[j] = p._node._children[j]
            if p._node._children[j] is not None:
                p._node._children[j]._parent = smaller_node
        # With kb and vb we create a new node
        bigger_node = self._Node(self._a, self._b, [self._Item(k, v) for k, v in zip(kb, vb)])
        for j in range(median):  # j parses all children of bigger_node: they are median
            bigger_node._children[j] = p._node._children[median + 1 + j]
            if p._node._children[j] is not None:
                p._node._children[median + 1 + j]._parent = bigger_node
        return smaller_node, self._Item(km, vm), bigger_node

    # -------------------------- PUBLIC METHODS --------------------------

    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def num_children(self, p):
        """Return the number of children that Position p has."""
        node = self._validate(p)
        return len(list(filter(lambda x: x is not None, node._children)))

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        node = self._validate(p)
        for child in node._children:
            if child is not None:
                yield self._make_position(child)

    def __setitem__(self, k, v):
        """
        Inserts a new (key-value) item in the tree
        :param k: the key of the item to insert
        :param v: the value of the item to insert
        :return: None
        """
        if self.is_empty():
            # If the tree is empty, we add a root
            leaf = self._add_root(self._Item(k, v))
        else:
            # Search for the node p that should contain k
            found, p, i = self._subtree_search(self.root(), k)
            if not found:  # k is not in the tree, insert (k,v) in the tree
                smaller_node = None
                bigger_node = None
                while p is not None:  # we ended up to the root
                    node = p._node
                    # To mantain p keys ordered, we have to move keys from index i
                    node._elements = node._elements[:i] + [self._Item(k, v)] + node._elements[i:]
                    # We also have to move the children from index i
                    node._children = node._children[:i] + [smaller_node, bigger_node] + node._children[i + 1:]
                    if p.is_overflow():
                        smaller_node, median_item, bigger_node = self._split(p)
                        k, v = median_item._key, median_item._value
                        p = self.parent(p)
                        if p is None:  # p was the root
                            # A new root is created
                            self._root = self._Node(self._a, self._b, [self._Item(k, v)])
                            root = self._make_position(self._root)
                            # the left child of the new root is smaller_node
                            root._node._children[0] = smaller_node
                            smaller_node._parent = self._root
                            # the right child of the new root is bigger_node
                            root._node._children[1] = bigger_node
                            bigger_node._parent = self._root
                        else:  # root of p exists
                            smaller_node._parent = p._node
                            bigger_node._parent = p._node
                            # Search where to insert k in p
                            _, i = binary_search(p.keys(), k)
                            i += 1
                    else:  # p is not in overflow, insertion completed
                        break
                # Increment the tree size
                self._size += 1
            else:  # k is in p at index i, substitute old value with v
                p._node._elements[i]._value = v
            pass

    def __delitem__(self, v):
        pass

    def __getitem__(self, k):
        pass

    def __repr__(self):
        """Returns the string representation of the tree, level by level"""
        return self._subtree_repr(self.root(), 0, 0)
