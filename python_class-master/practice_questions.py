# check if the iterable is empty - 0/int(), 0.0/float(), 0j/complex(), False/bool()
# ""/str(), []/list(), ()/tuple(), set(), {}/dict()

a = 10
# bool
# print(bool(a))      # a.__bool__() ==>  True
# print(dir(a))

s = ""
print(bool(s))      # s.__bool__() ==>   s.__len__()  False
# print(dir(s))
print(len(s))


if len(s) == 0:     # bool(len(s) == 0) ==> bool(False)
	print(False)
else:
	print(True)

if bool(s):         # bool(bool(s))
	print(True)
else:
	print(False)

value = []

if value:               # bool(value)
	print("not empty")
else:
	print("empty!!!")

#####################################################################################################
# greatest of 3 numbers

num1 = 17
num2 = 10
num3 = 30

if num1 > num2 and num1 > num3:         # 17 > 10 and 17 > 30
	print(f"{num1} is the greatest")

elif num2 > num3:       # 10 > 30
	print(f"{num2} is the greatest")

else:
	print(f"{num3} is the greatest")

######################################################################################################
# converting upper to lower and vice versa

char = "r"

# inbuilt method
if char.islower():
	print(char.upper())
else:
	print(char.lower())

# swapcase()
print(char.swapcase())

# without inbuilt method
char = "r"
print(ord(char))        # 114
print(ord("R"))         # 82

if 65 <= ord(char) <= 90:       # ord(char) in range(65, 91)
	print(chr(ord(char) + 32))

elif ord(char) in range(97, 123):
	print(chr(ord(char) - 32))


if "a" <= char <= "z":
	print(chr(ord(char) - 32))

elif "A" <= char <= "Z":
	print(chr(ord(char) + 32))

else:
	print("character is not an alphabet")

######################################################################################################
# check if entered character is vowel or not, if it is vowel then create a
# dictionary with char and its ascii value pair

char = "a"
d = {}

if char in "aeiouAEIOU":        # char.lower() in "aeiou":  char.upper() in "AEIOU"
	# d[key] = value
	d[char] = ord(char)
	print(d)

else:
	print("not a vowel")

#####################################################################################################
# check if the key is present, if present then increment or initialize the value to 1

d = {"a": 1, "b": 2, "c": 3}

key_to_search = "c"

if key_to_search in d:
	d[key_to_search] += 1

else:
	d[key_to_search] = 1

print(d)

###################################################################################################
# check if the given value is string or not

value = "10"

if isinstance(value, str):
	print("It is a string")
else:
	print("not a string")

##################################################################################################
# 9.	check whether the string is palindrome or not

string = "hello"

print(string == string[::-1])

###################################################################################################
# 10.	check if the integer is palindrome or not

num = 122

str_num = str(num)
print(str_num == str_num[::-1])

######################################################################################################
# 11.	check if the given year is leap year or not

import calendar
year = 1600
print(calendar.isleap(year))


if year % 4 == 0 and year % 100 != 0:       # non century year
	print("It is a leap year")

elif year % 400 == 0:      # century year
	print("It is a leap year")

else:
	print("It is not a leap year")

####################################################################################################
# check if the given character is number or alphabet or special character

string = " "

if string.isdigit():                    # "0" <= string <= "9"
	print("It is a number")

elif string.isalpha():                  # "a" <= string <= "z" or "A" <= string <= "Z"
	print("It is an alphabet")

else:
	print("It is a special symbol")

##################################################################################################
# check if the given number is perfect square or not

square_num = 16


for i in range(square_num):
	if i ** 2 == square_num:
		print("It is a perfect square")
		break


from math import sqrt

square_num = 15
square_root = int(sqrt(square_num))     # int(square_num ** 0.5)
print(square_root)      # 3

if square_root ** 2 == square_num:      # 3 ** 2 == 15
	print(True)
else:
	print(False)

#################################################################################################
# 15.	check if the given string is starting with vowel or not

string = "apple"
vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

print(string.startswith(vowels))

print(string[0] in "aeiouAEIOU")

#################################################################################################
# 18.	check the number of keys in the dictionary, if the number is even print the dictionary as it is
# , else add a new key to make it even and print it

d = {"a": 1, "b": 2, "c": 3}

if len(d) % 2 == 0:
	print(d)

else:
	d["e"] = 23
	print(d)

#####################################################################################################
# 19.	In a number check if the first digit is even or odd

num = 234

first_digit = int(str(num)[0])

print(first_digit % 2 == 0)


#############################################################################################

# 21.	Write a program to print prime numbers from 1 to 50

# num = 9
#
# for i in range(2, num // 2 + 1):        # (2, 6)
# 	if num % i == 0:        # 11 % 2 , 11 % 3, 11 % 4, 11 % 5
# 		print('not a prime number')
# 		break
#
# else:	        # executes only if the for loop executes without any break
# 	print("prime number")

# generate prime numbers

num = 1

for num in range(1, 51):
	if num > 1:
		for i in range(2, num//2 + 1):
			if num % i == 0:
				break

		else:
			print(num, end=", ")
print()

def isprime(num):
	if num > 1:
		for i in range(2, num//2 + 1):
			if num % i == 0:
				return False
		return True

def generate_prime_numbers():
	for num in range(1, 51):
		if isprime(num):
			print(num, end=", ")

generate_prime_numbers()
print()

#####################################################################################################
# Linear Search program

l = [1, 2, 3, 4, 5, 1]
value = 1

# print(value in l)

for num in l:
	if num == value:
		print(f"{value} is present at the index {l.index(num)}")
		break

else:
	print(f"{value} is not a member of the collection")


l = [1, 2, 3, 4, 5, 1]
value = 10
temp = False

for i in range(len(l)):
	if value == l[i]:
		print(f"value in present at index {i}")
		temp = True

if not temp:
	print("not present")

###################################################################################################

# 23.	Program to convert uppercase characters to lowercase characters in the string

name = "hello worl123d"
res = ""

for char in name:
	if "a" <= char <= "z":
		res = res + chr(ord(char) - 32)     # char.upper()

	elif "A" <= char <= "Z":
		res += chr(ord(char) + 32)

	else:
		res += char

# print(res)

#####################################################################################################
# 25.	Program to print only integer datatypes in the list
data = ["hi", "hello", 10, "12.3", 12, "90", 6.2]
res = []

for value in data:
	if isinstance(value, (int, float)):
		res.append(value)

print(res)

for value in data:
	if isinstance(value, str) and value.isdigit():
		print(value)

#####################################################################################################















