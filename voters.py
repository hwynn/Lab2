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
#print([1, 3, 29, 4, 29, 10])
#print(FPTPvote([1, 3, 29, 4, 29, 10]));#should be 2 or 4

def alternateVote(a_opinionList):
	"""takes a list of numbers as input, and returns a list that is those numbers ranked from 1 to 10"""
	alteredList = [x+1 for x in a_opinionList]#creates a list with no 0s
	voteList = [0]*len(a_opinionList)
	for i in range(1,len(a_opinionList)+1):
		current = FPTPvote(alteredList)
		voteList[current] = i;
		alteredList[current] = 0;
	return(voteList);
#print(alternateVote([1, 3, 29, 4, 29, 10]));

class Candidate:
	"""A candidate's profile and all information about their performance in an election.
	
	Attributes:
		self.name			The name (or possibly species) of the candidate
		self.opinionScore	The total opinion scores for the candidate from all voters. The higher this is for a candidate, the more highly voters think of them.
							Each voter has 100 opinion score to give. So the total opinionScore of all candidates will be 100*voters
		self.FPTPvotes		In the first past the post (FPTP) ballot system, the voter can only vote for one candidate. This number represents how many 
		self.AVplacement	In the alternate vote (AV) system (also known as Instant-runoff voting or transferable vote), each voter ranks the candidates from most to least desireable. This is a list of all the ranks a candidate earns from all voters combined.
							The placement of votes on this list represents ranked votes. [0] is 1st, [1] is 2nd, [2] is 3rd and etc.
		self.AVvotes		In the alternate vote (AV) system, a candidate must win over 50% of the votes to win. These votes are assigned in cycles from the candidate's ranked votes with the least popular candidate dropping out in each cycle.
	Methods:
		def __init__(self, name)				Creates empty Candidate object
		def setup_AVplacement(self, rosterSize)	Adjusts the size of self.AVplacement so that there is one element per rank in the election
		def add_opinionScore(self, x)			Adds to a candidates total opinion score
		add_FPTPvote(self)						Adds a single FPTP vote to a candidate's tally
		def add_AVplacement(self, rank)			Adds a single ranked vote to a candidate's alternate votes
		AVtransfer(self, round)					When the alternate votes are being counted, this will transfer a candidate's next rank of alternate votes to their total votes
												This function must be used in a loop with rounds starting at 1 and ending at [rosterSize]
		show_name(self)							Returns the candidate's name
		show_opinionScore(self)					Returns the candidate's opinionScore
		show_FPTPvotes(self)					Returns the candidate's FPTPvotes
		show_AVplacement(self)					Returns the candidate's list of ranked votes from 1st to last
		show_AVvotes(self)						Returns the candidate's current alternate vote total. This will begin at 0 and will only be finalized after all the AV counting cycles
	"""
	def __init__(self, name):
		self.name = name
		self.opinionScore = 0
		self.FPTPvotes = 0
		self.AVplacement = []
		self.AVvotes = 0
		
	def setup_AVplacement(self, rosterSize):
		self.AVplacement = [0]*rosterSize
		
	def add_opinionScore(self, x):
		self.opinionScore = self.opinionScore + x
	
	def add_FPTPvote(self):
		self.FPTPvotes = self.FPTPvotes + 1
	
	def add_AVplacement(self, rank):
		self.AVplacement[rank-1] += 1
		#self.AVplacement[0] is a candidate's 1st votes, [1] is their 2nd votes, etc.
		#+= used hesitantly
	
	def AVtransfer(self, round):
		#round 1 will use a candidates 1st votes, stored in self.AVplacement[0] round2 is 2nd votes in self.AVplacement[1] etc.
		self.AVvotes = self.AVvotes + self.AVplacement[round-1]
	
	def show_name(self):
		return(self.name)
		
	def show_opinionScore(self):
		return(self.opinionScore)
	
	def show_FPTPvotes(self):
		return(self.FPTPvotes)
		
	def show_AVplacement(self):
		return(self.AVplacement)
	
	def show_AVvotes(self):
		return(self.AVvotes)

class Election:
	def __init__(self, candidateList, voterSize):
		self.candidates = [Candidate(x) for x in candidateList] #immediately creates empty candidate objects
		for x in self.candidates:
			x.setup_AVplacement(len(candidateList));
		self.turnout = voterSize
	
	def generateVoters(self):
		count = 0
		while(count<self.turnout):
			currentVoter = randomSummedList(len(self.candidates))
			for i in range(len(currentVoter)):
				self.candidates[i].add_opinionScore(currentVoter[i])
			self.candidates[FPTPvote(currentVoter)].add_FPTPvote()
			AVresponce = alternateVote(currentVoter)
			for i in range(len(AVresponce)):
				self.candidates[i].add_AVplacement(AVresponce[i])
			count = count+1
		
	def runElection(self):
		self.generateVoters()
		#function that starts creating voters
		for x in self.candidates:
			print(x.show_name())
			print("Opinion score:", x.show_opinionScore())
			print("FPTPvotes:", x.show_FPTPvotes())
			print("AVplacement:", x.show_AVplacement())
		


firstTest = Election(["puppy", "bunny", "raccoon"], 20)
firstTest.runElection()