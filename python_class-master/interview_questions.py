# ** Write a program to find the length of the string without using inbuilt function (len)**

def length(iterable):

	count = 0
	for _ in iterable:
		count += 1

	return count

# print(length("hello"))

# Write a program to reverse a string without using any inbuilt functions.
string = "hello"

# reversed(sequence) - str, list, tuple

result = reversed(string)       # result -> reversed object/ iterator object
# print(result)

# # type_casting
# print("".join(list(result)))
#
# result = reversed(string)
# # traverse
# for i in result:
# 	print(i, end="")
#
# print()
#
# # next()
# result = reversed(string)
# # print(dir(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))         # StopIteration

# # slicing
# print(string[::-1])

# # concatenation
# result = ""
#
# for char in string:
# 	result =  char + result
#
# print(result)

"""
char                    result
h                       "" + h          h
e                       e + h           eh
l                       l + eh          leh
l                       l + leh         lleh
o                       o + lleh        olleh

"""

#######################################################################################################
# Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe"

# replace()
s = "Hello World"

res = s.replace("World", "Universe")
# print(res)

# for loop
words = s.split()
res = ""
for word in words:
	if word == "World":
		res = res + "universe" + " "
	else:
		res = res + word + " "

# print(res)

#############################################################################################
# How to convert a string to a list and vice-versa.

s = "hello world"

# l = list(s)
# print(l)
# print("".join(l))
#
# l_words = s.split()
# print(l_words)
# print(" ".join(l_words))

######################################################################################################
# Covert the string "Hello welcome to Python" to a comma separated string.

# s = "Hello welcome to Python"
# print(s.replace(" ", ","))

######################################################################################################
# Write a program to print alternate characters in a string.
# print(s[::2])
# print(s[1::2])

#####################################################################################################
# Write a Program to print ascii values of the characters present in a string

# s = "Hello welcome to Python"
#
# for char in s:
# 	print(ord(char))

######################################################################################################
# Write program to convert upper case to lower case and vice-versa without using inbuilt method.


def swap_case(string):
	result = ""

	for char in string:
		if "a" <= char <= "z":
		# if ord(char) in range(ord("a"), ord("z")+1):
			result += chr(ord(char) - 32)

		elif "A" <= char <= "Z":
		# elif ord(char) in range(ord("A"), ord("Z")+1):
			result += chr(ord(char) + 32)

		else:
			result += char
	return result

# print(swap_case(string))

######################################################################################################
# Write program to swap two numbers without using 3rd variable.
a, b = 1, 2
a, b = b, a

##################################################################################################
# Write program to merge two different lists.

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

# # concatenation
# print(l1 + l2)
#
# # unpacking
# c = [*l1, *l2]
# print(c)

# # extends
# l1.extend(l2)
# print(l1)

# # chain
# from itertools import chain
# c = chain(l1, l2)
# print(list(c))

#####################################################################################################
# Write program to read a random line in a file. (ex. 50, 65, 78th line)
path = r"C:\Users\Vidyashree M C\python_class\files\sample.log"

def read_random_line(n):

	# with open(path) as file:
	# 	for line_no, line in enumerate(file, start=1):
	# 		if line_no == n:
	# 			print(line)
	# 			break

	# 	islice
	from itertools import islice
	with open(path) as file:
		lines = islice(file, n-1, n)
		print(list(lines))

# read_random_line(4)


# Write program to read a random lines in a file. (ex. I want read all lines 10th to 15th line)
from itertools import islice

def random_lines(start, end):

	with open(path) as file:
		# lines = islice(file, start-1, end)
		# for line in lines:
		# 	print(line)

		for line_no, line in enumerate(file, start=1):

			if line_no in range(start, end+1):
				print(line)

# random_lines(2, 5)

###################################################################################################
# Program to print last "N" lines of a file

def read_last_n_lines(n):

	# islice
	with open(path) as file:
		count = 0
		for _ in file:
			count += 1

		# print(file.tell())
		file.seek(0)
		# print(file.tell())

		lines = islice(file, count-n, count)

		for line in lines:
			print(line)


def read_last_n_lines(n):
	from collections import deque

	with open(path) as file:
		lines = deque(file, n)
		for line in lines:
			print(line)


# read_last_n_lines(3)

#######################################################################################################
#  Write a program to check if the given string is Palindrome or not without using reversed method

def is_palindrome(string):
	print(string[::-1] == string)

# is_palindrome("hello")

######################################################################################################
# Write a program to search for a character in a given string and return the corresponding index

def search(string, key):        # linear search

	for index, char in enumerate(string):
		if char == key:
			print(f"{char} is found at index {index}")
			break

	else:
		print("character is not found")


