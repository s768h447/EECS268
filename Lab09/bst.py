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
        if current_node.entry[0] > entry[0]:

            #   checks for left child's existence
            if current_node.left is None:

                current_node.left = BNode(entry)

            #   if subtree exists, recursion occurs with subtree
            else:

                self._rec_add(entry, current_node.left)

        #   checks to see if entry is bigger than root
        elif current_node.entry[0] < entry[0]:

            #   checks for right child's existence
            if current_node.right is None:

                current_node.right = BNode(entry)

            #   if subtree exists, recursion occurs with subtree
            else:

                self._rec_add(entry, current_node.right)

        else:

            raise RunTimeError('No Duplicates')

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

        return self._rec_search(key, self._root)

    def _rec_search(self, key, root):

        #   returns when root
        if root.entry == key:

            print(f'{key[0]} {key[1]} {key[2]}')

            return key

        #   checks if key is bigger than root
        elif key[0] > root.entry[0]:

            if root.right is not None:

                self._rec_search(key, root.right)

            else:

                raise RuntimeError('Key Not Found')

        #   checks if key is smaller than root
        elif key[0] < root.entry[0]:

            if root.left is not None:

                self._rec_search(key, root.left)

            else:

                raise RuntimeError('Key Not Found')

    def print_tree(self, order):

        self._rec_print(self._root, order)

    def _rec_print(self, root, order):

        if root:

            if order == 'pre':

                print(root.entry)

                self._rec_print(root.left, order)

                self._rec_print(root.right, order)

            elif order == 'in':

                self._rec_print(root.left, order)

                print(root.entry)

                self._rec_print(root.right, order)

            elif order == 'post':

                self._rec_print(root.left, order)

                self._rec_print(root.right, order)

                print(root.entry)

    def remove(self, key):

        self._rec_remove(key, self._root)

    def _rec_remove(self, key, root):

        if root.entry == key:

            root.entry = [-1, key[1], key[2]]

        #   checks if key is smaller
        elif root.entry > key:

            self._rec_remove(key, root.left)

        #   checks if key is bigger
        elif root.entry < key:

            self._rec_remove(key, root.right)

        else:

            raise RunTimeError('Invalid Key')

        if root.entry[0] == -1:

            temp = []

            self._rec_fix(self._root, temp)

            [temp.remove(pokemon) for pokemon in temp if pokemon[0] == -1]

            self.empty()

            [self.add(pokemon) for pokemon in temp]

            self.print_tree('pre')

            return self._root

    def _rec_fix(self, root, temp):

        if root:

            temp.append(root.entry)

            self._rec_fix(root.left, temp)

            self._rec_fix(root.right, temp)

    def empty(self):

        self._root = None


