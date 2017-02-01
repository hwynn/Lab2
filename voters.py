#! python3
#this generates voters with opinion values for x given candidates
#http://stackoverflow.com/a/8064754 inspiration source
import random
def randomSummedList(a_size, a_sum=100):
	numList = [];
	for i in range(a_size-1):
		numList.append(random.randint(0, a_sum))
	numList.append(0)
	numList.append(a_sum)
	numList.sort()
	newList = []
	for i in range(len(numList)-1):
		newList.append(numList[i+1]-numList[i])
	random.shuffle(newList)
	return(newList)

"""size = 10
print("We want",size, "numbers that add up to 100")
numbers = randomSummedList(size, 1000)
print("numbers:", numbers, "Length:", len(numbers))
print("sum:", sum(numbers))
numbers = randomSummedList(8)
print("numbers:", numbers, "Length:", len(numbers))
print("sum:", sum(numbers))"""