# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', 
# then your program should print:
# Number of times bob occurs is: 2

total_of_bobs = 0
char_place = 0
    
for char in s:
    if char == 'b':
        if s[char_place - 1] == 'o' and char_place > 1:
            if s[char_place - 2] == 'b':
                total_of_bobs += 1
    char_place += 1

print('Number of times bob occurs is: ' + str(total_of_bobs))
