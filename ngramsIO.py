#################################################################################
#                                                                               #
#  ngramsIO                                                                     #
#                                                                               #
#  Input and Output for deducing ngrams.                                        #
#                                                                               #
#################################################################################

import nltk

#################################################################################
#                                                                               #
#  LoadWordlistFromFiles(Wordlist, filename)                                    #
#                                                                               #
#  Create a list of all the words in the given files.                           #
#                                                                               #
#################################################################################
def LoadWordlistFromFiles(Wordlist, filename):
    file = open(filename, "r");
    words = []
    for line in file:
        words = nltk.word_tokenize(line)
        for word in words:
            if word.isalpha():
               #print(word)
                Wordlist.append(word.lower())



#################################################################################
#                                                                               #
#  CreateNGramsList(DictionaryReverse, EdgeCount, NGramsList)                   #
#                                                                               #
#  Create a list of the results, suitable for human consumption.                #
#                                                                               #
#################################################################################
def CreateNGramsList(DictionaryReverse, EdgeCount, NGramsList):
    for edge in EdgeCount:

        edgeString = str("%04d" % edge.count) 
        edgeString += " "
        edgeString += DictionaryReverse.find(edge.n1)
        edgeString += " "
        edgeString += DictionaryReverse.find(edge.n2)
        edgeString += " "
        edgeString += DictionaryReverse.find(edge.n3)

        if edge.count > 6:  # List only ngrams who's edge has been drawn more than six times.
            NGramsList.append(edgeString);

    NGramsList.sort()


#################################################################################
#                                                                               #
#  OutputNGrams(NGramsList)                                                     #
#                                                                               #
#  Print the human readable results to standard out.                            #
#                                                                               #
#################################################################################
def OutputNGrams(NGramsList):
    for ngram in NGramsList:
        print(ngram)


#################################################################################
#                                                                               #
#  WriteNGramsToFileFormattedRDataSet(NGramsList, filename)                     #
#                                                                               #
#  Write to given file the results formatted as an r language data set.         #
#                                                                               #
#################################################################################
def OutputNGramsFormattedRDataSet(NGramsList, filename):
    file = open(filename, "w");
    file.write("occurrences word1 word2 word3\n")
    for ngram in NGramsList:
        file.write(ngram)
        file.write('\n')

    file.close()


