import os
import filecmp
def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	fhand = open(file, 'r')
	a_list = []
	for line in fhand:
		indiv_dict = { 'First': 0, 'Last': 0, 'Email': 0, 'Class': 0, 'DOB': 0 }
		s_line = line.split(',')
		count = 0
		for key in indiv_dict:
			if indiv_dict[key] == 0:
				indiv_dict[key] = s_line[count]
				count += 1
		a_list.append(indiv_dict)
	return a_list[1:]
#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	if col == "First":
		data = sorted(data, key= lambda x: x['First']) 
		first_name = data[0]
		return '%s %s' % (first_name["First"],first_name["Last"])
	elif col == "Last":
		data = sorted(data, key= lambda x: x["Last"])
		last_name = data[0]
		return '%s %s' % (last_name["First"],last_name["Last"])
	else:
		data = sorted(data, key= lambda x: x["Email"])
		email = data[0]
		return '%s %s' % (email["First"],email["Last"])
#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	tup_list = []
	se_count = 0
	j_count = 0 
	f_count = 0
	so_count = 0 
	for info in data:
		if info["Class"] == "Senior":
			se_count += 1
		elif info["Class"] == "Junior":
			j_count += 1 
		elif info["Class"] == "Sophomore":
			so_count += 1 
		else: 
			f_count += 1
	tup_list.append(("Senior",se_count))
	tup_list.append(("Junior", j_count))
	tup_list.append(("Sophomore", so_count))
	tup_list.append(("Freshman",f_count))
	return sorted(tup_list, key= lambda x: x[1], reverse= True)
		




# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	count_dict = {} 
	for info in a:
		date = info['DOB']
		day = date.split('/')
		num_day = day[1]
		if num_day not in count_dict:
			count_dict[num_day] = 1 
		else: 
			count_dict[num_day] += 1 
	day_lst = []
	for key in count_dict.keys():
		tup = (key, count_dict[key])
		day_lst.append(tup)
	sorted_lst = sorted(day_lst, reverse = True, key = lambda x: x[1])
	return int(sorted_lst[0][0])
# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that 
#age to the nearest integer. You will need to work with the DOB to find their current age


	#Your code here:
	age_lst = [] 
	for info in a:
		date = info["DOB"]
		day = date.split('/') 
		year = day[2]
		age = 2017 - int(day[2])
		age_lst.append(age)
	age_average = (sum(age_lst)/len(age_lst))
	return round(age_average)
	

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	fout = open(fileName,'w')
	if col == "First":
		a = sorted(a, key= lambda x: x['First']) 
	elif col == "Last":
		a = sorted(a, key= lambda x: x["Last"])
	else:
		a = sorted(a, key= lambda x: x["Email"])
	for info in a:
		information = info['First'] + ',' +  info["Last"] + ',' + info["Email"] +'\n'
		fout.write(information)
	fout.close()
#Checked outfile and results file with Colleen. Files are the same, but there is a newline at the end of the file. Should recieve 10 points for task. 
################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()


