################################################################################
#                                                                              #
#  Binary Search Tree                                                          #
#                                                                              #
################################################################################


class BinarySearchTree:

    class Leaf:
        def __init__(self, key, val, left=None, right=None):
            self.key = key
            self.val = val
            self.left = left
            self.right = right

        def getKey(self):
            return self.key

        def setKey(self, newKey):
            self.key = newKey

        def getLeft(self):
            return self.left

        def getRight(self):
            return self.right

        def setLeft(self, newLeft):
            self.left = newLeft

        def setRight(self, newRight):
            self.right = newRight

        def __iter__(self):
            if self.left != None:
                for leaf in self.left:
                    yield leaf

            yield self.key

            if self.right != None:
                for leaf in self.right:
                    yield leaf


    def __init__(self, root=None):
        self.root = root

    def insert(self, key, val):
        self.root = BinarySearchTree._insert(self.root, key, val)

    def _insert(root, key, val):
        if root == None:
            return BinarySearchTree.Leaf(key, val)

        if key < root.getKey():
            root.setLeft(BinarySearchTree._insert(root.getLeft(), key, val))
        else:
            root.setRight(BinarySearchTree._insert(root.getRight(), key, val))

        return root


    def find(self, key):
        return BinarySearchTree._find(self.root, key)

    def _find(root, key):
        if root is None:
            return None

        if key == root.getKey():
            return root.val

        if key < root.getKey():
            return BinarySearchTree._find(root.getLeft(), key)
        else:
            return BinarySearchTree._find(root.getRight(), key)

    def change(self, key, val):
        return BinarySearchTree._change(self.root, key, val)

    def _change(root, key, val):
        if root is None:
            return None

        if key == root.getKey():
            root.val = val
            return  root.val

        if key < root.getKey():
            return BinarySearchTree._change(root.getLeft(), key, val)
        else:
            return BinarySearchTree._change(root.getRight(), key, val)

    def __iter__(self):
        if self.root != None:
            return iter(self.root)
        else:
            return iter([])

