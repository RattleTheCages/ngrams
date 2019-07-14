#################################################################################
#                                                                               #
#  graphExe                                                                     #
#                                                                               #
#################################################################################

from bst import BinarySearchTree
from graphEdge import graphEdge


Debug = True


#################################################################################
#                                                                               #
#  CreateGraph(Wordlist, Dictionary, EdgeList, EdgeTree)                        #
#                                                                               #
#  Create an edge for each n-word list, drawing an edge from the n word to the  #
#  n+1 word, the n+1 word to the n+2 word, etc.                                 #
#                                                                               #
#  Find if there is a congruent edge, and if so, add to its count.              #
#                                                                               #
#################################################################################
def CreateGraph(Wordlist, Dictionary, EdgeList, EdgeTree):
    i = 0
    for word in Wordlist:
        word1 = word
        word2 = Wordlist[i+1]
        word3 = Wordlist[i+2]
        word4 = Wordlist[i+3]
        word5 = Wordlist[i+4]

        i += 1
        if i == len(Wordlist)-6:
            break

        edge = graphEdge(Dictionary.find(word1), Dictionary.find(word2), Dictionary.find(word3))
        EdgeList.append(edge)

        x = EdgeTree.find(edge)
        if x == None:
            EdgeTree.insert(edge, 1)
        else:
            EdgeTree.change(edge, x+1)

        if Debug is True and i % 5000 == 0:
            print("Edge generated:", i, word1, word2, word3)

    for edge in EdgeTree:
        x = EdgeTree.find(edge)
        edge.count = x


#################################################################################
#                                                                               #
#  ComputeEdgeCountList(EdgeList, EdgeTree, EdgeCount)                          #
#                                                                               #
#  We are only interested in edges that have been drawn more than once.         #
#  Make a list of edges that appear more than once.                             #
#                                                                               #
#################################################################################
def ComputeEdgeCountList(EdgeList, EdgeTree, EdgeCount):
    dbc = 0  #Debug line count.
    seen = set(EdgeList);
    for edge in seen:
        x = EdgeTree.find(edge)
        if x != None and x > 1:  # We are only interested in edges that have been drawn more then once.
            EdgeCount.append(edge)

        if Debug is True and dbc % 5000 == 0:
                edge.Print("Edge count: %d %s" % (dbc, edge.count))
                dbc += 1

    EdgeCount.sort();


