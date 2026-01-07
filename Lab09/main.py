#   Samuel Harrison 4/18/2022
from bst import BST

#   gets pokemon data from user
def pokemon_list():

    data = input('Input Pokedex Number, US Name, and JP Name Separated by Spaces: ').split(' ')

    #   returns as a list
    return int(data[0]), data[1], data[2]

def main():

    #   initializes everything
    tree = BST()

    copy = False

    #tree.add((8, 'a', 'a'))

    #tree.add((2, 'b', 'b'))

    #tree.add((10, 'c', 'c'))

    #tree.add((6, 'd', 'd'))

    #tree.add((7, 'e', 'e'))

    #tree.add((9, 'f', 'f'))

    command = input('Add file (y/n)?: ').lower()

    if command == 'y':

        command = input('Input File Name: ')

        with open(f'{command}.txt', 'r') as file:

            [tree.add(''.join(line).strip('\n').split('\t')) for line in file]

    while True:

        #   gets user input
        command = input('Input Command: ').lower()

        if command == 'add':

            pokemon = pokemon_list()

            #   checks for copy
            if copy is False:

                tree.add(pokemon)

            else:

                #   gets user input
                subcommand = input('Original or Copy: ').lower()

                #   adds to original or copy tree
                if subcommand == 'original':

                    tree.add(pokemon)

                elif subcommand == 'copy':

                    copy.add(pokemon)

        elif command == 'search':

            pokemon = pokemon_list()

            if copy is False:

                tree.search(pokemon)

            else:

                #   gets user input
                subcommand = input('Original or Copy: ').lower()

                #   adds to original or copy tree
                if subcommand == 'original':

                    tree.search(pokemon)

                elif subcommand == 'copy':

                    copy.search(pokemon)

        elif command == 'print':

            order = input('Input Traversal Order (Pre, In, Post): ').lower()

            if copy is False:

                #   orders: VLR, LVR, LRV
                if order in {'pre', 'in', 'post'}:

                    tree.print_tree(order)

            else:

                subcommand = input('Original or Copy?: ').lower()

                if subcommand == 'original':

                    #   orders: VLR, LVR, LRV
                    if order in {'pre', 'in', 'post'}:

                        tree.print_tree(order)

                elif subcommand == 'copy':

                    if order in {'pre', 'in', 'post'}:

                        copy.print_tree(order)

        elif command == 'copy':

            if copy is True:

                print('Already Copied')

            else:

                copy = tree

                print('Tree Copied')

        elif command == 'remove':

            if copy is False:

                test = 8, 'a', 'a'

                tree.remove(test)

        elif command == 'quit':

            break

if __name__ == '__main__':

    main()