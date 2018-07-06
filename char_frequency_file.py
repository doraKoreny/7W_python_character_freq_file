"""Write a procedure char_freq_table() that when running in a terminal,
 accepts a file name from the user, builds a frequency listing of the
  characters contained in the file to a Python dictionary,
 and prints a sorted and nicely formatted character frequency table to the screen."""
from char_frequency_console import char_freq
import sys


def make_string_from_file(file_name):
    with open(file_name) as my_file:
        my_file = my_file.readlines()
        all_lines = ""
        for item in my_file:
            all_lines += item
        return all_lines


def get_freq_char(letters):
    for char in letters:
        frequency_characters = char_freq(letters)
    freq_char_list = []
    for k, v in frequency_characters.items():
        temp = [k, v]
        freq_char_list.append(temp)
    freq_char_list.sort()
    return freq_char_list


def char_freq_table():
    user_file = "/home/dorello/codecool/Python/7th SI/Notes/char/text_for_hapax.txt"
    my_file_in_string = make_string_from_file(user_file)
    freq_char_list = get_freq_char(my_file_in_string)
    for i in range(len(freq_char_list)):
        letter = freq_char_list[i][0]
        quantity = str(freq_char_list[i][1])
        table = letter + ": " + quantity
        print(table)


char_freq_table()
