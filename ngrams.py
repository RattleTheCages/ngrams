#!/usr/bin/env python
#################################################################################
#                                                                               #
#  ngrams                                                                       #
#                                                                               #
#################################################################################

import time
from bst import BinarySearchTree
from graphEdge import graphEdge
from graphExe import CreateGraph, ComputeEdgeCountList
from ngramsIO import LoadWordlistFromFiles, CreateNGramsList, OutputNGrams


Debug = True


#################################################################################
#                                                                               #
#  CreateDictionaryFromWordlist(Wordlist, Dictionary, DictionaryReverse)        #
#                                                                               #
#  This dictionary assigns an integer value to a word to save memory space.     #
#                                                                               #
#################################################################################
def CreateDictionaryFromWordlist(Wordlist, Dictionary, DictionaryReverse):
    dbc = 0  #Debug line count.
    for word in Wordlist:
        if Dictionary.find(word) is None :
            r = hash(word)  # Python's md5 hash is 16 bytes, perhaps replace with something smaller.
            while r == Dictionary.find(word):
                print("Repeated hash value?")
                exit()

            Dictionary.insert(word, r)
            DictionaryReverse.insert(r, word)

        if Debug is True and dbc % 5000 == 0:
            print("Inserting: ", dbc, word, r)
            dbc += 1


#################################################################################
#                                                                               #
#  main                                                                         #
#                                                                               #
#  Start here.                                                                  #
#                                                                               #
#################################################################################

def main():

    startTime = time.time();
    Wordlist = []
    Dictionary = BinarySearchTree()
    DictionaryReverse = BinarySearchTree()
    EdgeList = []
    EdgeTree = BinarySearchTree()
    EdgeCount = []
    NGramsList = []

    LoadWordlistFromFiles(Wordlist, "words.txt")
    if Debug is True:
        print("Wordlist loaded in %d secs." % (time.time()-startTime))

    CreateDictionaryFromWordlist(Wordlist, Dictionary, DictionaryReverse)
    if Debug is True:
        print("Dictionary created in %d secs." % (time.time()-startTime))


    CreateGraph(Wordlist, Dictionary, EdgeList, EdgeTree)
    if Debug is True:
        print("Graph finished in %d secs.  There are %d edges." % (time.time()-startTime, len(EdgeList)))


    ComputeEdgeCountList(EdgeList, EdgeTree, EdgeCount)
    if Debug is True:
        print("Computed edge count list finished in %d secs." % (time.time()-startTime))


    CreateNGramsList(DictionaryReverse, EdgeCount, NGramsList)

    OutputNGrams(NGramsList)

    if Debug is True:
        print("Finished in %d secs." % (time.time()-startTime))


if __name__ == "__main__":
    main()


