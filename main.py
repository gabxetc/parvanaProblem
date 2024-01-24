import string


def run_game():
    print(create_two_words())
    print(create_three_word())
    print(create_the_sentence())


alphabet = list(string.ascii_lowercase)
alpha = dict()
for index, letter in enumerate(string.ascii_lowercase):
    alpha[letter] = index + 1

"""------------------------------------------------------------------------------------------------------------------------"""
two_words = "202315 4129238".split(" ")  # two which


def return_two_words():
    two_words_list = []
    for i in two_words:
        two_words_list.append(list(i))
    return two_words_list


the_list_of_two_words = return_two_words()


def return_single_word_of_two():
    double_letter_group = []
    for i in the_list_of_two_words:
        double_letter_group.append([i[j : j + 2] for j in range(0, len(i), 2)])
    return double_letter_group


final_two_word_list = return_single_word_of_two()


def the_two_words():
    word_one_list = []
    for i in final_two_word_list:
        counter = 0
        for j in i:
            j = "".join(i[counter])
            if int(j) > 26:
                k = [word_one_list.append(int(char)) for char in j]
            else:
                word_one_list.append(int(j))
            counter += 1
    return word_one_list


two_words_final = the_two_words()


def create_two_words():
    the_final_words = []
    for data_item in two_words_final:
        for key, values in alpha.items():
            if values == int(data_item):
                the_final_words.append(key)

    result_string_single = "".join(the_final_words)
    return result_string_single


"""------------------------------------------------------------------------------------------------------------------------"""
three_words = "22120 71992222 231518419".split(" ")  # vlgaiivvwordai


def return_three_words():
    three_words_list = []
    for i in three_words:
        three_words_list.append(list(i))
    return three_words_list


the_list_of_three_words = return_three_words()


def return_single_word_of_three():
    double_letter_group = []
    for i in the_list_of_three_words:
        double_letter_group.append([i[j : j + 2] for j in range(0, len(i), 2)])
    return double_letter_group


final_three_word_list = return_single_word_of_three()


def the_three_words():
    three_words_list = []
    for i in final_three_word_list:
        counter = 0
        for j in i:
            j = "".join(i[counter])
            if int(j) > 26:
                k = [three_words_list.append(int(char)) for char in j]
            else:
                three_words_list.append(int(j))
            counter += 1
    return three_words_list


three_words_final = the_three_words()


def create_three_word():
    the_final_words = []
    for data_item in three_words_final:
        for key, values in alpha.items():
            if values == int(data_item):
                the_final_words.append(key)

    result_string_single = "".join(the_final_words)
    return result_string_single


"""------------------------------------------------------------------------------------------------------------------------"""

sentance = "9 426137 2015 22137229 2085 141811 9142051814198916".split(" ")


def return_sentence_words():
    sentence_words_list = []
    for i in sentance:
        sentence_words_list.append(list(i))
    return sentence_words_list


the_sentence_list = return_sentence_words()


def return_sentence():
    double_letter_group = []
    for i in the_sentence_list:
        double_letter_group.append([i[j : j + 2] for j in range(0, len(i), 2)])
    return double_letter_group


final_sentence_list = return_sentence()


def the_sentence_words():
    the_sentence_list = []
    for i in final_sentence_list:
        counter = 0
        for j in i:
            j = "".join(i[counter])
            if int(j) > 26:
                k = [the_sentence_list.append(int(char)) for char in j]
            else:
                the_sentence_list.append(int(j))
            counter += 1
    return the_sentence_list


the_sentence_final = the_sentence_words()


def create_the_sentence():
    the_sentence_words = []
    for data_item in the_sentence_final:
        for key, values in alpha.items():
            if values == int(data_item):
                the_sentence_words.append(key)

    result_string_single = "".join(the_sentence_words)
    return result_string_single


if __name__ == "__main__":
    run_game()
