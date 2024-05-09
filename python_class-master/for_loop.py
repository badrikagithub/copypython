from collections import defaultdict, Counter
from time import sleep
from itertools import zip_longest
from sorting import *


# 12.	Find the sum of first 10 even numbers

num = 0
count = 1
sum_ = 0


while count <= 10:
	if num % 2 == 0:
		print(num, end=" ")
		sum_ += num
		count += 1

	num += 1

print()
# print(sum_)

##################################################################################
# 13.	Iterating over string using range function.
s = "hello world"

for char in s:
	print(char, end=" ")

print()
for index in range(len(s)):
	print(s[index], end=" ")

print()

###################################################################################
# 14.	iterating over a string in reversed direction

s = "hello world"

for char in s[::-1]:
	print(char, end=" ")

print()
for index in range(len(s)-1, -1, -1):
	print(s[index], end=" ")

print()
for char in reversed(s):        # reversed - inbuilt classes
	print(char, end=" ")

###################################################################################
# 15.	Printing Index and Character using range function
print()
for index in range(len(s)):
	print(index, s[index])

for index, item in enumerate(s):
	print(index, item)

###################################################################################
# 16.	Iterating over multiple string objects using zip class

s1 = "hello"
s2 = "hai"

for item1, item2 in zip(s1, s2):
	print(item1, item2)

# zip_longest

from itertools import zip_longest

for item1, item2 in zip_longest(s1, s2, fillvalue="zz"):
	print(item1, item2)

###################################################################################
# 17.	Printing alternate characters of the string

for index in range(0, len(s), 2):
	print(s[index])


for char in s[::2]:
	print(char)

###################################################################################
# 24.	Program to print filenames ending with pdf.
files = ['youtube.txt', 'amazon.pdf', 'facebook.pdf', 'google.pdf', 'apple.doc']

for file in files:      # youtube.txt
	f_name, extension = file.split(".")     # [youtube, txt]
	if extension == "pdf":
		print(file)

###################################################################################
l = []
for file in files:
	l.append((file, len(file)))

print(l)

###################################################################################
# printing keys

d = {"a": 1, "b": 2, "c": 3}

for item in d:
	print(item)

for value in d.values():
	print(value)

for key in d:
	print(d[key])

for key, value in d.items():
	print(key, value)

for index, item in enumerate(d.items()):
	print(index, item)

# deep unpacking
for index, (key, value) in enumerate(d.items()):
	print(key, value, index)

##################################################################################
# create dictionary of word and count pair using get method

sentence = 'hello world hello world welcome to python'
d = {}
words = sentence.split()

for word in words:
	if word not in d:
		d[word] = 1
	else:
		d[word] = d[word] + 1

print(d)

d = {}
# print(d["a"])
print(d.get("a", 0))

sentence = 'hello world hello world welcome to python'
words = sentence.split()

for word in words:
	d[word] = d.get(word, 0) + 1

print(d)

"""
hello hello world

d       {hello: 2, world: 1}

"""

##################################################################################
# 32.	Counting number of characters in a string
s = 'abracadabraca'

d = {}
for char in s:
	if char not in d:
		d[char] = 1
	else:
		d[char] = d[char] + 1

print(d)

# default dictionary

d = defaultdict(int)

for char in s:
	d[char] += 1

print(d)

# get method

d = {}

for char in s:
	d[char] = d.get(char, 0) + 1
print(d)

# Counter

c = Counter(s)
print(c)                # dictionary
print(c.most_common())      # list of tuples
print(c.most_common(3))      # list of tuples

sentence = 'hello world hello world welcome to python'

words = sentence.split()
print(Counter(words))
print(Counter(sentence))
print(Counter(list(sentence)))

#################################################################################
# 36.	Create a dictionary for the below list

cities = [('India', 'Bangalore'),
('India', 'Chennai'),
('India', 'Delhi'),
('India', 'Kolkata'),
('USA', 'Dallas'),
('USA', 'New York'),
('USA', 'Chicago'),
('China', 'Beijing'),
('China', 'Shainghai')
]

print(dict(a=1, b=3))
print(dict({1: 2, 3: 4}))
print(dict([('a', 6), ('b', 2), ('r', 2), ('c', 2), ('d', 1)]))
print(dict(cities))

d = defaultdict(list)

for country, city in cities:
	d[country] += [city]

print(d)

##################################################################################
# 38.	flattening the list using Multiple for loops in comprehension

items = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

l = [num for item in items for num in item]
# print(l)

###################################################################################
# 39.	Python Program for n-th Fibonacci number

a, b = 0, 1
n = 10


for i in range(n-1):
	print(a, end=", ")
	a, b = b, a + b

print()
print(a)

##################################################################################
# 40.	Python Program for Sum of squares of first n natural numbers

print(sum([num ** 2 for num in range(10)]))

