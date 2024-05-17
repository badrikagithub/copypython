# """
# # ** Write a program to find the length of the string without using inbuilt function (len)**
#
# def length(iterable):
#
# 	count = 0
# 	for _ in iterable:
# 		count += 1
#
# 	return count
#
# # print(length("hello"))
#
# # Write a program to reverse a string without using any inbuilt functions.
# string = "hello"
#
# # reversed(sequence) - str, list, tuple
#
# result = reversed(string)       # result -> reversed object/ iterator object
# # print(result)
#
# # # type_casting
# # print("".join(list(result)))
# #
# # result = reversed(string)
# # # traverse
# # for i in result:
# # 	print(i, end="")
# #
# # print()
# #
# # # next()
# # result = reversed(string)
# # # print(dir(result))
# # print(next(result))
# # print(next(result))
# # print(next(result))
# # print(next(result))
# # print(next(result))
# # print(next(result))         # StopIteration
#
# # # slicing
# # print(string[::-1])
#
# # # concatenation
# # result = ""
# #
# # for char in string:
# # 	result =  char + result
# #
# # print(result)
#
# """
# char                    result
# h                       "" + h          h
# e                       e + h           eh
# l                       l + eh          leh
# l                       l + leh         lleh
# o                       o + lleh        olleh
#
# """
#
# #######################################################################################################
# # Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe"
#
# # replace()
# s = "Hello World"
#
# res = s.replace("World", "Universe")
# # print(res)
#
# # for loop
# words = s.split()
# res = ""
# for word in words:
# 	if word == "World":
# 		res = res + "universe" + " "
# 	else:
# 		res = res + word + " "
#
# # print(res)
#
# #############################################################################################
# # How to convert a string to a list and vice-versa.
#
# s = "hello world"
#
# # l = list(s)
# # print(l)
# # print("".join(l))
# #
# # l_words = s.split()
# # print(l_words)
# # print(" ".join(l_words))
#
# ######################################################################################################
# # Covert the string "Hello welcome to Python" to a comma separated string.
#
# # s = "Hello welcome to Python"
# # print(s.replace(" ", ","))
#
# ######################################################################################################
# # Write a program to print alternate characters in a string.
# # print(s[::2])
# # print(s[1::2])
#
# #####################################################################################################
# # Write a Program to print ascii values of the characters present in a string
#
# # s = "Hello welcome to Python"
# #
# # for char in s:
# # 	print(ord(char))
#
# ######################################################################################################
# # Write program to convert upper case to lower case and vice-versa without using inbuilt method.
#
#
# def swap_case(string):
# 	result = ""
#
# 	for char in string:
# 		if "a" <= char <= "z":
# 		# if ord(char) in range(ord("a"), ord("z")+1):
# 			result += chr(ord(char) - 32)
#
# 		elif "A" <= char <= "Z":
# 		# elif ord(char) in range(ord("A"), ord("Z")+1):
# 			result += chr(ord(char) + 32)
#
# 		else:
# 			result += char
# 	return result
#
# # print(swap_case(string))
#
# ######################################################################################################
# # Write program to swap two numbers without using 3rd variable.
# a, b = 1, 2
# a, b = b, a
#
# ##################################################################################################
# # Write program to merge two different lists.
#
# l1 = [1, 2, 3, 4]
# l2 = [5, 6, 7, 8]
#
# # # concatenation
# # print(l1 + l2)
# #
# # # unpacking
# # c = [*l1, *l2]
# # print(c)
#
# # # extends
# # l1.extend(l2)
# # print(l1)
#
# # # chain
# # from itertools import chain
# # c = chain(l1, l2)
# # print(list(c))
#
# #####################################################################################################
# # Write program to read a random line in a file. (ex. 50, 65, 78th line)
# path = r"C:\Users\Vidyashree M C\python_class\files\sample.log"
#
# def read_random_line(n):
#
# 	# with open(path) as file:
# 	# 	for line_no, line in enumerate(file, start=1):
# 	# 		if line_no == n:
# 	# 			print(line)
# 	# 			break
#
# 	# 	islice
# 	from itertools import islice
# 	with open(path) as file:
# 		lines = islice(file, n-1, n)
# 		print(list(lines))
#
# # read_random_line(4)
#
#
# # Write program to read a random lines in a file. (ex. I want read all lines 10th to 15th line)
# from itertools import islice
#
# def random_lines(start, end):
#
# 	with open(path) as file:
# 		# lines = islice(file, start-1, end)
# 		# for line in lines:
# 		# 	print(line)
#
# 		for line_no, line in enumerate(file, start=1):
#
# 			if line_no in range(start, end+1):
# 				print(line)
#
# # random_lines(2, 5)
#
# ###################################################################################################
# # Program to print last "N" lines of a file
#
# def read_last_n_lines(n):
#
# 	# islice
# 	with open(path) as file:
# 		count = 0
# 		for _ in file:
# 			count += 1
#
# 		# print(file.tell())
# 		file.seek(0)
# 		# print(file.tell())
#
# 		lines = islice(file, count-n, count)
#
# 		for line in lines:
# 			print(line)
#
#
# def read_last_n_lines(n):
# 	from collections import deque
#
# 	with open(path) as file:
# 		lines = deque(file, n)
# 		for line in lines:
# 			print(line)
#
#
# # read_last_n_lines(3)
#
# #######################################################################################################
# #  Write a program to check if the given string is Palindrome or not without using reversed method
#
# def is_palindrome(string):
# 	print(string[::-1] == string)
#
# # is_palindrome("hello")
#
# ######################################################################################################
# # Write a program to search for a character in a given string and return the corresponding index
#
# def search(string, key):        # linear search
#
# 	for index, char in enumerate(string):
# 		if char == key:
# 			print(f"{char} is found at index {index}")
# 			break
#
# 	else:
# 		print("character is not found")
#
#
# # search("hello", "x")
#
# ####################################################################################
# # Write a program to get the below output**
# sentence = "hello world welcome to python programming hi there"
# # d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }
#
# words = sentence.split()
# d = {}
#
# for word in words:
# 	key = word[0]
# 	if key in d:
# 		d[key].append(word)     # d[word[0]] = d[word[0]] + [word]
# 	else:
# 		d[key] = [word]
#
# # print(d)
#
# # default dictionary
# from collections import defaultdict
#
# dd = defaultdict(list)
# words = sentence.split()
#
# for word in words:
# 	dd[word[0]].append(word)        # dd[word[0]] = dd[word[0]] + [word]
# 									# dd["h"] = dd["h"] + [hello]
# 									#  dd["h"] = [] + [hello]
#
# # print(dd)
#
# #################################################################################
# # Write a to replace all the characters with - if the character occurs more than once in a string
# s = "hello world"
# res = ""
#
# for char in s:
# 	if s.count(char) > 1:
# 		res += "-"
# 	else:
# 		res += char
#
# # print(res)
#
# #####################################################################################
# # write a decorator that returns only positive values of subtraction
#
# def positive(func):
# 	def wrapper(*args, **kwargs):
# 		result = func(*args, **kwargs)
# 		return abs(result)
# 	return wrapper
#
#
# @positive       # sub = positive(sub)
# def sub(a, b):
# 	return a - b
#
#
# # print(sub(1, 2))        # -1
#
# ##################################################################################
# # How to get the count of number of instances of a class that is being created.
#
# class Point:
# 	count = 0
#
# 	def __init__(self, a, b):
# 		self.a = a
# 		self.b = b
# 		Point.count += 1
#
#
# p1 = Point(1, 2)        # __init__
# p2 = Point(10, 20)
# p3 = Point(3, 2)
# p4 = Point(1, 7)
#
# # print(Point.count)
# """
# to access a class variable
# 1. self.class_var
# 2. className.class_var
# 3. self.__class__.class_var
# """
# #####################################################################################################
# # Write a function which takes a list of strings and integers.If the item is a string it should print
# # as is and if the item is integer of float it should reverse it.
#
# items = ["hello", 10, "hai", 1.2]
#
#
# def spam(iterable):
#
# 	for item in iterable:
# 		if isinstance(item, (int, float)):
# 			print(str(item)[::-1])
# 		else:
# 			print(item)
#
# # spam(items)
#
# ####################################################################################################
# # Write a class named Simple and it should have iteration capability.
#
# class Simple:
#
# 	def __init__(self, iterable):
# 		self.iterable = iterable
#
# 	def __iter__(self):     # returns iterator object
# 		return iter(self.iterable)
#
#
# s = Simple([1, 2, 3, 4])
# # print(dir(s))
#
# # for item in s:
# # 	print(item)
#
# ######################################################################################################
# # # iterator protocol
# #
# # s = "hello"
# #
# # for char in s:
# # 	print(char)
#
# # x = iter(s)         # __iter__
# # while True:
# # 	try:
# # 		char = next(x)      # __next__
# #
# # 	except StopIteration:
# # 		break
# #
# # 	print(char)
#
# #####################################################################################################
# # iterator class
#
# class Iterator:
#
# 	def __init__(self):
# 		self.start = 0
# 		self.end = 5
#
# 	def __iter__(self):
# 		return self
#
# 	def __next__(self):
# 		if self.start < self.end:
# 			self.start += 1
# 			return self.start
# 		raise StopIteration
#
#
#
# # i = Iterator()
# #
# # for item in i:
# # 	print(item)
#
# ####################################################################################################
# # Write a Custom class which can access the values of dictionaries using d['a'] and d.a
#
# class MyDict:
#
# 	def __init__(self, d):
# 		self.d = d
#
# 	def __getattribute__(self, item):
# 		if item == "a":
# 			return self.d["a"]
# 		elif item == "b":
# 			return self.d["b"]
#
# 		return super().__getattribute__(item)
#
# 	# def __getattribute__(self, item):
# 	# 	return self.d[item]
#
#
# # m = MyDict({"a": 1, "b": 2})
# # print(m.__dict__)
# # print(m.a)
# # print(m.b)
#
#
# class MyDict:
#
# 	def __init__(self, a, b):
# 		self.a = a
# 		self.b = b
#
# 	def __getitem__(self, item):
# 		if item == "a":
# 			return self.a
# 		elif item == "b":
# 			return self.b
#
# 		raise KeyError(f"{item} is not found")
#
# # m = MyDict(1, 2)
# # print(m.a)          # m.__getattribute__(a)
# # print(m.b)          # m.__getattribute__(b)
# #
# # print(m["a"])           # m.__getitem__(a)
# # print(m["b"])            # m.__getitem__(b)
# # print(m["c"])            # m.__getitem__(b)
# #####################################################################################################
#
# class Sample:
#
# 	def __init__(self, d):
# 		self.d = d
#
# 	# invoked for all the attributes
# 	def __getattribute__(self, item):
# 		print("in getattribute")
# 		return super().__getattribute__(item)
#
# 	# invoked only for missing attributes
# 	def __getattr__(self, item):
# 		print("in getattr")
#
# # s = Sample(10)
# # print(s.e)
#
#
# class MyDict:
#
# 	def __init__(self, d):
# 		self.d = d          # __setattr__
#
# 	def __getattribute__(self, item):
# 		print(f"checking for {item} in getattribute")
# 		return super().__getattribute__(item)
#
# 	def __getattr__(self, item):
# 		print(f"invoking get attr for {item}")
# 		return self.d[item]             # __getattribute__
#
# 	def __getitem__(self, item):
# 		return self.d[item]
#
# 	# def __setattr__(self, key, value):
# 	# 	print(f"setting {key} with value {value}")
# 	# 	if isinstance(value, dict):
# 	# 		super().__setattr__(key, value)
# 	# 	else:
# 	# 		raise TypeError("expecting a dictionary")
#
#
#
# # m = MyDict({"a": 1, "b": 2})
# # print(m.a)              # m.__getattribute__(a)
# # print(m.b)              # m.__getattribute__(b)
# # # print(m.c)
# # print(m["a"])           # m.__getitem__(a)
#
# # m.e = 10
#
# #####################################################################################################
# # Write a python program to get the below output**
#
# sentence = "Hi How are you"
# # o/p should be "iH woH era uoy"
#
#
# words = [word[::-1] for word in sentence.split()]
# # print(" ".join(words))
#
# ###############################################################################################
# # Write a lambda function to add two numbers (a, b)
#
# add = lambda a, b: a + b
# # print(add(1, 2))
#
# #####################################################################################################
# # How to remove duplicates from the list without using inbuilt functions**
# items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
#
# # set(items)
#
# dup = []
# for item in items:
# 	if item not in dup:
# 		dup.append(item)
#
# # print(dup)
#
# dup = []
# for item in items:
# 	if items.count(item) == 1:
# 		dup.append(item)
# # print(dup)
#
# ####################################################################################################
# # Find the longest word in the sentence**
# sentence = "Hello world. Welcome to Python"
#
# # for loop
# longest = ""
#
# for word in sentence.split():
# 	if len(word) > len(longest):
# 		longest = word
# # print(longest)
#
# # sorted()
# smallest, *rest, longest = sorted(sentence.split(), key=len)
# # print(longest)
#
# # max()
# # print(max(sentence.split(), key=len))
#
# ######################################################################################################
# # write a program to reverse the values in the dictionary if the value is of type String**
# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
#
# for key, value in d.items():
# 	if isinstance(value, str):
# 		d[key] = value[::-1]
#
# # print(d)
# ###################################################################################################
# # write a program to get 1234**
# t = ('1', '2', '3', '4')
# # print("".join(t))
#
# ####################################################################################################
# # How to get the elements that are in list b but not in list a**
# a = [1, 2, 3]
# b = [1, 2, 3, 4]
#
# # print(set(a) - set(b))
# # print(set(b) - set(a))
#
#
# if len(a) > len(b):
# 	longest, smallest = a, b
# else:
# 	longest, smallest = b, a
#
# l = []
# for item in longest:
# 	if item not in smallest:
# 		l.append(item)
#
# # print(l)
#
# ##################################################################################################
# # A function takes variable number of positional arguments as input. How to check if the arguments
# # that are passed are more than 5
#
# def func(*args):
# 	if len(args) > 5:
# 		print("arguments are more than 5")
# 	else:
# 		print("arguments are less than 5")
#
#
# # func(1, 2, 3, 4, 5, 6, 7)
#
# #####################################################################################################
# # Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.**
# # Assume Below is the contents of the log file
#
# lines = """CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical"""
#
#
# split_lines = lines.split("\n")
# # lines.splitlines()
# # print(split_lines)
#
# d = {}
# for line in split_lines:
# 	message = line.split(":")[0]
# 	if message not in d:
# 		d[message] = 1
# 	else:
# 		d[message] += 1
#
# # print(d)
#
# dd = defaultdict(int)
# for line in split_lines:
# 	message = line.split(":")[0]
# 	dd[message] += 1            # dd[message] = dd[message] + 1
# 													# 0 + 1
#
# # print(dd)
#
# ###################################################################################################
# # Write a function to reverse any iterable without using reverse function.**
#
# a = [1, 2, 3, 4, 5]
#
# def reverse_(iterable):
# 	return iterable[::-1]
#
# #####################################################################################################
# # Write a function to print the below output.**
# # func("TRACXN", 0)  # Should print RCN
# # func("TRACXN", 1)  # Should print TAX
#
#
# def func(string, n):
# 	if n == 0:
# 		return string[1::2]
# 	elif n == 1:
# 		return string[::2]
#
# # print(func("TRACXN", 0))
# # print(func("TRACXN", 1))
#
# ################################################################################################
# # Sum all the numbers in the below string.**
# s = "Sony12India567Pvt2ltd"
#
# sum_ = 0
# for char in s:
# 	if char.isdigit():
# 		sum_ += int(char)
#
# # print(sum_)
#
# ####################################################################################################
# # Write a program to sum all the numbers in below string.**
# s = "Sony12India567Pvt2ltd" # eg.12+567+2
#
# # import re
# # res = re.findall(r"\d+", s)
# # print(res)
#
#
# # result = ""
# #
# # for char in s:
# # 	if char.isdigit():
# # 		result += char
# # 	else:
# # 		result += " "
# #
# # sum_ = 0
# # for num in result.split():
# # 	sum_ += int(num)
# #
# # print(sum_)
#
# ####################################################################################################
# # Print all the numbers in the below list**
# a = ['abc', '123', 'hello', '23']
#
# res = [item for item in a if item.isdigit()]
# # print(res)
#
# # Program to print the number of occurrences of characters in a String without using inbuilt functions.**
# s = 'helloworld'
#
# d = {}
# for char in s:
# 	if char not in d:
# 		d[char] = 1
# 	else:
# 		d[char] += 1
#
# # print(d)
#
# # Program to print only the repeated characters and count of the same.**
# s = 'helloworld'
# d = {}
# for char in s:
# 	if s.count(char) > 1:
# 		if char not in d:
# 			d[char] = 1
# 		else:
# 			d[char] += 1
# # print(d)
#
# # Write a program to get alternate characters of a string in list format.**
# s = 'hello world welcome to python'
# # print(list(s[::2]))
#
#
# # Write a program to get square of list of number's using lambda function .**
# a = [1, 2, 3, 4, 5]
#
# square = lambda item: item ** 2
#
# # print(list(map(square, a)))
#
# # l = []
# # for item in a:
# # 	square_num = res(item)
# # 	l.append(square_num)
# # print(l)
#
# # Write a program to iterate through list and build a new list, only if the items of the list has
# # even number of characters.**
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
#
# res = [name for name in names if len(name) % 2 == 0]
# # print(res)
#
#
# # Write a program to iterate through list and build a new dictionary, only if the items of the list
# # has even number of characters.**
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
#
# d = {name: len(name) for name in names if len(name) % 2 == 0}
# # print(d)
# #######################################################################################################
# # Count number of lines in a file without loading the file to the memory
#
# with open("practice_questions.txt") as file:
# 	count = 0
# 	for line in file:
# 		count += 1
# 	# print(count)
#
# #####################################################################################################
# # Printing line and line no's
#
# # with open("practice_questions.txt") as file:
# # 	for line_no, line in enumerate(file, start=1):
# # 		print(line_no, line)
#
# ####################################################################################################
# # Write a Program to print the sum of entire list and sum of only internal list**
#
# l = [[1,2,3],[4,5,6],[7,8,9]]
#
# internal_sum = [sum(item) for item in l]
# # print(internal_sum)
# # print(sum(internal_sum))
#
# ###################################################################################################
# # Write a program to reverse the list as below**
# words = ["hi", "hello", "python"]
# # o/p ['nohtyp', 'olleh', 'ih']
#
# res = [word[::-1] for word in words[::-1]]
# # print(res)
#
# ###################################################################################################
# # Write a program to update the tuple**
# t1 = (1, 2, 3, 4)
# t2 = (100, 200, 300)
# # o/p (1, 2, 3, 4, 100, 200, 300)
#
# t1 = t1 + t2
# # print(id(t1))
# # print(t1)
#
# ###################################################################################################
# # Write a program to replace value present in nested dictionary.**
# d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# # Replace "nose" with "net"
#
# for key, value in d.items():
# 	if isinstance(value, dict):
# 		for k, v in value.items():
# 			if v == "nose":
# 				value[k] = "net"
#
# # print(d)
#
# ####################################################################################################
# # Write a program to count the number of white spaces in a file.
#
# with open("practice_questions.txt") as file:
# 	space_count = 0
# 	# for line in file:
# 		# space_count += line.count(" ")
# 	# print(space_count)
#
# 	for line in file:
# 		for char in line:
# 			if char == " ":
# 				space_count += 1
# 	# print(space_count)
#
# #####################################################################################################
# # 54 Grouping anagrams.**
# words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']
# anagrams = {}
#
# for word in words:
# 	key = "".join(sorted(word))
#
# 	if key not in anagrams:
# 		anagrams[key] = [word]
# 	else:
# 		anagrams[key] += [word]
#
# # print(anagrams)
#
#
# # checking if 2 strings are anagrams
# def is_anagram(s1, s2):
# 	return sorted(s1) == sorted(s2)
#
# # print(is_anagram("fear", "fare"))
#
# # [a, e, f, r]
# # [a, r, f, r]
#
# #####################################################################################################
# d = {"a": 1, "b": 2}
#
# # print(d["c"])
# # print(d.get("c"))
# # print(d.get("c", 10))
# # print(d)
#
# ####################################################################################################
# # Write a list comprehension to get a list of even numbers from 1-50
#
# l = [num for num in range(1, 51) if num % 2 == 0]
# # print(l)
#
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # print(nums)
#
# # even = lambda num: num % 2 == 0
#
# def even(num):
# 	if num % 2 == 0:
# 		return num
#
# # map
# # print(list(map(even, nums)))        # 10 elements
# #
# # print(list(filter(even, nums)))
#
# # default - 0, int(), 0.0, float(), False, bool(), 0j, complex(), "", [], (), {}, set(), None
#
# # squares of even numbers
# def square(num):
# 	if num % 2 == 0:
# 		return num ** 2
# 	# else:
# 	# 	return "odd"
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# # print(list(map(square, nums)))
# #
# # print(list(filter(square, nums)))
#
#
# def add(a, b):
# 	return a + b
#
#
# l1 = [1, 2, 3]
# l2 = [13, 23, 31, 4]
#
# # print(list(map(add, l1, l2)))
#
# ##################################################################################
# # property
#
# class Demo:
#
# 	def __init__(self, a):
# 		self.a = a
#
# 	# 	getter - access the value of the attribute
# 	@property
# 	def a(self):
# 		return self._a
#
# 	# setter
# 	@a.setter
# 	def a(self, value):
# 		if value < 0:
# 			raise ValueError("negative values are not allowed")
# 		self._a = value
#
# 	# deleter
# 	@a.deleter
# 	def a(self):
# 		del self._a
#
#
# # d = Demo(10)
# # print(d.__dict__)
# # print(Demo.__dict__)
# # print(d.a)
# # del d.a
# # print(d.a)
#
# ###################################################################################
# # Find the longest non-repeated substring in the below string**
# s = "This is a Programming language and Programming is fun"
#
# # sorted()
# words = s.split()
# non_rep = [word for word in words if words.count(word) == 1]
# print(non_rep)
#
# *rest, longest = sorted(non_rep, key=len)
# # print(longest)
#
# #  for loop
# longest = ""
# for word in words:
# 	if words.count(word) == 1:
# 		if len(longest) < len(word):
# 			longest = word
#
# # print(longest)
#
# ##################################################################################
# # Write a program to find the duplicate elements in the list without using inbuilt functions**
# names = ['apple', 'google', 'apple', 'yahoo', 'google']
#
# # # count
# # for name in names:
# # 	if names.count(name) > 1:
# # 		print(name)
# #
# # #
# # dup = []
# # non_dup = []
# # for name in names:
# # 	if name not in non_dup:
# # 		non_dup += [name]
# # 	else:
# # 		dup += [name]
# #
# # # print(dup)
# #
# # # dictionary
# # dd = defaultdict(int)
# #
# # for name in names:
# # 	dd[name] += 1
# #
# # print(dd)
# #
# # for key, value in dd.items():
# # 	if value > 1:
# # 		print(key)
#
# ###################################################################################################
# # Write a program to count the number occurrences of each item in the list without using any inbuilt functions**
# names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
#
# d = {}
#
# for name in names:
# 	if name not in d:
# 		d[name] = 1
# 	else:
# 		 d[name] += 1
#
# # print(d)
#
# #####################################################################################################
# # Write a function to check if the number is Prime
#
# def is_prime(num):
# 	if num > 1:
# 		for i in range(2, num//2+1):        # range(2, int(num ** 0.5)+1)
# 			if num % i == 0:
# 				print("not a prime number")
# 				break
# 		else:
# 			print("number is prime")
# 	else:
# 		print("number should be greater than 1")
#
#
# # is_prime(29)
# """
# 5
#
# 2 - 5 % 2
# 3 - 5 % 3
# 4 - 5 % 4
# ... 28
#
# 9
#
# 2 - 9 % 2
# 3
# 4
# 5
# 6
# 7
# 8
# """
# #####################################################################################################
# # How to create a tuple using range function
#
# # print(tuple(range(0)))
#
# ######################################################################################################
# # Write a program to find the largest number in the list without using any inbuilt functions**
# numbers = [10, 20, 30, 40, 50]
#
# largest = numbers[0]
#
# for num in numbers:
# 	if num > largest:
# 		largest = num
#
# # print(largest)
#
# #####################################################################################################
# # Write a method that returns the last digit of an integer. For example,
# # the call of get_last_digit(3572) should return 2
#
# def get_last_digit(num):
# 	return int(str(num)[-1])
#
# # print(get_last_digit(3572))
#
#
# ####################################################################################################
# # Write a program to find most common words in a given list.**
# words = [
# 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
# 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
# 'eyes', 'look', 'into','my', 'eyes', "you're", 'under'
# ]
#
# d = {}
#
# for word in words:
# 	if word not in d:
# 		d[word] = 1
#
# 	else:
# 		d[word] += 1
#
# # print(d)
#
# # print(d.items())
# # [('look', 4), ('into', 3), ('my', 3), ('eyes', 8), ('the', 5), ('not', 1), ('around', 2),
# # ("don't", 1), ("you're", 1), ('under', 1)]
#
#
# get_value = lambda item: item[1]        # item -> ('look', 4)
#
# # print(sorted(d.items(), key=get_value)[-1])
#
#
# # Counter
# from collections import Counter
#
# # c = Counter(words)
# # print(c)
# # print(c.most_common(2))
# #
# # print(Counter("hello"))
# # print(Counter({1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4}))
# # print(Counter({"a":"1", "b": "2", "c": "3"}))
#
# ####################################################################################################
# # Make a function named tail that takes a sequence (like a list, string, or tuple) and a number n and
# # returns the last n elements from the given sequence, as a list.
#
# def tail(sequence, n):
# 	return list(sequence[-n:])      # return list(deque(sequence, n))
#
#
# # print(tail([1, 2, 3, 4], 2))
# # print(tail((1, 2, 3, 4), 1))
# # print(tail("hello", 3))
#
# ###################################################################################################
# # Write function named is_perfect_square that accepts a number and returns True if it's a perfect
# # square and False if it's not.
#
# def is_perfect_square(num):
#
# 	for i in range(num):
# 		if i * i == num:
# 			return True
#
# 	return False
#
# # print(is_perfect_square(14))
#
# # from math import isqrt
# # num = 27
# # s = isqrt(num)           # 2       # num ** 0.5
# #
# # if s ** 2 == num:
# # 	print("perfect square")
# # else:
# # 	print("not a perfect square")
#
# ################################################################################################
#
# # Write a program to count the number of occurrences of each word in a file.
#
# with open("practice_questions.txt") as file:
# 	word_count = {}
# 	for line in file:
# 		for word in line.split():
# 			if word not in word_count:
# 				word_count[word] = 1
# 			else:
# 				word_count[word] += 1
# 	# print(word_count)
#
# #################################################################################################
# # Write a program to count the number of occurrences of vowels in a file.
#
# with open("practice_questions.txt") as file:
# 	vowels = defaultdict(int)
#
# 	for line in file:
# 		for char in line:
# 			if char in "aeiouAEIOU":
# 				vowels[char] += 1
# 	# print(vowels)
#
# ####################################################################################################
# # Write a program to print all numeric values in a list**
# items = ['apple', 1.2, 'google', '12.6', 26, '100']
#
# # for item in items:
# # 	if isinstance(item, (int, float)):
# # 		print(item)
#
# ######################################################################################################
# #  Triangle Patterns**
#
# """
# *
# * *
# * * *
# * * * *
# * * * * *
# """
#
# n = 5
#
# # for row in range(1, n+1):        # row = 1, 2, 3, 4
# # 	for col in range(row):      # col = (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)
# # 		print("*", end=" ")
# #
# # 	print()
#
#
# # for row in range(1, n+1):
# # 	print("* " * row)
#
# # print("a", "b", "c", sep="-")
#
# """
#
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# """
#
# # for num in range(1, 6):
# # 	print(f'{"* " * num:>10}')
#
# """
#
# ____*
# ___**
# __***
# _****
# *****
# """
#
# """
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# """
#
# # for row in range(1, 6):
# # 	print(f'{"* " * row:^10}')
#
# """
# * * * * *
# * * * *
# * * *
# * *
# *
# """
# n = 5
# # # for row in range(1, n+1)[::-1]:
# # for row in range(n, 0, -1):
# # 	print("* " * row)
#
# """
#   * * * * *
#     * * * *
#       * * *
#         * *
#           *
# """
# # for row in range(1, n+1)[::-1]:
# # 	print(f'{"* " * row:>10}')
# #
# #
# # for row in range(1, n+1)[::-1]:
# # 	print(f'{"* " * row:^10}')
#
# ###########################################################################################################
# # n = 5
# #
# # for row in range(1, n+1):
# # 	print(f'{"* " * row:^10}')
# #
# # for row in range(1, n)[::-1]:
# # 	print(f'{"* " * row:^10}')
#
# ####################################################################################################
# """
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# """
# # n = 5
# # pattern = ""
# #
# # for row in range(1, n+1):
# # 	pattern = pattern + str(row) + " "
# # 	print(pattern)
#
# """
# row                 pattern
# 1                       "1"
# 2                       "1" + "2"
# 3                       "1" + "2" + 3
# 4                       "1" + "2" + 3 + 4
# 5                       "1" + "2" + 3 + 4 + 5
# """
#
# #######################################################################################
# """
#     1
#    12
#   123
#  1234
# 12345
# """
# #
# # pattern = ""
# #
# # for row in range(1, 6):
# # 	pattern += str(row) + " "
# # 	print(f'{pattern:>10}')
# #
# # pattern = ""
# #
# # for row in range(1, 6):
# # 	pattern += str(row) + " "
# # 	print(f'{pattern:^10}')
#
# ########################################################################################
# # Write a program count the occurrence of a particular word in the file
# key = "program"
# with open("practice_questions.txt") as file:
# 	count = 0
# 	# for line in file:
# 	# 	words = line.split()
# 	# 	for word in words:
# 	# 		if key == word:
# 	# 			count += 1
# 	#
# 	# print(count)
#
# 	for line in file:
# 		words = line.split()
# 		count += words.count(key)
# 	# print(count)
#
# #########################################################################################
# # Write a program to map a product to a company and build a dictionary with company and list of products pair**
# # ```python
# all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows',
#                 'iOS', 'Google Drive', 'One Drive']
#
# # Pre-defined products for different companies
# apple_products = {'iPhone', 'Mac', 'iWatch'}
# google_products = {'Gmail', 'Maps', 'Google Drive'}
# msft_products = {'Windows', 'One Drive'}
#
#
# d = defaultdict(list)
# # d = {}
# for product in all_products:
# 	if product in apple_products:
# 		d["apple_products"] += [product]
# 	elif product in google_products:
# 		d["google_products"] += [product]
# 	elif product in msft_products:
# 		d["msft_products"] += [product]
# # print(d)
#
# #########################################################################################
# # Write a program to rotate items of the list**
# names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
#
# def _rotate(iterable, n):
#
# 	for i in range(n):
# 		item = iterable.pop()
# 		iterable.insert(0, item)
# 	return (iterable)
#
# # print(_rotate(names, 8))
# # print(_rotate(list("hello world"), 8))
#
# names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
# def _rotate(iterable, n):
#
# 	rem = n % len(iterable)
# 	return iterable[-rem:] + iterable[:-rem]
#
#
# # print(_rotate(names, 8))
#
# # Write a program to rotate characters in a string
#
# # print(_rotate("hello world", 2))
# # sentence = "Hello world welcome to python"
# # print(_rotate(sentence.split(), 2))
# #######################################################################################
# # Write a program to count the number of white spaces in a given string**
# sentence = "Hello world welcome to Python Hi  How are you. Hi how are you"
#
# # print(sentence.count(" "))
#
# count = 0
# for char in sentence:
# 	if char == " ":
# 		count += 1
#
# # print(count)
#
# #######################################################################################
# # Write a program to count the number of commented lines in a text file
#
# with open("practice_questions.txt") as file:
# 	count = 0
# 	for line in file:
# 		if line.startswith("#"):        # line[0] == "#"
# 			count += 1
#
# 	# print(count)
#
# ##########################################################################################
# # Write a program to check if the year is leap year or not
#
# # year = 1600
# #
# #
# # if year % 4 == 0 and year % 100 != 0:       # non century year
# # 	print(f"{year} is a leap year")
# #
# # elif year % 400 == 0:       # century year
# # 	print(f"{year} is a leap year")
# #
# # else:
# # 	print(f"{year} is not a leap year")
#
#
# # from calendar import isleap
# # print(isleap(year))
#
# ######################################################################################
# """
# *
# *
# *
# * *
# *
# * * *
# *
# * * * *
# *
# * * * * *
# """
#
# # for i in range(1, 6):
# # 	print("*")
# # 	print("* " * i)
# ######################################################################################
# # Write a program to get the below output**
# """
# >>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# >>> [1, 2]
#     [3, 4]
#     [5, 6]
#     [7, 8]
#     [9]
# """
# a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#
#
# # for i in range(0, len(a), 2):   # [0, 2, 4, 6, 8]
# # 	print(a[i:i+2])
#
# ########################################################################################
# # Write a program to check if the elements in the second list is series of continuation
# # of the items in the first list**
# a = [10, 12, 15, 16, 18]
# b = [20, 22, 24, 26, 28]
#
# def is_sequence(iter1, iter2):
# 	diff = iter1[1] - iter1[0]      # 12-10 = 2
# 	x = iter1 +  iter2
#
	# for i in range(len(x)-1):
	# 	if x[i] + diff != x[i+1]:        # 12 + 2 == 15
	# 		print("not a sequence")
	# 		break
	# else:
	# 	print("It is a sequence")
