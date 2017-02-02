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
	
	
def FPTPvote(a_opinionList):
	"""takes a list of numbers as input, and returns the index of the maximum (random maximum in a tie)"""
	biggest = max(a_opinionList)
	maxList = []
	if(a_opinionList.count(biggest) == 1):
		return(a_opinionList.index(biggest))
	else:
		for i,x in enumerate(a_opinionList):
			if(x==biggest):
				maxList.append(i)
	return(maxList[random.randrange(0,len(maxList))]);
print([1, 3, 29, 4, 29, 10])
print(FPTPvote([1, 3, 29, 4, 29, 10]));#should be 2 or 4

def alternateVote(a_opinionList):
	"""takes a list of numbers as input, and returns a list that is those numbers ranked from 1 to 10"""
	alteredList = [x+1 for x in a_opinionList]#creates a list with no 0s
	voteList = [0]*len(a_opinionList)
	for i in range(1,len(a_opinionList)+1):
		current = FPTPvote(alteredList)
		voteList[current] = i;
		alteredList[current] = 0;
	return(voteList);
print(alternateVote([1, 3, 29, 4, 29, 10]));