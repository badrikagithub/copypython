# log decorator

def log(func):          # func --> add
	def wrapper(*args, **kwargs):       # args -> (1, 2), kwargs -> {}
		print(f"executing {func.__name__} function")
		result = func(*args, **kwargs)
		return result
	return wrapper


@log            # add = log(add) = wrapper
def add(a, b):
	return a + b

# print(add(1, 2))            # add --> wrapper

@log
def sub(a, b):
	return a - b

# print(sub(1, 2))

#################################################################################
# positive decorator

def positive(func):             # func -> sub
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		return abs(result)
	return wrapper


@positive       # sub = positive(sub)   = wrapper
def sub(a, b):
	return a - b

# print(sub(1, 2))

################################################################################
# decorator to count the number of arguments passed to a function

def no_of_args(func):
	def wrapper(*args, **kwargs):       # args -> (1, 2), kwargs -> {c: 3, d: 4}
		print(f"number of arguments are {len(args) + len(kwargs)}")
		return func(*args, **kwargs)
	return wrapper

@no_of_args
def spam(a, b, c, d):
	return "in spam"

# print(spam(1, 2, c=3, d=4))

##################################################################################
#  reverse decorator

def reverse(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		if isinstance(result, str):     # if isinstance(result, (str, list, tuple))
			return result[::-1]
		return result

	return wrapper


@reverse
def demo():
	return {1, 2, 3, 4}

# print(demo())       # olleh


@reverse
def add(a, b):
	return a + b

# print(add(1, 2))

#################################################################################
# decorator to execute a function 3 times

def execute_3_times(func):
	def wrapper(*args, **kwargs):
		for _ in range(3):
			print(func(*args, **kwargs))
	return wrapper


@execute_3_times
def greet():
	return "hello world"

# greet()

##################################################################################
# decorator to count the number of function calls

function_count = {}

def count_function_calls(func):
	def wrapper(*args, **kwargs):
		key = func.__name__

		if key not in function_count:
			function_count[key] = 1
		else:
			function_count[key] += 1

		return func(*args, **kwargs)
	return wrapper


@count_function_calls
def add(a, b):
	return a + b

# print(add(1, 2))        # {"add": 1}
# print(add(5, 8))        # {"add": 2}


@count_function_calls
def sub(a, b):
	return a - b

# print(sub(1, 2))        # {"add": 2, sub: 1}
# print(sub(5, 8))
# print(sub(15, 8))
# print(sub(15, 8))
# print(sub(15, 8))
# print(add(10, 20))      # {add: 3, sub: 3}

# print(function_count)
# {add: 2, sub: 3}

#################################################################################
from collections import defaultdict

# d = dict()  # {}
d = defaultdict(int)

def count_function_calls(func):
	def wrapper(*args, **kwargs):
		key = func.__name__
		d[key] = d[key] + 1
		return func(*args, **kwargs)
	return wrapper


@count_function_calls
def add(a, b):
	return a + b

# print(add(1, 2))        # {"add": 1}
# print(add(5, 8))        # {"add": 2}


@count_function_calls
def sub(a, b):
	return a - b

# print(sub(1, 2))        # {"add": 2, sub: 1}
# print(sub(5, 8))
# print(sub(15, 8))
# print(sub(15, 8))
# print(sub(15, 8))
# print(add(10, 20))      # {add: 3, sub: 3}

# print(d)
# {add: 2, sub: 3}

################################################################################
# decorator that accepts only positional arguments

def pos_only(func):
	def wrapper(*args, **kwargs):           # args -> (1, 2, 3) (1, 2), kwargs -> {}, {c: 3}
		if len(kwargs) == 0:
			print("in wrapper")
			return func(*args, **kwargs)
		else:
			# print("no kwargs are allowed")
			raise TypeError("keyword arguments are not allowed")

	return wrapper

@pos_only
def add(a, b, c):
	return a + b + c

# print(add(1, 2, 3))
# print(add(1, 2, c=3))


def pos_only(func):
	def wrapper(*args):           # args -> (1, 2, 3) (1, 2)
		print("in wrapper")
		return func(*args)

	return wrapper

# print(add(1, 2, 3))
# print(add(1, 2, c=3))

#################################################################################
# decorator to convert the string output of a function to upper case (the output
# must be a string)

def upper_(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)

		if not isinstance(result, str):
			raise ValueError("result must be a string")
		return result.upper()

		# if isinstance(result, str):
		# 	return result.upper()
		# else:
		# 	raise ValueError("result must be a string")

	return wrapper

@upper_
def full_name(fname, lname):
	return fname + lname


# print(full_name("John", "doe"))
# print(full_name([1, 2], [3, 4]))
###########################################################################

# decorator that creates a dictionary of arguments passed to a function and their result pairs

"""

4 - 1, 4, 2
5 - 1, 5
7 - 1, 7

"""

def is_prime(num):
	factors = 0

	for i in range(1, num+1):       # 1, 2, 3, 4, 5
		if num % i == 0:
			factors += 1

	if factors == 2:
		return True
	else:
		return False

# print(is_prime(123))


d = {}
def cache(func):
	def wrapper(*args):
		if args not in d:       # (12,) -> False
			result = func(*args)    # False
			d[args] = result        # {(12,) : False}
		return d[args]
	return wrapper


@cache
def isprime(num):       # 14 // 2 = 7
	print("executing isprime...")
	for i in range(2, num//2 + 1):         # 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
		if num % i == 0:
			return False

	return True

# print(isprime(513))
# print(isprime(513))
# print(isprime(513))

from functools import lru_cache

@lru_cache
def isprime(num):       # 14 // 2 = 7
	print("executing isprime...")
	for i in range(2, num//2 + 1):         # 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
		if num % i == 0:
			return False

	return True

# print(isprime(12))
# print(isprime(12))

###################################################################################

# parameterized decorator
import time

def outer(n):
	def delay(func):
		def wrapper(*args, **kwargs):
			print(f"{func.__name__} has delay of {n}")
			time.sleep(n)
			return func(*args, **kwargs)
		return wrapper
	return delay


@outer(2)       # @outer(2) ==> @delay => spam = delay(spam)
def spam():
	print("in spam")

# spam()


@outer(3)
def greet():
	print("hello world")

# greet()

############################################################################
# log decorator that takes user log message

def logging(message="hello world"):
	def log(func):
		def wrapper(*args, **kwargs):
			print(message)
			return func(*args, **kwargs)
		return wrapper
	return log


@logging("Haii")
def add(a, b):
	return a + b

# print(add(1, 2))

#################################################################################
# execute a function n times

#################################################################################

# type validator decorator

def type_check(type1, type2):       # type1 = int, type2 = int
	def type_validator(func):       # func = add
		def wrapper(*args):         # args = (1, 2)
			if isinstance(args[0], type1) and isinstance(args[1], type2):
				return func(*args)
			else:
				print("not same")
		return wrapper
	return type_validator


def type_check(*types):             # types = (int, float, int)
	def type_validator(func):       # func = add
		def wrapper(*args):         # args = (1, 2, 3)

			for i in range(len(args)):      # i -> 0, 1, 2
				if not isinstance(args[i], types[i]):
					raise TypeError("not same")

			return func(*args)

		return wrapper
	return type_validator


def type_check(*types):  # types = (int, float, int)
	def type_validator(func):  # func = add
		def wrapper(*args):  # args = (1, 2, 3)
			for arg, type_ in zip(args, types):
				if not isinstance(arg, type_):
					raise TypeError(f"{arg} is not an instance of {type_}")

			return func(*args)

		return wrapper

	return type_validator


@type_check(int, float, int)
def add(a, b, c):
	return a + b + c


# print(add(1, 2, 3))
# print(add("hi", "hello"))

################################################################################
from functools import wraps

def log(func):
	@wraps(func)
	def wrapper():
		print("in wrapper")
		return func()
	return wrapper


@log
def spam():
	"""This is spam function and it does nothing"""
	return "in spam"


print(spam())
print(spam.__name__)
print(spam.__doc__)









