"""
Parse text file
"""

def parseDoc(fileName): 
	f = open(fileName).read().split('\n')
	cast = lambda x: [int(el) for el in x]
	def getPersons(): 
		for lines in f[1:]: 
			if lines != '': yield cast(lines.split(',')) 
			else: break 
	persons = list(getPersons())
	return persons


#Step 1: K-means
#Step 2: Favorize the one who are more likely to die soon
#Step 3: Remove outliers
