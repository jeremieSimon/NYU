class Points (object): 
      """
      """
      Points = []
      def __init__ (self, infos):
            """
            @infos: list of (x, y, timeLeft)
            """
            self.infos = infos
            self.avgTimeLeft = sum(info[2] for info in self.infos) / (len(self.infos)+0.0)
            sortByTimeLeft = sorted(self.infos, key = lambda self.infos: infos[2])

      def self.parsing(self):
            """
            Parsing each point. if the point has a very low timeLeft, then give him a higher
            priority by doubling it.
            Coeff: point in the first 3rd, tripple it
            point in the 2nd 3rd, double
            point in the 3rd 3rd, do nothing
            Append the total to Points
            """
            for info in self.infos:
            
            
            

      
