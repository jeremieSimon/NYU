“““
def parseDoc(fileName): 
	f = open(fileName).read().split(‘\n’)
	cast = lambda x: [int(el) for el in x]
	def getPersons(): 
		for lines in f[:1]: 
			if lines != ‘‘: yield cast(lines.split(‘,’)) 
			else: break 
	persons = list(getPersons()) 
“““	