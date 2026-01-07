#Sam Harrison 1/26/2022

from executive import Executive

def main():

    #gets the file name with type and then calls executive

    input_file = open(input('Enter the name of the input file <name.type>: '), 'r')

    Executive.user_menu(input_file)

if __name__ == '__main__':

    main()

