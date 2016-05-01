import sys
from Heap import *

vertexDict = {}

def main():
    #Gets the command line argument for the input file name
    agrumentList = sys.argv
    if len(sys.argv) != 2:
        print("ERROR - Enter correct parameters - wordgame.py [fileName]")
        return
    fileName = sys.argv[1]

    #This is for when not using command line arguments
        #fileName = "5lw.dat"

    try:
        #try to read in file
        file = open(fileName, "r")

    except IOError:
        print("ERROR - Unable to open specified file " + fileName)
        return

    #read in all ines from file
    lines = file.readlines()
    wordGraph = createGraph(vertexDict, lines)

    #Run the trial continously until ended
    rerun = runGameTrial(wordGraph)
    while(rerun):
        rerun = runGameTrial(wordGraph)

    #Run test based on user input --- FOR PART 1
##
##    rerun = runTrial(wordGraph)
##    while(rerun):
##        rerun = runTrial(wordGraph)


def createGraph(vertexDict, lines):
    #initialize graph of words
    wordGraph = {}

    #initialize empty 2d list of empty lists to store past
    #   words put in the graph. The dimensions representing
    #   every possible letter, and each letter position in
    #   a word
    pastWordList = [[[] for x in range(5)] for y in range(26)]

    #iterate through every line in the input file
    for line in lines:
        #split by words
        l = line.split("\n")
        words = l[0].split(" ")

        #iterate through every word in file
        for word in words:
            #if it's an actual word
            if len(word) > 0 and word != "\n":
                #see if it's in our dictionary of vertices
                try:
                    vertexDict[word]
                except:
                    #if not, add it
                    vertexDict[word] = Vertex(word)
                #initialize an empty list to stor current word's neighbors
                neighborList = []

                #initialize dictionary used to keep track of similarly spelled
                #   words
                pastWords = {}

                #iterate through every character in word
                for c in range(len(word)):
                    #get value of letter in order to access correct 2d list pos
                    letterPos = (ord(word[c]) % 26)

                    #check every word that has had a letter in the same position
                    for pst in pastWordList[letterPos][c]:

                        try:
                            #if we've run into this word before, increment counter
                            occur = pastWords[pst] + 1
                            pastWords[pst] = occur
                            #if we've run into the word 3 times, they differ by at
                            #   most 2 letters
                            if occur == 3:
                                #Add vertex to dictionary
                                pVert = vertexDict[pst]
                                #calculate score for difference between words
                                missScore = getMissScore(word, pVert.getWord(), len(word))

                                #store the word in neighborlist and add back
                                vertexDict[pst].setKey(missScore)
                                neighborList.append(vertexDict[pst])
                                wordGraph[pst].append(vertexDict[word])
                        except KeyError:
                            #if not, add it to pastWords and intialize to 1
                            pastWords[pst] = 1

                    #Add word to the list in that given letter/pos slot
                    pastWordList[letterPos][c].append(word)

                try:
                    #if word already in wordgraph, append
                    wordGraph[word].append(neighborList)
                except KeyError:
                    #if not, initialize
                    wordGraph[word] = neighborList

    #return wordGraph
    return wordGraph


def getMissScore(w1, w2, wLen):
    #initialize score to 0
    missScore = 0

    #count the number of letters differing between
    #   The two words
    for i in range(wLen):
        if w1[i] != w2[i]:
            missScore = missScore + 1

    #return an appropriate score based off of differences
    if missScore == 2:
        return 5
    elif missScore == 1:
        return 1
    elif missScore == 0:
        return 0
    else:
        return -1


def runTrial(wordGraph):
    #asks the user to input word to check
    try:
        userWord = input("Please enter a five-letter word to check: ")

        #makes sure word is in consistent case
        userWord = userWord.upper()

        if len(userWord) != 5:
            raise ValueError("Whoops! Didn't enter a five letter word!")
        else:
            print()

            #Test to see if user word in the neighbor list
            try:
                neighborList = wordGraph[userWord]

                print("The neighbors of "+userWord+" are:")
                numTotal = 0

                for v in neighborList:
                    A = [[-1 for x in range(4)] for x in range(4)]
                    #score = LCS_len(userWord, v.getWord(), A)
                    score = getMissScore(userWord, v.getWord(), 5)

                    if numTotal % 6 == 0:
                        print()
                    print(v.getWord() + " (" + str(score) + ") ", end = " ")
                    numTotal = numTotal + 1

            except KeyError:
                print(userWord + " is not in the graph!")
                return 1

    #if incorrect length, it is caught
    except ValueError as err:
        print(err.args)
        return 1

    ### ----Ask User If they desire to do another trial---- ###
    doTrial = input("\nDo you wish to complete another trial? (Y/Yes, N/No) ")
    doTrial = doTrial.upper()
    #print(doTrial)

    if doTrial == "Y" or doTrial == "YES":
        return 1
    elif doTrial == "N" or doTrial == "NO":
        return 0
    else:
        print("Sorry, that is not a valid input")

