import sys

def main():
    agrumentList = sys.argv
##    if len(sys.argv) != 2:
##        print("ERROR - Enter correct parameters - wordgame.py [word1] [word2]")
##        return
##    fileName = sys.argv[1]
    fileName = "5lw-s.dat"
    
    try:
        #try to read in file
        file = open(fileName, "r")
        
    except IOError:
        print("ERROR - Unable to open specified file " + fileName)
        return

    lines = file.readlines()

    wordGraph = createGraph(lines)

    #Run test based on user input
    runTrial(wordGraph)


def createGraph(lines):
    wordGraph = {}
    
    for line in lines:
        words = line.split(" ")

        for word in words:
            v = Vertex(word)
            A = [[-1 for x in range(5)] for x in range(5)]
            neighborList = []
            
            for k in wordGraph:
                lcsScore = 5 - LCS_len(word, k, A)

                if lcsScore >= 3:
                    neighborList.append(k)
                    wordGraph[k].append(v)
            try:
                wordGraph[word].append(neighborList)
            except KeyError:
                wordGraph[word] = neighborList

    return wordGraph
            

def runTrial(wordGraph):
    #asks the user to input word to check
    try:
        userWord = input("Please enter a five-letter word to check: ")

        #makes sure word is in consistent case
        userWord = userWord.upper()

        if len(userWord) != 5:
            raise ValueError("Whoops! Didn't enter a five letter word")
        
    #if incorrect length, it is caught
    except ValueError as err:
        print(err.args)

    #Test to see if user word in the neighbor list
##    try:
##        neighborList = wordGraph[userWord]
##
##        for v in neighborList:
##            A = [[-1 for x in range(4)] for x in range(4)]
##            score = LCS_len(userWord, v.getKey(), A)
##            print(v.getKey() + " (" + str(score) + ") ", end = " ")
##        
##    except KeyError:
##        print(userWord + " is not in the graph!")

    ### ----Ask User If they desire to do another trial---- ###
    while(True):
        doTrial = input("Do you wish to complete another trial? (Y/Yes, N/No) ")
        doTrial = doTrial.upper()

        if doTrial is "Y" or doTrial is "YES":
            runTrial()
        elif doTrial is "N" or doTrial is "NO":
            break
        else:
            print("Sorry, that is not a valid input")


class Vertex:
    """Vertex Class"""

    def __init__(self, key):
        self.key = key
        self.handle = -1

    def getHandle(self):
        return self.handle

    def setHandle(self, handle):
        self.handle = handle

    def getKey(self):
        return self.key

