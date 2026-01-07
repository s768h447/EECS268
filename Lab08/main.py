#   Samuel Harrison 4/18/2022
from bst import BST

#   gets pokemon data from user
def pokeget():

    us_name = input('Input US Name: ')

    jp_name = input('Input JP Name: ')

    pokedex = int(input('Input Pokedex Number: '))

    return us_name, jp_name, pokedex

def main():

    #   initializes class
    tree = BST()

    root = None

    while True:

        command = input('Input Command: ').lower()

        if command == 'search':

            #   uses pokeget to get pokemon data
            tree.search(pokeget())

        elif command == 'add':

            if root == None:

                #   uses pokeget to get pokemon data
                tree.add(pokeget())

            else:

                tree.add(pokeget())

        elif command == 'print':

            #   obtains traversal order
            subcommand = input('Input Traversal Order (Pre, In, Post): ').lower()

            #   orders: VLR, LVR, LRV
            if subcommand in {'pre', 'in', 'post'}:

                tree.print_in_order(tree._root, subcommand)

        elif command == 'quit':

            break

if '__name__' == main():

    main()