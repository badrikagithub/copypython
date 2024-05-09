"""
1. open file
2. reading/writing
3. closing file


open(file_name, mode)
mode - read
"""

# without context manager
file_obj = open("sample.txt")
print(file_obj)
print(file_obj.closed)

file_obj.close()
print(file_obj.closed)      # True

# using context manager - with
with open("sample.txt") as file:
	print(file)
	print(file.closed)

print(file.closed)

#################################################################################
# attributes of file object

file_obj = open("sample.txt")

print(file_obj.name)
print(file_obj.mode)
print(file_obj.readable())      # True
print(file_obj.writable())
print(file_obj.encoding)

file_obj.close()
##################################################################################
# modes - read(r), write(w), append(a), create(x)

# read mode
with open("sample.txt", "r") as file:
	print(file)


# # write mode - always creates a new file
# with open("sample.txt", "w") as file:
# 	print(file)

# append mode - add extra content to the existing file
with open("sample.txt", "a") as file:
	print(file)

# # create mode - checks if the file is present
# # if file is not present - creates the file and supports write functionality
# # if the file is present - FileExistsError
# with open("sample1.txt", "x") as file:
# 	print(file)

#####################################################################################
"""
read a file
1. file.read(n) - returns entire file as a single string
2. file.readline(limit) - return one line as a string 
3. file.readlines() - read entire file as a list of lines

"""

with open("sample.txt") as file:
	data = file.read()
	print(data)

	# returns current position of the cursor
	print(file.tell())

	# seeks back the control to specified position
	file.seek(0)
	print(file.tell())

	print("_" * 30)
	data = file.read()
	print(data)

print("*" * 50)

# using read with arguments
with open("sample.txt") as file:
	data = file.read(5)
	print(data)

	data = file.read(5)
	print(data)

	data = file.read(5)
	print(data)


###################################################################################
# readline
with open("sample.txt") as file_obj:
	data = file_obj.readline()
	print(data)
	data = file_obj.readline()
	print(data)
	data = file_obj.readline()
	print(data)
	data = file_obj.readline()
	print(data)

# readline with arguments
with open("sample.txt") as file:
	data = file.readline(5)
	print(data)
	data = file.readline(5)
	print(data)
	data = file.readline(5)
	print(data)
	data = file.readline(5)
	print(data)

##################################################################################################
# readlines
with open("sample.txt") as file:
	data = file.readlines()
	print(data)

# readlines with argument
with open("sample.txt") as file:
	data = file.readlines(12)
	print(data)

#####################################################################################################
"""
writing into a file
1. file.write(string)
2. file.writelines(iterable of strings)
"""

# write in write mode
with open("sample2.txt", "w") as f:
	data = f.write("hello\n")
	print(data)

# write in append mode
with open("sample3.txt", "a") as f:
	f.write("hai\n")

# # write in create mode
# with open("sample4.txt", "x") as f:
# 	f.write("hello world\n")

###################################################################################
# writelines()
with open("sample1.txt", "w") as f:
	f.write("hello!!!!\n")
	f.writelines(["hello\n", "hai\n"])
	f.writelines(("hello...\n", "hai...\n"))
	f.writelines({"hello***\n", "hai***\n"})
	f.writelines({"hello_dict\n": 10, "hai_dict\n": 2})

################################################################################