#
# # is_sequence(a, b)
#
#
# def is_sequence(iter1, iter2):
# 	diff = iter1[0] - iter2[0]      # 10 - 20 = -10
# 	x = zip(iter1, iter2)
#
# 	for i1, i2 in x:
# 		if i1 - i2 != diff:
# 			print("not a sequence")
# 			break
#
# 	else:
# 		print("sequence")
#
# # is_sequence(a, b)
#
# # a = [0, 5, 10, 15]
# # b = [20, 25, 30, 35, 40]
# #
# # x = [10, 20, 30, 40]
# # y = [50, 40, 60, 70]
#
# ####################################################################################
# #Write a program to find the first repeating character in a string**
# s = 'helloworld'
#
# # for char in s:
# # 	if s.count(char) > 1:
# # 		print(char)
# # 		break
#
# # s1 = ""
# # for char in s:
# # 	if char not in s1:
# # 		s1 += char
# # 	else:
# # 		print(char)
# # 		break
#
# ########################################################################################
# # Write a program to find the index of nth occurrence of a sub-string in a string**
# sentence = "hello world welcome to python hello hi how are you hello there"
#
# # import re
# # finditer
#
# # result = re.finditer("hello", sentence)
# #
# # n = 2
# # count = 0
# # for item in result:
# # 	count += 1
# # 	if count == n:
# # 		print(item.start(), item.end())
#
# #####################################################################################
# # Write a program to print prime numbers from 1 to 50
#
# # for num in range(1, 51):
# # 	if num > 1:
# # 		for i in range(2, num // 2 + 1):
# # 			if num % i == 0:
# # 				break
# #
# # 		else:
# # 			print(num, end=" ")
#
# #####################################################################################
# # Write a program to sort a list which has mix of both odd and even numbers,
# # the sorted list should have odd numbers first and then even numbers in sorted order**
# a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
#
#
# evens = [item for item in a if item % 2 == 0]
# odds = [item for item in a if item % 2 == 1]
#
# # odds.sort()
# # evens.sort()
# # result = odds + evens
# # print(result)
#
# result = sorted(odds) + sorted(evens)
# print(result)
#
# # Write a program to sort a list which has mix of both odd and even numbers,
# # in the sorted list, odd numbers should be in ascending order and
# # even numbers should be in descending order**
# a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
#
# evens = [item for item in a if item % 2 == 0]
# odds = [item for item in a if item % 2 == 1]
#
# # result = sorted(odds) + sorted(evens, reverse=True)
# # print(result)
#
# ########################################################################################
# # **97 Write a program to count the number of occurrences of non-special characters in a given string**
# s = 'hello@world! welcome!!! Python$ hi how are you & where are you?'
#
# import string
#
# count = 0
# for char in s:
# 	if char in string.punctuation:
# 		count += 1
#
# # print(count)
#
# ########################################################################################
# # Grouping Flowers and Animals in the below list**
# items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']
#
# d = {}
#
# for item in items:      # lotus-flower
# 	name, category = item.split("-")     # [lotus, flower]
#
# 	if category not in d:
# 		d[category] = [name]
# 	else:
# 		d[category].append(name)
# # print(d)
#
# # Grouping files with same extensions**
# files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
#
# d = defaultdict(list)
#
# for file in files:
# 	name, extension = file.split(".")
# 	d[extension].append(name)
#
#
# # print(d)
# ########################################################################################
# # Find all max numbers from the below list**
# numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
#
# max_num = max(numbers)
#
# # for num in numbers:
# # 	if num == max_num:
# # 		print(num)
#
# #######################################################################################
# # Find all max length words from the below sentence**
# sentence = "hello world hi apple you yahoo to you"
# words = sentence.split()
# max_word = max(words, key=len)
# # print(max_word)
#
# # for word in words:
# # 	if len(word) == len(max_word):
# # 		print(word)
#
# #######################################################################################
# # Find the range from the following string**
# sentence = '0-0, 4-8, 20-20, 43-45'
# # >>> # Output Should be [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]
#
# nums = sentence.split(",")
# # print(nums)         # ['0-0', ' 4-8', ' 20-20', ' 43-45']
# output = []
# for num in nums:
# 	start, end = num.split("-")
# 	output += list(range(int(start), int(end)+1))
#
# # print(output)
#
# #######################################################################################
# # static method
#
#
#
#
# class Demo:
#
# 	def spam(self):         # instance method
# 		print("in spam", self)
#
# 	@classmethod
# 	def sample(cls):           # class address
# 		print("in sample", cls)
#
# 	def display(self):
# 		print("hello....")
#
# 	@staticmethod
# 	def add(a, b):          # independent function
# 		print(a + b)
# 		print("hello..")
#
#
# # d = Demo()
# # d.spam()
# #
# # # calling a class method
# # d.sample()
# # Demo.sample()
# #
# # # calling a static method
# # d.add(1, 2)
# # Demo.add(1, 2)
# #
# # print(dir(Demo))
#
# ########################################################################################
# # Can we override a static method in python?
#
# class Parent:
#     @staticmethod
#     def demo():
#         print('Running demo in Parent')
#
# class Child(Parent):
#     @staticmethod
#     def demo():
#         print('Running demo in Child')
#
#
# # c = Child()
# # c.demo()
#
# ########################################################################################
# # Write a function which returns the sum of lengths of all the iterables**
#
# def total_length(*args):
# 	count = 0
# 	for arg in args:
# 		count += len(arg)
# 	return count
#
#
# # print(total_length([1, 2, 3], (4, 5), ['apple', 'google', 'yahoo', 'gmail', 'flipkart']))
# ########################################################################################
#
# # Replace all vowels with "*"**
# sentence = "hello world welcome to python"
# res = ""
# for char in sentence:
# 	if char.lower() in "aeiou":
# 		res += "*"
# 	else:
# 		res += char
#
# # print(res)
#
# ########################################################################################
# # Replace all occurances of "Java" with "Python" in a file
#
# with open("read_sample.txt") as file, open("sample.txt", "w") as write_file:
#
# 	for line in file:
# 		re_line = []
# 		words = line.split()
# 		for word in words:
# 			if word == "Java":
# 				re_line.append("python")
# 			else:
# 				re_line += [word]
#
# 		# line = " ".join(re_line)
# 		# write_file.write(line+"\n")
#
# ########################################################################################
# # Maximum sum of 3 numbers and Minimum sum of 3 numbers**
# numbers = [10, 15, 20, 25, 30, 35, 40, 15, 15]
#
# result = sorted(numbers)
# # print("maximum sum of 3 numbers", sum(result[-3:]))
# # print("minimum sum of 3 numbers", sum(result[:3]))
#
# ########################################################################################
# # Write a program to get the output as below**
# string = "python@#$%pool"
# # # o/p should be ['PYTHON', 'POOL']
#
# res = ""
# for char in string:
# 	if char.isalpha():      # "a" <= char <= "z" or "A" <= char <= "Z"
# 		res += char
# 	else:
# 		res += " "
#
# # print(res.upper().split())
#
# ########################################################################################
# # Write a program to get the indexes of each item in the below list**
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# # output should be -  {'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]}
#
# ########################################################################################
# # Write a program to print "Bangalore" 10 times without using "for" loop**
#
# # print("Bangalore\n" * 10)
# """
########################################################################################
# Write a program to remove duplicates from the list without using set or empty list**
l1 = [1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 4]
l2 = l1[:]

