import string


def run_game():
    first_word_return = first_word()
    print(create_first_word(first_word_return))
    print()
    second_word_return = second_word()
    print(create_second_word(second_word_return))
    print(return_indi_words())
    print(return_single_word())


"""get alphabet"""
alphabet = list(string.ascii_lowercase)
"""assign numerical value to each letter of the alphabet"""
alpha = dict()
for index, letter in enumerate(string.ascii_lowercase):
    alpha[letter] = index + 1

"""return a list of strings"""
two_words = "202315 4129238".split(" ")  # two which
# print(two_words)

three_words = "22120 71992222 231518419".split(" ")

sentance = "9 426137 2015 22137229 2085 141811 9142051814198916".split(" ")

"""select the item of the first and second index and make each str an item in its own list"""
word_one = list(two_words[0])
# print(word_one)
word_two = list(two_words[1])
# print(word_two)


def return_indi_words():
    three_words_list = []
    for i in three_words:
        three_words_list.append(list(i))
    return three_words_list


the_list_of_three_words = return_indi_words()


def return_single_word():
    double_letter_group = []
    for i in the_list_of_three_words:
        double_letter_group.append([i[j : j + 2] for j in range(0, len(i), 2)])
    return double_letter_group


final_three_word_list = return_single_word()

"""list comprehension: iterate through list and create a new list of items of length 2 i.e. instead of ['2', '0', ...] it is [['2', '0'], ...] """
word_one_group = [word_one[i : i + 2] for i in range(0, len(word_one), 2)]
print(word_one_group)
word_two_group = [word_two[i : i + 2] for i in range(0, len(word_two), 2)]
word_two_group = (
    [word_two[i : i + 2] for i in range(0, len(word_two) - 1, 2)] + [word_two[-1]]
    if len(word_two) % 2 != 0
    else [word_two[i : i + 2] for i in range(0, len(word_two), 2)]
)


# print(word_two_group)


def third_word():
    counter = 0
    words_list = []
    for i in final_three_word_list:
        for j in i:
            j = "".join(i[counter])
            words_list.append(j)
            counter += 1
    return words_list


def create_first_word(word_one_list):
    the_first_word = []
    single_letters = []

    for data_item in word_one_list:
        for key, values in alpha.items():
            if values == int(data_item):
                the_first_word.append(key)

    for data_item in word_one:
        for key, values in alpha.items():
            if values == int(data_item):
                single_letters.append(key)


"""joins the items of the smaller list to create a single int value i.e. [['2','0'], ...] becomes ['20',...]"""


def first_word():
    counter = 0
    word_one_list = []
    for i in word_one_group:
        i = "".join(word_one_group[counter])
        word_one_list.append(i)
        counter += 1
    return word_one_list


def create_first_word(word_one_list):
    the_first_word = []
    single_letters = []

    for data_item in word_one_list:
        for key, values in alpha.items():
            if values == int(data_item):
                the_first_word.append(key)

    for data_item in word_one:
        for key, values in alpha.items():
            if values == int(data_item):
                single_letters.append(key)

    result_string_single = "".join(the_first_word)
    result_string_double = "".join(single_letters)
    result_string = result_string_single + " " + result_string_double
    return result_string


"""joins the items of the smaller list to create a single int value i.e. [['2','0'], ...] becomes ['20',...]"""


def second_word():
    counter = 0
    word_two_list = []
    for i in word_two_group:
        i = "".join(word_two_group[counter])
        word_two_list.append(i)
        counter += 1
    return word_two_list


def create_second_word(word_two_list):
    the_second_word = []
    single_letters = []

    for data_item in word_two_list:
        for key, values in alpha.items():
            if values == int(data_item):
                the_second_word.append(key)

    for data_item in word_two:
        for key, values in alpha.items():
            if values == int(data_item):
                single_letters.append(key)

    result_string_single = "".join(the_second_word)
    result_string_double = "".join(single_letters)
    result_string = result_string_single + " " + result_string_double
    return result_string


if __name__ == "__main__":
    run_game()