# search("hello", "x")

####################################################################################
# Write a program to get the below output**
sentence = "hello world welcome to python programming hi there"
# d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }

words = sentence.split()
d = {}

for word in words:
	key = word[0]
	if key in d:
		d[key].append(word)     # d[word[0]] = d[word[0]] + [word]
	else:
		d[key] = [word]

# print(d)

# default dictionary
from collections import defaultdict

dd = defaultdict(list)
words = sentence.split()

for word in words:
	dd[word[0]].append(word)        # dd[word[0]] = dd[word[0]] + [word]
									# dd["h"] = dd["h"] + [hello]
									#  dd["h"] = [] + [hello]

# print(dd)

#################################################################################
# Write a to replace all the characters with - if the character occurs more than once in a string
s = "hello world"
res = ""

for char in s:
	if s.count(char) > 1:
		res += "-"
	else:
		res += char

# print(res)

#####################################################################################
# write a decorator that returns only positive values of subtraction

def positive(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		return abs(result)
	return wrapper


@positive       # sub = positive(sub)
def sub(a, b):
	return a - b


# print(sub(1, 2))        # -1

##################################################################################
# How to get the count of number of instances of a class that is being created.

class Point:
	count = 0

	def __init__(self, a, b):
		self.a = a
		self.b = b
		Point.count += 1


p1 = Point(1, 2)        # __init__
p2 = Point(10, 20)
p3 = Point(3, 2)
p4 = Point(1, 7)

# print(Point.count)
"""
to access a class variable
1. self.class_var
2. className.class_var
3. self.__class__.class_var
"""
#####################################################################################################
# Write a function which takes a list of strings and integers.If the item is a string it should print
# as is and if the item is integer of float it should reverse it.

items = ["hello", 10, "hai", 1.2]


def spam(iterable):

	for item in iterable:
		if isinstance(item, (int, float)):
			print(str(item)[::-1])
		else:
			print(item)

# spam(items)

####################################################################################################
# Write a class named Simple and it should have iteration capability.

class Simple:

	def __init__(self, iterable):
		self.iterable = iterable

	def __iter__(self):     # returns iterator object
		return iter(self.iterable)


s = Simple([1, 2, 3, 4])
# print(dir(s))

# for item in s:
# 	print(item)

######################################################################################################
# # iterator protocol
#
# s = "hello"
#
# for char in s:
# 	print(char)

# x = iter(s)         # __iter__
# while True:
# 	try:
# 		char = next(x)      # __next__
#
# 	except StopIteration:
# 		break
#
# 	print(char)

#####################################################################################################
# iterator class

class Iterator:

	def __init__(self):
		self.start = 0
		self.end = 5

	def __iter__(self):
		return self

	def __next__(self):
		if self.start < self.end:
			self.start += 1
			return self.start
		raise StopIteration



# i = Iterator()
#
# for item in i:
# 	print(item)

####################################################################################################
# Write a Custom class which can access the values of dictionaries using d['a'] and d.a

class MyDict:

	def __init__(self, d):
		self.d = d

	def __getattribute__(self, item):
		if item == "a":
			return self.d["a"]
		elif item == "b":
			return self.d["b"]

		return super().__getattribute__(item)

	# def __getattribute__(self, item):
	# 	return self.d[item]


# m = MyDict({"a": 1, "b": 2})
# print(m.__dict__)
# print(m.a)
# print(m.b)


class MyDict:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __getitem__(self, item):
		if item == "a":
			return self.a
		elif item == "b":
			return self.b

		raise KeyError(f"{item} is not found")

# m = MyDict(1, 2)
# print(m.a)          # m.__getattribute__(a)
# print(m.b)          # m.__getattribute__(b)
#
# print(m["a"])           # m.__getitem__(a)
# print(m["b"])            # m.__getitem__(b)
# print(m["c"])            # m.__getitem__(b)
#####################################################################################################

class Sample:

	def __init__(self, d):
		self.d = d

	# invoked for all the attributes
	def __getattribute__(self, item):
		print("in getattribute")
		return super().__getattribute__(item)

	# invoked only for missing attributes
	def __getattr__(self, item):
		print("in getattr")

# s = Sample(10)
# print(s.e)


class MyDict:

	def __init__(self, d):
		self.d = d          # __setattr__

	def __getattribute__(self, item):
		print(f"checking for {item} in getattribute")
		return super().__getattribute__(item)

	def __getattr__(self, item):
		print(f"invoking get attr for {item}")
		return self.d[item]             # __getattribute__

	def __getitem__(self, item):
		return self.d[item]

	# def __setattr__(self, key, value):
	# 	print(f"setting {key} with value {value}")
	# 	if isinstance(value, dict):
	# 		super().__setattr__(key, value)
	# 	else:
	# 		raise TypeError("expecting a dictionary")



# m = MyDict({"a": 1, "b": 2})
# print(m.a)              # m.__getattribute__(a)
# print(m.b)              # m.__getattribute__(b)
# # print(m.c)
# print(m["a"])           # m.__getitem__(a)

# m.e = 10

#####################################################################################################
# Write a python program to get the below output**

sentence = "Hi How are you"
# o/p should be "iH woH era uoy"


words = [word[::-1] for word in sentence.split()]
# print(" ".join(words))

###############################################################################################
# Write a lambda function to add two numbers (a, b)

add = lambda a, b: a + b
# print(add(1, 2))

#####################################################################################################
# How to remove duplicates from the list without using inbuilt functions**
items = [1, 2, 3, 4, 1, 2, 3, 4, 5]

# set(items)

dup = []
for item in items:
	if item not in dup:
		dup.append(item)

# print(dup)

dup = []
for item in items:
	if items.count(item) == 1:
		dup.append(item)
# print(dup)

####################################################################################################
# Find the longest word in the sentence**
sentence = "Hello world. Welcome to Python"

# for loop
longest = ""

for word in sentence.split():
	if len(word) > len(longest):
		longest = word
# print(longest)

# sorted()
smallest, *rest, longest = sorted(sentence.split(), key=len)
# print(longest)

# max()
# print(max(sentence.split(), key=len))

######################################################################################################
# write a program to reverse the values in the dictionary if the value is of type String**
d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}

