'''
Character Access and Counting
Task: Given the string word = "Programming", perform the following:
 1. Print the first character of the string.
 2. Print the last character of the string.
 3. Print the length of the string.
Example Code:
word = "Programming"
first_char = word[0]
last_char = word[-1]
length_of_word = len(word)
print("First Character:", first_char)
print("Last Character:", last_char)
print("Length of the Word:", length_of_word)
'''
word = 'Programming'
# Printing first character of word
first_char=word[0]
# print(word[0])
# Print the last character of the string.
last_char=word[-1]
# print(word[-1])
# Print the length of the string.
length=len(word)

print('First character is ' +first_char)
print('Last character is ' +last_char)
print('Length of the Word is {}'.format(length))