for num in l2:
	if l1.count(num) > 1:
		l1.remove(num)
# print(l1)

########################################################################################
# Print all the missing numbers from 1 to 10 in the below list**
numbers = [1, 3, 6, 8, 10]


# for i in range(1, 11):
# 	if i not in numbers:
# 		print(i)

########################################################################################
# Write a python program to get the below output**
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
# >>> # o/p ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']
res = []
for item1 in l1:
	for item2 in l2:
		res.append(str(item1) + item2)

# print(res)
########################################################################################
#Write a python program to get the below output**
word = "AAAAaaccYYY"
# o/p ['Y3', 'c2', 'a2', 'A4']
res = []
for char in set(word):
	count_ = word.count(char)
	res.append(char + str(count_))

# print(res)

########################################################################################
# In the list below, find all the number pairs which results in 10 either when added or subtracted**
a = [3, 5, -4, 8, 11, 1, -1, 6]

# for index1 in range(len(a)):
# 	for index2 in range(index1+1, len(a)):
# 		if a[index1] + a[index2] == 10 or a[index1] - a[index2] == 10:
# 			print(a[index1], a[index2])

########################################################################################
# Write a decorator to prefix +91 to the original phone numbers**
numbers = [1234567890, 123456790, 1234567890]

def prefix_91(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		return "+91" + str(result)
	return wrapper

@prefix_91
def get_phone_num(num):
	return num

# for num in numbers:
# 	print(get_phone_num(num))

########################################################################################
# Reverse a list without using any built-in functions and slicing**
a = [1, 2, 3, 4, 5]
res = []
for index in range(len(a)-1, -1, -1):
	res += [a[index]]

# print(res)

###################################################################################
#  write a program to get the below output using while loop**
# 1
# 12
# 123
# 1234

# n = 4
# pattern = ""
# for row in range(1, n+1):
# 	pattern += str(row)
# 	print(pattern)
#
#
# count = 1
# pattern = ""
# while count <= n:
# 	pattern += str(count)
# 	print(pattern)
# 	count += 1

###################################################################################
# write a program to get the below output**
items = ['$123.45', '$434.23', '$567.89']
res = []

for item in items:
	res.append(float(item[1:]))
# print(res)
# >>> # o/p [123.45, 434.23, 567.89]

###################################################################################
# Generator function for Fibonacci series program

def fibo(n):
	a, b = 0, 1
	for i in range(n):
		yield a
		c = a + b
		a = b
		b = c
		# a, b = b, c

# res = fibo(5)
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
"""
n = 5

a                   b                       c
-----------------------------------------------
0                   1                       1
1                   1                       2
1                   2                       3
2                   3                       5
3                   5                       8


a, b = 0, 1


c = a + b
a = b
b = c
"""
# write a program to print nth fibonocci number

def nth_fibo(n):
	a, b = 0, 1
	for i in range(n-1):      # 5th -> a = 3
		a, b = b, a + b

	return a

# print(nth_fibo(5))

###################################################################################
# Write a program to print common character present in all the items of the below list**
items = [ "glories", "glass", "sight", "fights"]
common = []
for char in items[0]:   # glories -> g, l, o, r, i, e, s

	for item in items[1:]:  # ["glass", "sight", "fights"]
		if char not in item:
			break
	else:
		common.append(char)
# print(common)

items = [ "glories", "glass", "sight", "fights"]
common_char = []
for char in items[0]:       # g, l
	# l = []
	# for item in items[1:]:  # "glass", "sight", "fights"
	# 	l.append(char in item)

	l = [char in item for item in items[1:]]

	if all(l):
		common_char.append(char)
# print(common_char)

###################################################################################
# all(), any()

def is_prime(num):
	if num > 1:
		for i in range(2, n):
			if num % i == 0:
				print("not a prime number")
				break

		else:
			print("prime number")

def is_prime(num):
	# l = []
	# if num > 1:
	#
	# 	for i in range(2, num):
	# 		l.append(num % i)
	#
	# print(all(l))

	return all([num % i for i in range(2, num)])

# is_prime(16)

###################################################################################
# Function should accept a list and if any number divisible by 3 then modify to 33 or else keep it as it is**

def function(items):
	# result = []
	# for item in items:
	# 	if item % 3 == 0:
	# 		result.append(33)
	# 	else:
	# 		result.append(item)
	# print(result)

	result = [33 if item % 3 == 0 else item for item in items]
	print(result)

# function([1, 2, 3, 4, 5, 6])
###################################################################################
"""
1 2 3 *
1 2 * 4
1 * 3 4
* 2 3 4
"""

n = 4
star_col = 4
for row in range(n):    # 0
	pattern = ""
	for col in range(1, n+1):    # 1, 2, 3 ,4   1, 2, 3, 4
		if col == star_col:
			pattern += "* "
		else:
			pattern += str(col) + " "
	star_col -= 1
	# print(pattern)


n = 4

for i in range(n, 0, -1):
	pattern = ""
	for col in range(1, n+1):
		if col == i:
			pattern += "* "
		else:
			pattern += str(col) + " "
	# print(pattern)
###################################################################################
# write a program to map digits to its corresponding word**
d = {   "0": "ZERO", "1": "ONE", "2": "TWO", "3": "THREE", "4": "FOUR",
        "5": "FIVE", "6": "SIX", "7": "SEVEN", "8": "EIGHT", "9": "NINE"
    }


# num = 123

# for char in str(num):
# 	print(d[char])

###################################################################################
 # validate if the list contains odd number at the begining (0th index) and even numbers there after from 1st till end of the list**
# numbers = [1, 2, 4, 8, 6, 12] ----> the function should return True
# numbers = [1, 2, 4, 7, 6, 12] ----> the function should return False
# numbers = [2, 2, 4, 8, 6, 12] ----> the function should return False

numbers = [1, 2, 4, 81, 6, 12]
# is_odd = numbers[0] % 2
#
# for num in numbers[1:]:
# 	if num % 2 != 0:
# 		print(False)
# 		break
# else:
# 	if is_odd:
# 		print(True)
# 	else:
# 		print(False)

def is_sequence(iterable):

	if iterable[0] % 2:
		for item in iterable[1:]:
			if item % 2 != 0:
				return False
		return True

	return False
# print(is_sequence(numbers))

###################################################################################
# sort the list of names based on lastname or first character of the lastname**

names = ['steve jobs', 'bill gates', 'john doe', 'tim cook', 'laura turner', 'alex martin']

def last_name(name):
	fname, lname = name.split()     # [steve, jobs]
	return lname

result = sorted(names, key=lambda name: name.split()[-1])
# print(result)

###################################################################################################
# write unique characters to the file**
word = "aaabbbccc"

unique = set(word)

uniques = []
for letter in word:
	if letter not in uniques:
		uniques.append(letter)
# print(uniques)

# with open("demo.txt", "w") as file:
# 	# file.writelines(unique)
#
# 	for item in uniques:
# 		file.write(item + "\n")

#######################################################################################
# Comparing two versions of the software
from packaging.version import Version
a = "11.3.4"
b = "2.4.5"

# print(Version(a) > Version(b))

#######################################################################################
# Comparing two employee objects**

class Employee:

	def __init__(self, name, experience):
		self.name = name
		self.experience = experience

	# def __gt__(self, other):
	# 	if self.experience > other.experience:
	# 		return True
	# 	return False

	def __lt__(self, other):
		if self.name < other.name:
			return True
		return False


e1 = Employee('alex', 5)
e2 = Employee('brain', 1)

# print(e1 < e2)        # e1.__gt__(e2)        e2.__gt__(e1)
# print(dir(Employee))
print(e1 > e2)          # e2.__lt__(e1)

#######################################################################################
class Employee:

	def __init__(self, name, experience):
		self.name = name
		self.experience = experience

	def __repr__(self):
		return f'({self.name}, {self.experience})'

	def __gt__(self, other):
		if self.experience > other.experience:
			return True
		return False


e1 = Employee('alex', 5)
e2 = Employee('brain', 1)
e3 = Employee('clara', 2)
e4 = Employee('steve', 4)
e5 = Employee('max', 3)

# employees = [e1, e2, e3, e4, e5]
# print(sorted(employees))      # requires __gt__ or __lt__ implemented in the class

# without implementing magic method in the class
# sorted_emps = sorted(employees, key=lambda emp: emp.experience)
#
# for emp in sorted_emps:
# 	print(emp)

####################################################################################
# Replace characters at odd index by 'x'**
word = "example"
res = ""

for index, char in enumerate(word):
	if index % 2:
		res += "x"
	else:
		res += char
# print(res)
####################################################################################
# If the number is divisible by 2 it should print 'hi' if the no is divisible by 3
# it should print 'hello' if the number is divisible by both 2 and 3 it should
# print 'bye'. using list comprehension**

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = []
for num in numbers:
	if num % 2 == 0 and num % 3 == 0:
		res.append("bye")
	elif num % 2 == 0:
		res.append("hi")
	elif num % 3 == 0:
		res.append("hello")
	else:
		res.append(num)

# print(res)
####################################################################################
#  write a program to get the below output**
states = {'mysore':'karnataka','Bangalore':'karnataka','chennai':'TN','pune':'maharastra','coimbatore': 'TN'}

d = {}
for city, state in states.items():
	if state not in d:
		d[state] = [city]
	else:
		d[state] += [city]

# print(d)
from collections import defaultdict

d = defaultdict(list)

for city, state in states.items():
	d[state] += [city]
# print(d)
# # o/p {'karnataka': ['mysore', 'Bangalore'], 'TN': ['chennai', 'coimbatore'], 'maharastra': ['pune']}
####################################################################################
# write a program to get the below output**
l1 = ['m', 'na', 'i', 'pyt']
l2 = ['y', 'me', 's', 'hon']

l = [item1 + item2 for item1, item2 in zip(l1, l2)]
# print(l)
# print(" ".join(l))

# >>> # o/p ['my', 'name', 'is', 'python']
####################################################################################
#  write a program to get the below output**
input={1:'a',2:'b',3:'c'}

output = {value: key for key, value in input.items()}
# print(output)

# >>> output = {'a': 1, 'b': 2, 'c': 3}
####################################################################################
# write a program to get the below output**
names = ['bangalore', 'chennai', 'mumbai', 'delhi']
output = [name[-3:] for name in names]
# print(output)
# >>> ['ore', 'nai', 'bai', 'lhi']

####################################################################################
# write a program to sort the given collection that contains uppercase, lowercase numeric and special character based on ASCII value**
items = ['a', 'b', 'C', 'D', 1, 8, '!']


# print(sorted(items, key=lambda item: ord(str(item)), reverse=True))
####################################################################################






