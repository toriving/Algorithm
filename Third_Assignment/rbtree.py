# The possible Node colors
BLACK = 'BLACK'
RED = 'RED'
NIL = 'NIL'

# Node class for using in augmented red-black tree.
# This class has 5 fields. Each is key, color, parent, left, right and size.
# If you print node class, you can get key color and size
# (e.g., 20B1 means the key is 20, the color is black, and the size is 1).
# In addition, the show method is print itself, left and right.
# Lastly, the update_size method is used when there is a change in the tree to update the size of the node.

class node:
    def __init__(self, key, color=RED, parent=None, left=None, right=None):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right
        self.size = 0

    def __str__(self):
        s = str(self.key)
        if self.key is not NIL:
            s += self.color[0] + str(self.size)
        return s

    def show(self, level=0, indent="   "):
        s = level * indent + str(self.key)
        if self.key is not NIL:
            s += self.color[0] + str(self.size)
        if self.left:
            s = s + "\n" + self.left.show(level + 1, indent)
        if self.right:
            s = s + "\n" + self.right.show(level + 1, indent)
        return s

    def update_size(self):
        if self.key is NIL:
            self.size = 0
        else:
            self.size = self.left.size + self.right.size + 1


class Augmented_Red_Black_Tree:
    # Augmented Red Black Tree is consisted of three fields and many method.
    # If you want to use this tree, you just define without any arguments.
    # For example, t = Augmented_Red_Black_Tree()
    # The initialized tree consists of NIL nodes and zero size.
    def __init__(self):
        self.NIL = node(NIL, BLACK)
        self.ROOT = self.NIL
        self.size = 0

    def __str__(self):
        # Printing tree structure.
        return ("(root.size = %d)\n" % self.size) + str(self.ROOT.show())

    def print(self):
        # Printing tree structure same as print(tree).
        print(self)

    def report(self, a, b):
        # Printing node's keys between a and b using _report method.
        self._report(self.ROOT, a, b)

    def count(self, a, b):
        # Printing the number of node's keys between a and b using _count method.
        print(self._count(self.ROOT, a, b))

    def select(self, x, i):
        # Selecting i th smallest node from x (Usually x is ROOT).
        r = x.left.size + 1
        if i == r:
            return x
        elif i < r:
            return self.select(x.left, i)
        else:
            return self.select(x.right, i-r)

    def rank(self, x):
        # Printing the rank of x.
        r = x.left.size + 1
        y = x
        while y is not self.ROOT:
            if y is y.parent.right:
                r = r + y.parent.left.size + 1
            y= y.parent
        return r

    def search(self, k, x=None):
        # Finding node using key.
        # It does not return key of node, but returns node.
        if x is None:
            x = self.ROOT
        if x is self.NIL or k == x.key:
            return x
        if k < x.key:
            return self.search(k, x.left)
        else:
            return self.search(k, x.right)

    def predecessor(self, x):
        # Finding predecessor node and returning it.
        if x.left is not self.NIL:
            return self.maximum(x.left)
        y = x.parent
        while y is not self.NIL and x == y.left:
            x = y
            y = y.parent
        return y

    def successor(self, x):
        # Finding successor node and returning it.
        if x.right is not self.NIL:
            return self.minimum(x.right)
        y = x.parent
        while y is not self.NIL and x == y.right:
            x = y
            y = y.parent
        return y

    def minimum(self, x=None):
        # Finding minimum node and returning it.
        if x is None:
            x = self.ROOT
        while x.left is not self.NIL:
            x = x.left
        return x

    def maximum(self, x=None):
        # Finding maximum node and returning it.
        if x is None:
            x = self.ROOT
        while x.right is not self.NIL:
            x = x.right
        return x

    def insert(self, z):
        # It is insert method to add new nodes.
        z = self._insert(z)
        y = self.NIL
        x = self.ROOT

        while x is not self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is self.NIL:
            self.ROOT = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.NIL
        z.right = self.NIL
        z.color = RED
        self._insert_fixup(z)
        self.update_node_size()

    def delete(self, z):
        # It is delete method to remove existing nodes.
        z = self._delete(z)
        y = z
        y_origin_color = y.color
        if z.left is self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right is self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_origin_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_origin_color == BLACK:
            self._delete_fixup(x)
        self.size -= 1
        self.update_node_size()

    def inorder_tree_walk(self, x=None):
        # Inorder tree walk.
        if x is None:
            x = self.ROOT
        if x.left:
            self.inorder_tree_walk(x.left)
        if x.key is not NIL:
            print(x.key, x.color)
        if x.right:
            self.inorder_tree_walk(x.right)

    def update_node_size(self, x=None):
        # Update size of node.
        if x is None:
            x = self.ROOT
        if x.left:
            self.update_node_size(x.left)
        if x.right:
            self.update_node_size(x.right)
        if x.key is not NIL:
            x.update_size()

    # The following methods are sub-methods that help the main methods above

    def _report(self, x, a, b):
        # Sub method for report method.
        if a <= x.key and x.left.key is not NIL:
            self._report(x.left, a, b)
        if a <= x.key <= b:
            print(x.key)
        if x.key <= b and x.right.key is not NIL:
            self._report(x.right, a, b)

    def _count(self, x, a, b):
        # Sub method for count method.
        if x.key == NIL:
            return 0
        if a <= x.key <= b:
            return 1 + self._count(x.left, a, b) + self._count(x.right, a, b)
        elif x.key < a:
            return self._count(x.right, a, b)
        else:
            return self._count(x.left, a, b)

    def _delete(self, z):
        return self.search(z)

    def _insert(self, z):
        return node(z, RED, None, self.NIL, self.NIL)

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is self.NIL:
            self.ROOT = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is self.NIL:
            self.ROOT = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

    def _insert_fixup(self, z):
        while z != self.ROOT and z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == RED:  # case1
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:  # case2
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = BLACK  # case3
                    z.parent.parent.color = RED
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == RED:  # case1
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:  # case2
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = BLACK  # case3
                    z.parent.parent.color = RED
                    self._left_rotate(z.parent.parent)
        self.ROOT.color = BLACK
        self.size += 1

    def _transplant(self, u, v):
        if u.parent is self.NIL:
            self.ROOT = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _delete_fixup(self, x):
        while x is not self.ROOT and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED: # case 1
                    w.color = BLACK
                    x.parent.color = RED
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK: # case2
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK: # case 3
                        w.left.color = BLACK
                        w.color = RED
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self._left_rotate(x.parent)
                    x = self.ROOT
            else:
                w = x.parent.left
                if w.color == RED: # case 1
                    w.color = BLACK
                    x.parent.color = RED
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == BLACK and w.left.color == BLACK: # case2
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK: # case 3
                        w.right.color = BLACK
                        w.color = RED
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self._right_rotate(x.parent)
                    x = self.ROOT
        x.color = BLACK