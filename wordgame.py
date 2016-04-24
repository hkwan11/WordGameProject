import sys
import Heap import *

vertexDict = {}

def main():
    agrumentList = sys.argv
##    if len(sys.argv) != 2:
##        print("ERROR - Enter correct parameters - wordgame.py [fileName]")
##        return
##    fileName = sys.argv[1]

    #doesn't really run on the full file
    fileName = "5lw-s.dat"
    
    try:
        #try to read in file
        file = open(fileName, "r")
        
    except IOError:
        print("ERROR - Unable to open specified file " + fileName)
        return

    lines = file.readlines()

    wordGraph = createGraph(vertexDict, lines)

    #Run test based on user input
    
    rerun = runTrial(wordGraph)
    while(rerun):
        rerun = runTrial(wordGraph)
        

def createGraph(vertexDict, lines):
    wordGraph = {}

    pastWordList = [[[] for x in range(5)] for y in range(26)]
    
    for line in lines:
        l = line.split("\n")
        words = l[0].split(" ")

        for word in words:
            if len(word) > 0 and word != "\n":
                try:
                    vertexDict[word]
                except:
                    vertexDict[word] = Vertex(word)
                neighborList = []

                pastWords = {}

                for c in range(len(word)):
                    letterPos = (ord(word[c]) % 26)

                    for pst in pastWordList[letterPos][c]:
                        print("Past Word of " + word + ": " + pst)
                        try:
                            occur = pastWords[pst] + 1
                            pastWords[pst] = occur
                            if occur == 3:
                                pVert = vertexDict[pst]
                                neighborList.append(pVert)
                                wordGraph[pst].append(vertexDict[word])
                                #This was the missing line of
                                #code that messed up our results
                        except KeyError:
                            #print(pst)
                            pastWords[pst] = 1
                        #print(pastWords)
                        
                    pastWordList[letterPos][c].append(word)
                #print(neighborList)
                
##                for k in wordGraph:
##                    missScore = getMissScore(word, k, len(word))
##
##                    if missScore != -1:
##                        vertexK = Vertex(k)
##                        neighborList.append(vertexK)
##                        wordGraph[k].append(v)
                try:
                    wordGraph[word].append(neighborList)
                except KeyError:
                    wordGraph[word] = neighborList

    return wordGraph

def getMissScore(w1, w2, wLen):
    missScore = 0

    for i in range(wLen):
        #print("WORD IS: " + w1)
        if w1[i] != w2[i]:
            missScore = missScore + 1

    if missScore == 2:
        return 5
    elif missScore == 1:
        return 1
    elif missScore == 0:
        return 0
    else:
        return -1

def playGame(wordGraph, rootWord, targetWord):
    #iterate through all keys in the graph
    print("TERE")#for v in wordGraph:
        
        

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

def dijkstra(graph, root, target):
    #sets root
    r = vertexDict[root]

    #initialize all vertices
    for word in graph:
        v = vertexDict[word]
        v.setKey(-1)
        v.setPredecessor(None)

    #initialize the root to 0
    r.setKey(0)
    #INITIALIZE HEAP (PRIORITY QUEUE)
    priorityHeap = Heap()
    for v in vertexDict:
        priorityHeap.insert(vertexDict[v])

    #While priority queue is not empty
    while priorityQueue.getHeapsize() > 0:
        #remove min of heap
        u = priorityHeap.removeMin()

        #iterate through the adjacency list of u
        for v in graph[u.getName()]:
            uKey = u.getKey() + weight(u,v)
            if uKey < v.getKey():
                v.setPredecessor(u)
                v.setKey(uKey)
                priorityHeap.heapifyUp(v.getHandle())


def weight(u, v):
    return u.getKey() + v.getKey()


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

    def setKey(self, key)
        self.key = key

    def getKey(self):
        return self.key

    def getWord(self):
        return self.word
main()
