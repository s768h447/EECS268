#   Samuel Harrison 3/9/2022

def fibonacci(cmd, num):

    #   ith

    if cmd == '-i':

        #   checks for first two in sequence to stop going down

        if num <= 1:

            return num

        else:

            #   finds previous two and adds them

            return fibonacci('-i', num - 1) + fibonacci('-i', num - 2)

    elif cmd == '-v':

        #   verify


        if ((5 * num ** 2 + 4) ** 0.5) % 1 == 0 or 5 * ((5 * num ** 2 - 4) ** 0.5) % 1 == 0:

            #   uses fibonacci math to check if its in the sequence

            return f'{num} is in the Sequence'

        #   if the math failed, it will return here

        return f'{num} is Not in the Sequence'

    else:

        #   if all else fails, the user inputted incorrectly

        return 'Invalid Command'

while True:

    #   makes an infinite loop

    user = input('Input Mode and Integer: ').split(' ')

    #   checks for negatives preemptively for -i

    if int(user[1]) < 0:

        print('Invalid Integer')

    #   checks for 0 and 1 preemptively for -i

    elif int(user[1]) <= 1 and int(user[0] == '-i'):

        print(int(user[1]))

    else:

        #   calls fibonacci if conditions are met

        print(fibonacci(user[0], int(user[1])))
