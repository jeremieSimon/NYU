"""
Follow the idea of K-means ++
"""

import sys


class Points (object): 
      """
      """
      P = []
      def __init__ (self, infos):
            """
            @infos: list of (x, y, timeLeft)
            """
            self.infos = infos
            self.avgTimeLeft = sum(info[2] for info in self.infos) / (len(self.infos)+0.0)
            self.sortByTimeLeft = sorted(infos, key = lambda infos: infos[2])
            self.parsing()

      def parsing(self):
            """
            Parsing each point. if the point has a very low timeLeft, then give him a higher
            priority by doubling it.
            Coeff:
            point in the first 3rd, tripple it
            point in the 2nd 3rd, double
            point in the 3rd 3rd, do nothing
            Append the total to Points
            """
            for i, info in enumerate(self.sortByTimeLeft):
                  if i< (int)(len(self.sortByTimeLeft)/(2.0)):
                        self.P.append(self.sortByTimeLeft[i])
                  if i< (int)(len(self.sortByTimeLeft)/(3.0)):
                        self.P.append(self.sortByTimeLeft[i])
                  self.P.append(self.sortByTimeLeft[i])

      def __call__(self):       
            return self.P

class Cluster(object):
      """
      Will consider each hospital as a cluster
      """
      points = []
      def __init__ (self, hospital, numberOfAmbulances, points):

            if len(self.points)==0: self.points = points
            
            

if __name__ == "main":
      fileName = sys.argv[1]

      def parseDoc(fileName): 
            f = open(fileName).read().split('\n')
            cast = lambda x: [int(el) for el in x]
            def getPersons(): 
                  for lines in f[1:]: 
                        if lines != '': yield cast(lines.split(',')) 
                        else: break
            persons = list(getPersons())
            return persons
      
      infos = parseDoc(fileName)
      points = Points(infos)
      
      
