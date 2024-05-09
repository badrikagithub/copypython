from collections import Counter, defaultdict, deque
from itertools import islice, zip_longest

# with open("sample.txt") as file:
# 	print(file)     # iterator object
#
# 	for line in file:
# 		print(line)
#
# # print line along with line number - enumerate
# with open("sample.txt") as f:
# 	for line_no, line in enumerate(f, start=1):
# 		print(line_no, line)

# # read the file in reversed order
# with open("sample.txt") as file:
#
# 	for line in reversed(list(file)):
# 		print(line)

##################################################################################
# # reading sample.log using for loop
# sample_log_path = r"C:\Users\Vidyashree M C\python_class\files\sample.log"
#
# with open(sample_log_path) as sample_log_file:
# 	for line in sample_log_file:
# 		# check if the line is empty
# 		if line.strip():
# 			data = line.split()
# 			print(data[2])

# count the number of lines present in the file

sample_log_path = r"C:\Users\Vidyashree M C\python_class\files\sample.log"

with open(sample_log_path) as file:
	count = 0
	for line in file:
		count += 1
	# print(count)


# count number of blank lines in the file

with open(sample_log_path) as file:
	count = 0

	for line in file:
		if not line.strip():
			count += 1

	# print(count)

#################################################################################
# count the total number of words present in the file

with open(sample_log_path) as file:
	total_words = 0

	for line in file:
		words = line.split()
		total_words += len(words)

	# print(total_words)

#################################################################################
# find the length of each line in the file

# with open("sample.txt") as file:
# 	for line in file:
# 		print(len(line))


# # find the number of words in each line
# with open("sample.txt") as file:
# 	for line in file:
# 		print(len(line.split()))

# count the number of spaces present in the file
with open("sample.txt") as file:
	spaces = 0
	for line in file:
		spaces += line.count(" ")
	# print(spaces)

#################################################################################
# count the total number of messages

sample_log_path = r"C:\Users\Vidyashree M C\python_class\files\sample.log"

with open(sample_log_path) as file:
	count = 0
	for line in file:
		if line.strip():
			data = line.split()[2]
			count += 1
	# print(count)

# count each message separately

with open(sample_log_path) as file:
	messages = {}

	for line in file:
		if line.strip():
			data = line.split()[2]

			if data not in messages:
				messages[data] = 1
			else:
				messages[data] += 1

	# print(messages)

#  most repeated message
least_repeated, *rest, most_repeated = sorted(messages.items(), key=lambda x: x[1])
# print(most_repeated)

# using Counter

with open(sample_log_path) as file:
	msgs = []
	for line in file:
		if line.strip():
			data = line.split()[2]
			msgs.append(data)

	c = Counter(msgs)
	# print(c)


# # most common message
# print(c.most_common(1))

###################################################################################
# count the number of occurrences of ip addresses in access-log.txt

access_log_path = r"C:\Users\Vidyashree M C\python_class\files\access-log.txt"

with open(access_log_path) as file:
	ips = {}
	for line in file:
		if line.strip():
			ip_ = line.split()[0]

			if ip_ not in ips:
				ips[ip_] = 1
			else:
				ips[ip_] += 1
	# print(ips)

# most occurred ip address
least, *rest, most = sorted(ips.items(), key=lambda item: item[-1])
# print(least, most)

# using counter()

################################################################################
# count the occurrences of country names in football.txt

path = r"C:\Users\Vidyashree M C\python_class\files\football.txt"

with open(path, encoding="UTF-8") as file:
	country = defaultdict(int)

	# skipping the header
	header = next(file)

	for line in file:
		if line.strip():
			data = line.split("\t")[1]
			country[data] += 1

	# print(country)

###################################################################################
# group the players based on their positions
path = r"C:\Users\Vidyashree M C\python_class\files\football.txt"

with open(path, encoding="utf-8") as file:

	header = next(file)
	data = {}

	for line in file:
		if line.strip():
			position = line.split("\t")[4]
			player = line.split("\t")[-2]

			if position not in data:
				data[position] = [player]
			else:
				data[position].append(player)
	# print(data)


with open(path, encoding="utf-8") as file:

	header = next(file)
	data = defaultdict(list)

	for line in file:
		if line.strip():
			position, player = line.split("\t")[4], line.split("\t")[-2]
			data[position].append(player)

	# print(data)


# group the colors based on the brands

path = r"C:\Users\Vidyashree M C\python_class\files\data.txt"

with open(path) as file:
	data = defaultdict(list)
	for line in file:
		if line.strip():
			brand, color = line.split("\t")[0], line.split("\t")[1]
			data[brand] += [color]
	# print(data)

with open(path) as file:
	data = {}

	for line in file:
		if line.strip():
			brand, color = line.split("\t")[0], line.split("\t")[1]

			if brand not in data:
				data[brand] = [color]
			else:
				if color not in data[brand]:
					data[brand] += [color]
	# print(data)

###################################################################################
# print 5th line from a file

path = r"C:\Users\Vidyashree M C\python_class\files\access-log.txt"
n = 4

with open(path) as file:

	for line_no, line in enumerate(file, start=1):
		if line_no == n:
			print(line)
			break

# islice()

with open(path) as file:
	print(list(islice(file, 4-1, 4)))

################################################################################
# print all the line from 12 - 16th lines
with open(path) as file:

	for line_no, line in enumerate(file, start=1):
		if line_no in range(12, 16+1):            # 12 <= line_no <= 16
			print(line)

print("*" * 50)
# islice
start = 12
stop = 16
with open(path) as file:
	lines = islice(file, start-1, stop)

	for line in lines:
		print(line)



################################################################################
# print first 5 lines

# with open(path) as file:
#
# 	for line_no, line in enumerate(file, start=1):
# 		if line_no in range(1, 6):            # 12 <= line_no <= 16
# 			print(line)

################################################################################
# print last 2 lines

with open("sample.txt") as file:
	count = 0

	for _ in file:
		count += 1
	print(count)

	file.seek(0)
	lines = islice(file, count-2, count)

	for line in lines:
		print(line)


with open("sample.txt") as file:
	lines = deque(file, 2)

	for line in lines:
		print(line)


#################################################################################
# # copy the contents of sample.txt to another file
# with open("sample.txt") as read_file, open("sample_copy.txt", "w") as write_file:
# 	for line in read_file:
# 		write_file.write(line)

with open("sample.txt") as file1, open("sample_copy.txt") as file2:
	for line1, line2 in zip_longest(file1, file2):
		if line1 != line2:
			# raise ValueError("Contents are not same")
			print("contents are not same")
			break
	else:
		print("contents are same")


#################################################################################
with open("sample1.txt", "a+") as file:
	# file.write("hellooo\n")
	file.seek(0)
	for line in file:
		print(line)


with open("sample1.txt", "w+") as file:
	file.write("hello\n")
	file.seek(0)
	for line in file:
		print(line)

#####################################################################################################

