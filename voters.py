#! python3
#this generates voters with opinion values for x given candidates
#http://stackoverflow.com/a/8064754 inspiration source
import random
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
	random.shuffle(newList)
	return(newList)

size = 10
print("We want",size, "numbers that add up to 100")
numbers = random100List(size)
print("numbers:", numbers, "Length:", len(numbers))
print("sum:", sum(numbers))
