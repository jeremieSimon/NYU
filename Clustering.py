"""
Follow the idea of K-means ++

-Choose one center uniformly at random from among the data points.
-For each data point x, compute D(x), the distance between x and the nearest center that has already been chosen.
-Choose one new data point at random as a new center, using a weighted probability distribution where a point x is
chosen with probability proportional to D(x)2.
-Repeat Steps 2 and 3 until k centers have been chosen.
-Now that the initial centers have been chosen, proceed using standard k-means clustering.
"""

import sys
import math 


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
      def __init__ (self, x, y, points):

            if len(self.points)==0: self.points = points
            self.centroidDistance = []
            self.points = points[:2]
            self.coord = (x, y)
            
      def computeCentroid(self):
            """
            Compute the distance from the cluster to each point
            """
            for point in points:
                  centroidDistance.append(distance(self.coord, self.points))

      @staticmethod
      def Distance(p1, p2):
            """
            Compute the euclidean distance of the 2 points
            @param p = (x, y)
            """
            distance = math.sqrt(math.pow(p2[0]-p1[0], 2) + math.pow(p2[1] - p1[1], 2)) 
            return distance
            
            

def main():
      """
      Make the cluster and run the main loop
      """
            

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
      
      