def dijkstra(adjGraph, root):
    #initialize all vertices
    for word in adjGraph:
        vertexDict[word].setKey(float('inf'))
        vertexDict[word].setPredecessor(None)

    #initialize the root to 0
    vertexDict[root].setKey(0)
    #INITIALIZE HEAP (PRIORITY QUEUE)
    priorityHeap = Heap()
    for v in vertexDict:
        priorityHeap.insert(vertexDict[v])

    #While priority queue is not empty
    while priorityHeap.getHeapsize() > 0:
        #remove min of heap
        u = priorityHeap.removeMin()

        #iterate through the adjacency list of u
        for v in adjGraph[u.getWord()]:

            uKey = vertexDict[u.getWord()].getKey() + weight(u,v)

            #relax the graph
            if uKey < vertexDict[v.getWord()].getKey():
                vertexDict[v.getWord()].setPredecessor(vertexDict[u.getWord()])

                vertexDict[v.getWord()].setKey(uKey)
                priorityHeap.heapifyUp(vertexDict[v.getWord()].getHandle())


    return priorityHeap

def runGameTrial(wordGraph):
    #Ask for both input words to find a path between them
    rootWord = input("\nEnter the first five-letter word: ").upper()
    checkWord = input("\nEnter the second five-letter word: ").upper()

    #find and print path and best score
    if(findPath(wordGraph, rootWord, checkWord)):
        return 1

    ### ----Ask User If they desire to do another trial---- ###
    doTrial = input("\nDo you wish to complete another trial? (Y/Yes, N/No) ")
    doTrial = doTrial.upper()
    #print(doTrial)

    if doTrial == "Y" or doTrial == "YES":
        return 1
    elif doTrial == "N" or doTrial == "NO":
        return 0
    else:
        print("Sorry, that is not a valid input")


def findPath(wordGraph, word1, word2):

    #Check to see both words are in the graph!
    try:
        vertexDict[word1]
    except KeyError:
        print("WHOOPS! - " + word1 + " isn't in the graph!")
        return 1

    try:
        vertexDict[word2]
    except KeyError:
        print("WHOOPS! - " + word2 + " isn't in the graph!")
        return 1

    #First call dijkstra making word1 as root
    dijkstra(wordGraph, word1)
    #Now all adjacencies should be correct

    #Get the vertex for word2 and store it's distance score
    curVertex = vertexDict[word2]
    bestScore = curVertex.getKey()

    print("The best score for " + word1 + " to " + word2 + " is " + str(bestScore) + " points.")

    #initialize pathString to keep track of words in path
    pathString = ""

    #While we haven't reached the end of the path, store current word and go to next
    while(curVertex != None):
        pathString = curVertex.getWord() + " " + pathString

        curVertex = curVertex.getPredecessor()

    print("\n\t"+pathString)

    return 0


def weight(u, v):
    #return the weight of the two words (obtained via getting the miss score)
    return getMissScore(vertexDict[u.getWord()].getWord(), vertexDict[v.getWord()].getWord(), len(v.getWord()))


class Vertex:
    """Vertex Class"""

    def __init__(self, word):
        self.key = -1
        self.handle = -1
        self.predecessor = None
        self.word = word


    def getPredecessor(self):
        return self.predecessor

    def setPredecessor(self, pred):
        self.predecessor = pred

    def getHandle(self):
        return self.handle

    def setHandle(self, handle):
        self.handle = handle

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def getWord(self):
        return self.word

    def __str__(self):
        return "(" + self.word + ": KEY[" + str(self.key) + "] HANDLE[" + str(self.handle) + "])"

    def __repr__(self):
        return self.__str__()

main()