for key, value in d.items():
	if isinstance(value, str):
		d[key] = value[::-1]

# print(d)
###################################################################################################
# write a program to get 1234**
t = ('1', '2', '3', '4')
# print("".join(t))

####################################################################################################
# How to get the elements that are in list b but not in list a**
a = [1, 2, 3]
b = [1, 2, 3, 4]

# print(set(a) - set(b))
# print(set(b) - set(a))


if len(a) > len(b):
	longest, smallest = a, b
else:
	longest, smallest = b, a

l = []
for item in longest:
	if item not in smallest:
		l.append(item)

# print(l)

##################################################################################################
# A function takes variable number of positional arguments as input. How to check if the arguments
# that are passed are more than 5

def func(*args):
	if len(args) > 5:
		print("arguments are more than 5")
	else:
		print("arguments are less than 5")


# func(1, 2, 3, 4, 5, 6, 7)

#####################################################################################################
# Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.**
# Assume Below is the contents of the log file

lines = """CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical"""


split_lines = lines.split("\n")
# lines.splitlines()
# print(split_lines)

d = {}
for line in split_lines:
	message = line.split(":")[0]
	if message not in d:
		d[message] = 1
	else:
		d[message] += 1

# print(d)

dd = defaultdict(int)
for line in split_lines:
	message = line.split(":")[0]
	dd[message] += 1            # dd[message] = dd[message] + 1
													# 0 + 1

# print(dd)

###################################################################################################
# Write a function to reverse any iterable without using reverse function.**

a = [1, 2, 3, 4, 5]

def reverse_(iterable):
	return iterable[::-1]

#####################################################################################################
# Write a function to print the below output.**
# func("TRACXN", 0)  # Should print RCN
# func("TRACXN", 1)  # Should print TAX


def func(string, n):
	if n == 0:
		return string[1::2]
	elif n == 1:
		return string[::2]

# print(func("TRACXN", 0))
# print(func("TRACXN", 1))

################################################################################################
# Sum all the numbers in the below string.**
s = "Sony12India567Pvt2ltd"

sum_ = 0
for char in s:
	if char.isdigit():
		sum_ += int(char)

# print(sum_)

####################################################################################################
# Write a program to sum all the numbers in below string.**
s = "Sony12India567Pvt2ltd" # eg.12+567+2

# import re
# res = re.findall(r"\d+", s)
# print(res)


# result = ""
#
# for char in s:
# 	if char.isdigit():
# 		result += char
# 	else:
# 		result += " "
#
# sum_ = 0
# for num in result.split():
# 	sum_ += int(num)
#
# print(sum_)

####################################################################################################
# Print all the numbers in the below list**
a = ['abc', '123', 'hello', '23']

res = [item for item in a if item.isdigit()]
# print(res)

# Program to print the number of occurrences of characters in a String without using inbuilt functions.**
s = 'helloworld'

d = {}
for char in s:
	if char not in d:
		d[char] = 1
	else:
		d[char] += 1

