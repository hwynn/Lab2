#! python3
#this generates voters with opinion values for x given candidates
#first we need a function that generates a list of x integers that add up to 100
#http://stackoverflow.com/a/8064754 inspiration source

"""x = 8;
print("We want", x, "numbers that add up to 100")
numList = [];
for i in range(x-1):
	numList.append(random.randint(0, 100))

print("initial list:", numList, "Length:", len(numList))
print("numList sum:", sum(numList))
numList.append(0)
numList.append(100)
numList.sort()
print("step 2 list:", numList, "Length:", len(numList))
newList = []
for i in range(len(numList)-1):
	newList.append(numList[i+1]-numList[i])

print("newList:", newList, "Length:", len(newList))
print("newList sum:", sum(newList))

import random
import copy"""
#http://stackoverflow.com/a/8064754 inspiration source
import random
import copy
def random100List(x):
	numList = [];
	for i in range(x-1):
		numList.append(random.randint(0, 100))
	numList.append(0)
	numList.append(100)
	numList.sort()
	newList = []
	for i in range(len(numList)-1):
		newList.append(numList[i+1]-numList[i])
	return(newList)

size = 10
print("We want",size, "numbers that add up to 100")
numbers = random100List(size)
print("numbers:", numbers, "Length:", len(numbers))
print("sum:", sum(numbers))