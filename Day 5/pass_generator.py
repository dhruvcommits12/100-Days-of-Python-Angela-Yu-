import string
import random

letters = list(string.ascii_lowercase)
numbers=list(string.digits)
symbols = ['!','$','#','%','*','&','(',')','+']

print("Welcome to the Pypassword generator")
n_letters=int(input("How many letters do you want in your password:"))
n_numbers=int(input("How many numbers do you want in your password:"))
n_symbols=int(input("How many symbols do you want in your password:"))

#Easy version 

# password=" "

# for num in range(0,4):
#     password+=random.choice(letters)

# for num in range(0,4):
#     password+=random.choice(numbers)

# for num in range(0,4):
#     password+=random.choice(symbols)

# print(password)

#Hard version

password_list = []
password = " "

for num in range(0,4):
    password_list.append(random.choice(letters))

for num in range(0,4):
    password_list.append(random.choice(numbers))

for num in range(0,4):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

for char in password_list:
    password+=char

print(password)