# print(d)

# Program to print only the repeated characters and count of the same.**
s = 'helloworld'
d = {}
for char in s:
	if s.count(char) > 1:
		if char not in d:
			d[char] = 1
		else:
			d[char] += 1
# print(d)

# Write a program to get alternate characters of a string in list format.**
s = 'hello world welcome to python'
# print(list(s[::2]))


# Write a program to get square of list of number's using lambda function .**
a = [1, 2, 3, 4, 5]

square = lambda item: item ** 2

# print(list(map(square, a)))

# l = []
# for item in a:
# 	square_num = res(item)
# 	l.append(square_num)
# print(l)

# Write a program to iterate through list and build a new list, only if the items of the list has
# even number of characters.**
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']

res = [name for name in names if len(name) % 2 == 0]
# print(res)


# Write a program to iterate through list and build a new dictionary, only if the items of the list
# has even number of characters.**
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']

d = {name: len(name) for name in names if len(name) % 2 == 0}
# print(d)
#######################################################################################################
# Count number of lines in a file without loading the file to the memory

with open("practice_questions.txt") as file:
	count = 0
	for line in file:
		count += 1
	# print(count)

#####################################################################################################
# Printing line and line no's

# with open("practice_questions.txt") as file:
# 	for line_no, line in enumerate(file, start=1):
# 		print(line_no, line)

####################################################################################################
# Write a Program to print the sum of entire list and sum of only internal list**

l = [[1,2,3],[4,5,6],[7,8,9]]

internal_sum = [sum(item) for item in l]
# print(internal_sum)
# print(sum(internal_sum))

###################################################################################################
# Write a program to reverse the list as below**
words = ["hi", "hello", "python"]
# o/p ['nohtyp', 'olleh', 'ih']

res = [word[::-1] for word in words[::-1]]
# print(res)

###################################################################################################
# Write a program to update the tuple**
t1 = (1, 2, 3, 4)
t2 = (100, 200, 300)
# o/p (1, 2, 3, 4, 100, 200, 300)

t1 = t1 + t2
# print(id(t1))
# print(t1)

###################################################################################################
# Write a program to replace value present in nested dictionary.**
d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# Replace "nose" with "net"

for key, value in d.items():
	if isinstance(value, dict):
		for k, v in value.items():
			if v == "nose":
				value[k] = "net"

# print(d)

####################################################################################################
# Write a program to count the number of white spaces in a file.

with open("practice_questions.txt") as file:
	space_count = 0
	# for line in file:
		# space_count += line.count(" ")
	# print(space_count)

	for line in file:
		for char in line:
			if char == " ":
				space_count += 1
	# print(space_count)

#####################################################################################################
# 54 Grouping anagrams.**
words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']
anagrams = {}

for word in words:
	key = "".join(sorted(word))

	if key not in anagrams:
		anagrams[key] = [word]
	else:
		anagrams[key] += [word]

# print(anagrams)


# checking if 2 strings are anagrams
def is_anagram(s1, s2):
	return sorted(s1) == sorted(s2)

# print(is_anagram("fear", "fare"))

# [a, e, f, r]
# [a, r, f, r]

#####################################################################################################
d = {"a": 1, "b": 2}

# print(d["c"])
# print(d.get("c"))
# print(d.get("c", 10))
# print(d)

####################################################################################################
# Write a list comprehension to get a list of even numbers from 1-50

l = [num for num in range(1, 51) if num % 2 == 0]
# print(l)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums)

# even = lambda num: num % 2 == 0

def even(num):
	if num % 2 == 0:
		return num

# map
print(list(map(even, nums)))        # 10 elements

print(list(filter(even, nums)))

# default - 0, int(), 0.0, float(), False, bool(), 0j, complex(), "", [], (), {}, set(), None

# squares of even numbers
def square(num):
	if num % 2 == 0:
		return num ** 2
	# else:
	# 	return "odd"

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(list(map(square, nums)))
#
print(list(filter(square, nums)))


def add(a, b):
	return a + b


l1 = [1, 2, 3]
l2 = [13, 23, 31, 4]

# print(list(map(add, l1, l2)))

##################################################################################
# property

class Demo:

	def __init__(self, a):
		self.a = a

# 	getter - access the value of the attribute
	@property
	def a(self):
		return self._a

# setter
	@a.setter
	def a(self, value):
		if value < 0:
			raise ValueError("negative values are not allowed")
		self._a = value

# deleter
	@a.deleter
	def a(self):
		del self._a


# d = Demo(10)
# print(d.__dict__)
# print(Demo.__dict__)
# print(d.a)
# del d.a
# print(d.a)



