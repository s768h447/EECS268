#   Samuel Harrison 3/9/2022

def power_func(b, e):

    #   checks if the exponential is 0 or b is 1, if so, returns 1

    if e == 0 or b == 1:

        return 1

    #   a quick check that makes sure the user has not inputted a negative exponential

    elif e < 0:

        return 'Exponential integer must be greater than or equal to zero.'

    #   multiplies the base by the base and then decreases the exponential count

    else:

        return b * power_func(b, e - 1)


while True:

    #   uses an infinite loop and takes two integers from the user

    base = int(input('Input a base integer: '))

    exponential = int(input('Input a positive exponential integer: '))

    print(power_func(base, exponential))