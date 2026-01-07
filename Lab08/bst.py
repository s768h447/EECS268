#   Samuel Harrison 4/18/2022
from bnode import BNode

class BST:

    def __init__(self):

        self._root = None

    def __eq__(self, entry):

        return self._root == entry

    def __lt__(self, entry):

        return self._root > entry

    def __gt__(self, entry):

        return self._root < entry

    def _rec_add(self, entry, current_node):

        #   checks to see if entry is smaller than root
        if current_node.entry > entry:

            #   checks for left child's existence
            if current_node.left is None:

                current_node.left = BNode(entry)

            #   if subtree exists, recursion occurs with subtree
            else:

                self._rec_add(entry, current_node.left)

        #   checks to see if entry is bigger than root
        elif current_node.entry < entry:

            #   checks for right child's existence
            if current_node.right is None:

                current_node.right = BNode(entry)

            #   if subtree exists, recursion occurs with subtree
            else:

                self._rec_add(entry, current_node.right)

    def add(self, entry):

        #   if root does not exist, adds root
        if self._root is None:

            self._root = BNode(entry)

        #   checks for duplicates
        elif self._root.entry == entry:

            raise RuntimeError('No Duplicates')

        #   starts using hidden recursive method
        else:

            self._rec_add(entry, self._root)

    def search(self, key):

        #   calls hidden recursive method
        return self._rec_search(key, self._root)

    def _rec_search(self, key, root):

        #   returns when found
        if root.entry == key:

            print(key)

            return key

        #   checks if key is bigger than root
        elif key > root.entry:

            if root.right is not None:

                self._rec_search(key, root.right)

            else:

                raise RunTimError('Key Not Found')

        #   checks if key is smaller than root
        elif key < root.entry:

            if root.left is not None:

                self._rec_search(key, root.left)

            else:

                raise RunTimeError('Key Not Found')

    def print_in_order(self, root, order):

        if root:

            if order == 'pre':

                print(root.entry)

                self.print_in_order(root.left, order)

                self.print_in_order(root.right, order)

            elif order == 'in':

                print(root.left)

                self.print_in_order(root.left, order)

                print(root.entry)

                self.print_in_order(root.right, order)

            elif order == 'post':

                self.print_in_order(root.left, order)

                self.print_in_order(root.right, order)

                print(root.entry)

    def pre_order(self, root):

        if root:

            print(root.entry)

            self.pre_order(root.left)

            self.pre_order(root.right)

    def in_order(self, root):

        if root:

            self.in_order(root.left)

            print(root.entry)

            self.in_order(root.right)

    def post_order(self, root):

        if root:

            self.post_order(root.left)

            self.post_order(root.right)

            print(root.entry)


