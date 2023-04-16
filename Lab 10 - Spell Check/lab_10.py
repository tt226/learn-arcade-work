import re


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


my_file = open("dictionary.txt")

# empty list to read the file dictionary
dictionary_text = []

# loop through each line
for line in my_file:
    # remove any carriage return or line feed or spaces
    for line in dictionary_text:
        line = line.strip(line)
        # add the words to the list
        dictionary_text.append(line)

my_file.close()


def linear_search():
    print("--- Linear Search ---")
    file_two = open("AliceInWonderLand200.txt")
    current_list_position = 0
    line_number = 0
    for line in file_two:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:
            pos = 0
            while current_list_position < len(dictionary_text) and word.upper() != dictionary_text[pos]:
                pos += 1
            if pos == len(dictionary_text):
                print("Line", line_number, "possible misspelled word:", word)
    file_two.close()


linear_search()

def binary_search():
    print("--- Binary Search ---")
    file_two = open("AliceInWonderLand200.txt")
    line_number = 0
    for line in file_two:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:
            lower_bound = 0
            upper_bound = len(dictionary_text) - 1
            found = False
            while lower_bound <= upper_bound and not found:
                middle_pos = (lower_bound + upper_bound) // 2
                if dictionary_text[middle_pos] < word.upper():
                    lower_bound = middle_pos + 1
                elif dictionary_text[middle_pos] > word.upper():
                    upper_bound = middle_pos - 1
                else:
                    found = True
            if not found:
                print("Line", line_number, "possible misspelled word:", word)
    file_two.close()


binary_search()
