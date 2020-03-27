# This program MUST run under python folder

# function for getting unicode code for a given word
def sum_of_word(word):
    sum = 0 
    for char in word:
        sun += ord(char) - 96 # a starts with 97 but we need to def a as 1 so -96
    return sum

with open("words_alpha.txt", "r") as file:
    for word in file.readlines():
        if sum_of_word(word) == 100:
            print(word)