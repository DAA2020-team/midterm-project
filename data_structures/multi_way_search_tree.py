from math import ceil
from typing import Tuple

from .map_base import MapBase
from .tree import Tree



class MultiWaySearchTree(Tree, MapBase):

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
        elements is a list of _Item: _Item is a (key-value)
        parent is the node's parent
        children is a list of links to the node's children
        """

        __slots__ = '_a', '_b', '_elements', '_parent', '_children', '_num_children'  # streamline memory usage

        def __init__(self, a, b, elements, parent=None, children=None):
            if elements is None or not a - 1 <= len(elements) <= b - 1:
                raise ValueError(f"size of elements must be in [{a - 1}, {b - 1}]")
            self._a = a
            self._b = b
            self._elements = elements
            self._parent = parent
            self._children = children if children is not None else [None] * (len(self._elements) + 1)

        def __repr__(self):
            """Returns the string representation of the Node"""
            return repr(self._elements)

    # ------------------------------- NESTED Position CLASS -------------------------------

    class Position(Tree.Position):
        """An abstraction representing the location of a single element within a tree.
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
        if a < 2:
            raise ValueError("a must be greater or equal to 2")
        if not a <= ceil((b - 1) / 2):
            raise ValueError("a must be greater at most ceil((b - 1) / 2)")
        self._a = a
        self._b = b
        self._root = None
        self._size = 0

    # -------------------------- PRIVATE METHODS --------------------------

    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
        Raise ValueError if tree is non-empty.
        """
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(self._a, self._b, [e])
        return self._make_position(self._root)

    def _subtree_search(self, p: Position, k) -> Tuple[Position, int]:
        """
        Returns:
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
            return p, index

        # Next position to search in is the child next to p.keys()[index]
        next_position = self._make_position(node._children[index + 1])
        if next_position is None:
            return None, index + 1
        return self._subtree_search(next_position, k)

    # -------------------------- PUBLIC METHODS --------------------------

    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the alberi (or None if tree is empty)."""
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
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))
        else:

            pass

    def __delitem__(self, v):
        pass

    def __getitem__(self, k):
        pass
