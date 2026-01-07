#Samuel Harrison 2/2/2022

def build_count(file):

    #   defines a list to use

    word_list = []

    #   takes each line in the file and splits it by space

    for line in file:

        line = line.split(' ')

        #   takes each word in the line in list form and then sends it to the clean_word function and then appends

        for word in line:

            word_list.append(clean_word(word))

    #   makes a dictionary to use

    word_dict = {}

    #   if the word is already in the dictionary, it counts

    for word in word_list:

        if word in word_dict:

            word_dict[word] += 1

        #   if not, it sets it to 1, then returns

        else:

            word_dict[word] = 1

    return word_dict

def clean_word(word):

    #   takes the word through a gauntlet of lower, then replaces, and then strips to clean up

    word = word.lower()

    word = word.replace('.', '')
    word = word.replace(',', '')
    word = word.replace(';', '')
    word = word.replace(':', '')
    word = word.replace('!', '')
    word = word.replace('?', '')
    word = word.replace('|', '')
    word = word.replace('--', '')
    word = word.strip("'")

    word = word.strip('\n\t')

    return word

def unique_words(file):

    #   defines a list to use

    word_list = []

    #   takes each line in the file and splits it by space

    for line in file:

        line = line.split(' ')

        #   takes each word in the line in list form and then sends it to the clean_word function and then appends

        for word in line:

            word = clean_word(word)

            if word not in word_list:

                word_list.append(word)

    return word_list

def main():

    #   just says welcome

    print('Welcome!\n'.center(16))

    #   gets the input file from user

    input_file = open(input('Enter input file using the format <name.type>: '), 'r')

    #   word_data will contain all words and corresponding counts

    word_data = open('word_data.txt', 'a')

    #   unique_data will contain only words appearing once

    unique_data = open('unique_words.txt', 'a')

    #   uses previous made functions to get the dictionary

    word_dict = build_count(input_file)

    for word in word_dict:

        #   for each key in the dictionary, it writes a formatted fstring of the key then number value

        word_data.write(f'{word}: {word_dict[word]}\n')

        if word_dict[word] == 1:

            #   does the same as above but also writes values equal to one in the unique_data file

            unique_data.write(f'{word}\n')

#   starts function main

if __name__ == '__main__':

    main()