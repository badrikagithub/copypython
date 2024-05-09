numbers = [4, 8, 1, 3, 9, 4, 6]
string = "hello"

print(numbers.sort())
print(numbers.sort(reverse=True))
print(numbers)
# string.sort()

# sorted(iterable) -> list
print(sorted(numbers))
print(numbers)

print(sorted(string))

#################################################################################
# default sorting

# string
string = "hello"

res = sorted(string)        # based on Ascii value in ascending order
print(res)

print(sorted(string, reverse=True)) # based on Ascii value in descending order

# list
numbers = [4, 8, 1, 3, 9, 4, 6]

print(sorted(numbers))
print(sorted(numbers, reverse=True))

names = ["steve", "John", "eve", "hannah", "alex", "joe"]
print(sorted(names))

# tuple
numbers = (4, 8, 1, 3, 9, 4, 6)

print(sorted(numbers))
print(sorted(numbers, reverse=True))

names = ("steve", "john", "eve", "hannah", "alex", "joe")
print(sorted(names))

# set
numbers = {4, 8, 1, 3, 9, 4, 6}
print(sorted(numbers))

# dictionary
d = {2: 10, 4: 7, 3: 8, 9: 12, 7: 3}

print(sorted(d))            # list of sorted keys
print(sorted(d.keys()))            # list of sorted keys
print(sorted(d.values()))   # list of sorted values

print(d.items())
print(sorted(d.items()))    # list of tuples sorted based on keys

##################################################################################
# custom sorting

names = ["steve", "joe", "John", "eve", "hannah", "alex"]

# sort based on length of each name
def length(item):
	return len(item)

print(sorted(names, key=length))

print(sorted(names, key=len))


length_ = lambda item: len(item)
print(sorted(names, key=length_))

print(sorted(names, key=lambda item: len(item)))

# sort names based on last character
def last_char(word):
	return word[-1]

print(sorted(names, key=last_char))

last_char = lambda word: word[-1]
print(sorted(names, key=last_char))

# dictionary
prices = {"mobile": 1000, "laptop": 1238, "tablet": 700, "television": 1500}

# sorting keys
print(sorted(prices))
print(sorted(prices.keys()))

# sorting values
print(sorted(prices.values()))

# sorting both key-value
print(sorted(prices.items()))

print(prices.items())
# [('mobile', 1000), ('laptop', 1238), ('tablet', 700), ('television', 1500)]

# sorting based on values
def get_values(item):       # ('mobile', 1000)
	return item[1]

print(sorted(prices.items(), key=get_values))
print(sorted(prices.items(), key=lambda item: item[-1]))

# sort based on last character of key
prices = {"mobile": 1000, "laptop": 1238, "tablet": 700, "television": 1500}

def last_key_char(item):    # ("mobile", 1000)
	return item[0][-1]

print(sorted(prices.items(), key=last_key_char))
print(sorted(prices.items(), key=lambda item: item[0][-1]))

# sort the dictionary based on length of the key
places = {"mysore": "Karnataka", "pune": "Maharashtra", 'cochin': "Kerala"}

def key_len(item):
	return len(item[0])

print(sorted(places.items(), key=key_len))

# sort the dictionary based on length of the value

def key_len(item):
	return len(item[1])

print(sorted(places.items(), key=key_len))

# sort the dictionary based on last character of value

def last_char_value(item):
	return item[1][-1]

print(sorted(places.items(), key=last_char_value))

# sort the dictionary based on first character of value
def first_char_value(item):
	return item[1][0]

print(sorted(places.items(), key=last_char_value))

# sort the dictionary based on first character of key
print(sorted(places.items()))

##################################################################################

numbers = [4, 8, 1, 3, 9, 4, 6]

# maximum value

max_value = numbers[0]

for num in numbers:
	if max_value < num:
		max_value = num

print(max_value)

# bubble sort technique
numbers = [4, 8, 1, 3, 9, 6]

for n in range(len(numbers)-1):       # 6
	for i in range(len(numbers)-1): # 5
		if numbers[i] > numbers[i+1]:
			numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
print(numbers[0], numbers[-1])

print(numbers)

min_, *c, max_ = numbers
print(max_, min_)
print(c)

#######################################################
min_, *rest, max_ = sorted(numbers)
print(min_, max_)

#########################################################
numbers = [4, 8, 9, 1, 3, 9, 6]
print(max(numbers))
print(min(numbers))
print(sum(numbers))


names = ["steve", "John", "eve", "hannah", "alex", "joe"]
print(max(names, key=lambda item: len(item)))
print(max(names, key=len))
print(min(names, key=len))

###############################################################################
# find the longest and smallest word in the sentence
sentence = "python is a programming language and programming is fun"

smallest, *rest, longest = sorted(sentence.split(), key=len)
print(smallest, longest)


# find the longest non repeated word in the sentence
sentence = "python is a programming language and programming is fun"
words = sentence.split()

l = []
for word in words:
	if words.count(word) == 1:
		l.append(word)

print(max(l, key=len))


# find all the longest words in the sentence
sentence = "hello world today is a good day"
words = sentence.split()

longest = max(words)

for word in words:
	if len(longest) == len(word):
		print(word)


################################################################################

# anagrams : fare and fear, silent and listen, dear and dare

word1 = "fare"      # sorted(word1) = [a, e, f, r]
word2 = "fearr"      # sorted(word2) = [a, e, f, r]

def is_anagram(word1, word2):
	return sorted(word1) == sorted(word2)

# print(is_anagram("fare", "fearr"))

#################################################################################
# grouping anagrams -> dictionry

words = ["eat", "dear", "fear", "fare", "listen", "silent", "ate", "tea", "dare", "read"]


# op = {"aet": ["eat", "ate", "tea"], "aedr": ["dear", "dare", "read"]}
anagrams = {}

for word in words:      # eat
	key = "".join(sorted(word))      # [a, e, t]  ==> "aet"

	if key not in anagrams:
		anagrams[key] = [word]
	else:
		anagrams[key] += [word]

print(anagrams)

# default dictionary

from collections import defaultdict

d = defaultdict(list)

for word in words:
	key = "".join(sorted(word))
	d[key] += [word]

print(d)















