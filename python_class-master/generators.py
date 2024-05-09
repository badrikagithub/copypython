def even_nums(iterable):
	evens = []

	for num in iterable:
		if num % 2 == 0:
			evens.append(num)

	return evens


# print(even_nums(list(range(20))))

# generators - generate iterables - lazy iterables
# next()

def even_generator(iterable):
	for num in iterable:
		if num % 2 == 0:
			yield num


evens = even_generator(list(range(10)))
print(evens)            # generator object
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
# print(next(evens))      # stopIteration

evens = even_generator(list(range(10)))
for element in evens:
	print(element)

evens = even_generator(list(range(10)))
print(evens)        # <generator object even_generator at 0x000001A754385E70>
# print(str(evens))
# print(" ".join(evens))
print(list(evens))
print(tuple(evens))

evens = even_generator(list(range(10)))
print(tuple(evens))

####################################################################################

def greet():
	yield "hello"
	yield "hai"
	yield "hello world"
	yield "hai...."
	yield "hello there!!!!!"


res = greet()
print(res)      # generator object address
print(next(res))        # hello
print(next(res))        # hai
print(next(res))        # hello world
print("--------------------------------")
for item in res:
	print(item)

res = greet()
print(list(res))
# print(len(res))

##################################################################################
"""
iterator objects
----------------
* __next__ and __iter__
* dont have any length
"""
###################################################################################
# generate even numbers infinitely

def gen_even():
	num = 0

	while True:
		if num % 2 == 0:
			yield num
		num += 1


res = gen_even()
# print(next(res))

#################################################################################
# generating infinite prime numbers

def prime():
	num = 1
	while True:
		if num > 1:
			for i in range(2, num//2+1):
				if num % i == 0:
					break
			else:
				yield num
		num += 1


res = prime()
print(next(res))

# generating infinite fibonacci numbers

# 0, 1, 1, 2, 3, 5, 8, 13, 21

def fibo():

	a = 0
	b = 1

	for _ in range(10):
		yield a
		c = a + b
		a, b = b, c


res = fibo()


def fibo():

	a = 0
	b = 1

	while True:
		yield a
		c = a + b
		a, b = b, c


res = fibo()

##################################################################################
# yield only the words starting with vowels
names = ["steve", "John", "alex", "lara", "eve"]

def vowels(iterable):

	for word in iterable:
		if word[0].lower() in "aeiou":
			yield word


res = vowels(names)
print(list(res))

# list comprehension
vowel = [name for name in names if name[0].lower() in "aeiou"]
print(vowel)


# generator expressions
vowels = (name for name in names if name[0].lower() in "aeiou")
# print(list(vowels))
# print(str(vowels))
print(" ".join(vowels))


###################################################################################
# yield only the words which have even length
sentence = "python is a programming language"

def even_len_words(words):
	for word in words:
		if len(word) % 2 == 0:
			yield word

print(list(even_len_words(sentence.split())))

# generator expression

res = (word for word in sentence.split() if len(word) % 2 == 0)
print(list(res))

################################################################################
# generator function to countdown from a number to 0

def countdown_gen(start):
	for i in range(start, 0, -1):
		yield i

print(list(countdown_gen(10)))

start = 10
res = list((i for i in range(start, 0, -1)))
print(res)


# generator to yield tuple of name and length pairs
names = ["steve", "John", "alex", "lara", "eve"]

def name_len_pair(names):
	for name in names:
		yield name, len(name)


print(list(name_len_pair(names)))

# expr
res = ((name, len(name)) for name in names)
print(list(res))


# generator to yield reversed names if the name is of odd length
def reversed_list(names):
	for name in names:
		if len(name) % 2 == 1:
			yield name[::-1]

print(list(reversed_list(names)))

res = (name[::-1] for name in names if len(name) % 2 == 1)
print(list(res))

# yield name as it is if it is a palindrome else reverse it

def palindrome(names):
	for name in names:
		if name == name[::-1]:
			yield name
		else:
			yield name[::-1]

print(list(palindrome(names)))


res = (name if name == name[::-1] else name[::-1] for name in names)
print(list(res))















