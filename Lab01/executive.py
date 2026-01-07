#Sam Harrison 1/26/2022

from boardgame import BoardGame

class Executive:

    def user_menu(file):

        #prints a menu

        user_choice = int(input('Choose an Option:\n1) Print All Games:\n2) Print Games from a Year\n3) Print Ranking Range\n4) People VS Gibbons\n5) Print Play Time\n6) Exit\n'))

        #simply prints all of the games after putting in class

        if user_choice == 1:

            for game in file:

                game = game.strip('\n').split('\t')

                game = BoardGame(game[0], game[1], game[2], game[3], game[4], game[5])

                print(game)

        elif user_choice == 2:

            user_year = int(input("Input a Year: "))

            for game in file:

                game = game.strip('\n').split('\t')

                game = BoardGame(game[0], game[1], game[2], game[3], game[4], game[5])

                #uses inputted year to find matches

                if int(game.year_published) == user_year:

                    print(game)

        #   takes two numbers from user then splits them in a list

        elif user_choice == 3:

            user_range = (input('Input a Ranking Range <lower_num higher_num> separated by a space: ')).split(' ')

            #checks if either number is out of range

            if int(user_range[0]) < 0 or int(user_range[0]) > 10 or int(user_range[1]) < 0 or int(user_range[1]) > 10:

                print('Invalid Number')

            else:

                for game in file:

                    #turns it into the BoardGame class and then puts it through the range

                    game = game.strip('\n').split('\t')

                    game = BoardGame(game[0], game[1], game[2], game[3], game[4], game[5])

                    if float(game.gibbons_rating) in range(int(user_range[0]), int(user_range[1])):

                        print(game)

        elif user_choice == 4:

            user_number = float(input('Input a Number: '))

            for game in file:

                #turns it into the BoardGame class

                game = game.strip('\n').split('\t')

                game = BoardGame(game[0], game[1], game[2], game[3], game[4], game[5])

                #takes the difference of both reviews and checks if the inputted number is out of range

                if user_number <= float(game.gibbons_rating) - float(game.peoples_rating):

                    print(game)

        elif user_choice == 5:

            #checks time inputted by user and then checks game file for matches with less than or equal to

            user_time = float(input('Input a Number: '))

            for game in file:

                game = game.strip('\n').split('\t')

                game = BoardGame(game[0], game[1], game[2], game[3], game[4], game[5])

                #turns game into the BoardGame class and then checks it against the inputted time

                if user_time >= float(game.min_playtime):

                    print(game)

        elif user_choice == 6:

            #does nothing but ends program

            print('Program Ended')


