#   Samuel Harrison 3/9/2022

def outbreak(day):

    if day <= 1:

        #   checks for invalid days and day one then returns whichever

        return 6 if day == 1 else 'Invalid Day'

    elif day <= 3:

        #   checks for day one and two then returns whichever

        return 20 if day == 2 else 75

    else:

        #   returns the previous three days

        return outbreak(day - 1) + outbreak(day - 2) + outbreak(day - 3)

#   gets day, calls function with input, and prints number

print(outbreak(int(input('Input a Day: '))))