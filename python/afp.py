# This program MUST run under python folder

# function for getting unicode code for a given word
def sum_of_word(word):
    sum = 0 
    for char in word:
        sum += ord(char) - 96 # a starts with 97 but we need to def a as 1 so -96
    return sum

print(sum_of_word("latitude"))
print(sum_of_word("Latitude"))
print(sum_of_word("precision"))
print(sum_of_word("Preision"))

with open("result.txt", "w") as result: ## Generating result.txt as result
    with open("words_alpha.txt", "r") as file:
        for word in file.readlines():
            if sum_of_word(word.strip()) == 100:
                print(word)
                result.write(word) # Save results to the file, which lefts with 3700 or so