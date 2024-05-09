import csv

"""
reading a csv file:
- reader(file_obj) -> list of rows
- DictReader(file_obj) -> Dictionary of rows


writer
"""

# comma separated values

path = r"C:\Users\Vidyashree M C\python_class\files\csv_files\sample.csv"
#
# with open(path) as file:
# 	reader_obj = csv.reader(file)
#
# 	for data in reader_obj:
# 		print(data)
#
#
# with open(path) as file:
# 	reader_obj = csv.DictReader(file)
#
# 	for data in reader_obj:
# 		print(data)

####################################################################################
# path = r"C:\Users\Vidyashree M C\python_class\files\csv_files\example.csv"
#
# with open(path) as file:
# 	r_obj = csv.reader(file)
#
# 	for data in r_obj:
# 		print(data)
#
#
# with open(path) as file:
# 	r_obj = csv.DictReader(file)
#
# 	for data in r_obj:
# 		print(data)

##################################################################################
"""
writing into a csv file

writer
DictWriter

- writerow
- writerows
- writeheader

"""

# with open("sample.csv", "w") as file:
# 	w_obj = csv.writer(file)
#
# 	w_obj.writerow("hello")
# 	w_obj.writerow(["hello"])
# 	w_obj.writerow([1, 2, 3, 4])
# 	w_obj.writerow((1, 2, 3, 4))
# 	w_obj.writerow({1, 2, 3, 4})
# 	w_obj.writerow({1: 2, 3: 4})

# with open("sample.csv", "w") as file:
# 	w_obj = csv.DictWriter(file, ["name", "class"])
#
# 	w_obj.writeheader()
# 	w_obj.writerow({"name": "steve", "class": 10})
# 	# w_obj.writerow({"a": 10, "b": 20})
# 	# w_obj.writerow([10, 20])
#
#
# data = [("steve", 2000), ("alex", 1000), ("eve", 2500)]
#
# with open("sample1.csv", "w") as file:
# 	w_obj = csv.writer(file)
#
# 	w_obj.writerows(data)
#
#
# data = [{"a": 10}, {"b": 20}, {"c": 30}]
#
# with open("sample3.csv", "w") as file:
#
# 	w_obj = csv.DictWriter(file, ["a", "b", "c"])
#
# 	w_obj.writeheader()
# 	w_obj.writerows(data)

###################################################################################################
# reading only names of the shares in test.csv

path = r"C:\Users\Vidyashree M C\python_class\files\csv_files\test.csv"

# reader
with open(path) as file:
	r_obj = csv.reader(file)

	names = []
	header = next(r_obj)
	for row in r_obj:       # row -> list
		names.append(row[0])

# print(names)

# DictReader
with open(path) as file:
	r_obj = csv.DictReader(file)
	names = []

	for row in r_obj:       # row -> dictionary
		names.append(row["name"])

# print(names)

###################################################################################
# extract names from employees.csv
path = r"C:\Users\Vidyashree M C\python_class\files\csv_files\employees.csv"


# with open(path) as file:
# 	r_obj = csv.reader(file)
#
# 	header = next(r_obj)
#
# 	for row in r_obj:
# 		print(row[0])

# extract names from employees.csv only if they have pay more than 80000

with open(path) as file:

	r_obj = csv.DictReader(file)

	for row in r_obj:
		if int(row["pay"]) >= 80000:
			print(row["name"])

print("*" * 50)

with open(path) as file:
	r_obj = csv.reader(file)
	header = next(r_obj)

	for row in r_obj:
		if int(row[-1]) >= 80000:
			print(row[0])

print("*" * 50)
# extract names from employees.csv only if the employee is a female
with open(path) as file:

	r_obj = csv.DictReader(file)

	for row in r_obj:
		if row["gender"] == "female":
			print(row["name"])

print("*" * 50)
# extract names from employees.csv only if the employee works in testing dept
with open(path) as file:

	r_obj = csv.DictReader(file)

	for row in r_obj:
		if row["team"] == "testing":
			print(row["name"])

##################################################################################
# group all the data based on columns

with open(path) as file:

	r_obj = csv.DictReader(file)
	data = {}

	# {'name': 'douglas', 'gender': 'male', 'team': 'testing', 'pay': '70000'}
	# {'name': 'thomas', 'gender': 'male', 'team': 'development', 'pay': '80000'}

	for row in r_obj:
		for key, value in row.items():
			if key not in data:
				data[key] = [value]
			else:
				data[key] += [value]
	# print(data)


with open(path) as file:
	r_obj = csv.reader(file)

	headers = next(r_obj)
	print(headers)
	data = {}
	for row in r_obj:
		for key, value in zip(headers, row):

			if key not in data:
				data[key] = [value]
			else:
				data[key] += [value]

	# print(data)

# ['name', 'gender', 'team', 'pay'] -> headers
# ['douglas', 'male', 'testing', '70000'] -> row

# (name, douglas), (gender, male), (team, testing), (pay, 70000)

####################################################################################################
# total sum of pay in employee.csv
# group all the employees based on the team
# group all the employees based on the gender

# count the number of countries in vaccination_data.csv
# get the sum of TOTAL_VACCINATIONS in vaccination_data.csv
# group the countries based on the VACCINES_USED

#####################################################################################################




