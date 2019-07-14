################################################################################
#                                                                              #
#  Graph Edge data structure                                                   #
#                                                                              #
#  This structure holds the edges that plot individual ngrams.                 #
#  For convenience and memory diminutiveness, there is a data member that      #
#  holds a count of duplicate edges.                                           #
#                                                                              #
################################################################################

class graphEdge:
    def __init__(self, n1, n2, n3 = 0, n4 = 0, n5 = 0):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.count = 0

    def __eq__(self, other):
        if self.n1 == other.n1 and self.n2 == other.n2 and self.n3 == other.n3 and self.n4 == other.n4 and self.n5 == other.n5:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.n1 > other.n1:
            return True
        if self.n1 < other.n1:
            return False

        if self.n2 > other.n2:
            return True
        if self.n2 < other.n2:
            return False

        if self.n3 > other.n3:
            return True
        if self.n3 < other.n3:
            return False

        if self.n4 > other.n4:
            return True
        if self.n4 < other.n4:
            return False

        if self.n5 > other.n5:
            return True
        if self.n5 < other.n5:
            return False
        if self.n5 == other.n5:
            return False

    def __hash__(s):
        return  hash(s.n1+(10*s.n2)+(100*s.n3)+(1000*s.n4)+(10000*s.n5))

    def Print(self, string):
        print("%s: %d %d %d %d " % (string, self.count, self.n1, self.n2, self.n3))




