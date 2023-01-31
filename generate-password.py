import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

how_many_letters = int(input("How many letters?: "))
how_many_numbers = int(input("How many numbers?: "))
how_many_symbols = int(input("How many symbols?: "))

letters_count = 1
numbers_count = 1
symbols_count = 1
character_count = 0
password_total_characters = how_many_letters+how_many_numbers+how_many_symbols
password = ""

#version 1

while character_count != password_total_characters:
    character = random.randint(1, 3)

    if character == 1 and letters_count <= how_many_letters:
        password += random.choice(letters)
        letters_count += 1
        character_count += 1
    elif character == 2 and numbers_count <= how_many_numbers:
        password += random.choice(numbers)
        numbers_count += 1
        character_count += 1
    elif character == 3 and symbols_count <= how_many_symbols:
        password += random.choice(symbols)
        symbols_count += 1
        character_count += 1

print(f"version 1\nYour password is: {password}")

#version 2

my_password_list = []

for letter_count in range(1, how_many_letters):
    my_password_list.append(random.choice(letters))

for number_count in range(1, how_many_numbers):
    my_password_list.append(random.choice(numbers))

for symbol_count in range(1, how_many_symbols):
    my_password_list.append(random.choice(symbols))

print(my_password_list)

random.shuffle(my_password_list)

print(my_password_list)

my_password = ""

for char in my_password_list:
    my_password += char

print(f"Version 2\nYour password is: {my_password}")