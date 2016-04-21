import sys

def main():
    agrumentList = sys.argv
##    if len(sys.argv) != 2:
##        print("ERROR - Enter correct parameters - wordgame.py [word1] [word2]")
##        return
##    fileName = sys.argv[1]

    #doesn't really run on the full file
    fileName = "5lw.dat"
    
    try:
        #try to read in file
        file = open(fileName, "r")
        
    except IOError:
        print("ERROR - Unable to open specified file " + fileName)
        return

    lines = file.readlines()

    wordGraph = createGraph(lines)

    #Run test based on user input
    
    rerun = runTrial(wordGraph)
    while(rerun):
        rerun = runTrial(wordGraph)
        

def createGraph(lines):
    wordGraph = {}

    pastWordList = [[[] for x in range(5)] for y in range(26)]
    
    for line in lines:
        l = line.split("\n")
        words = l[0].split(" ")

        for word in words:
            if len(word) > 0 and word != "\n":
                v = Vertex(word)
                neighborList = []

                pastWords = {}

                for c in range(len(word)):
                    letterPos = (ord(word[c]) % 26)

                    for pst in pastWordList[letterPos][c]:
                        try:
                            occur = pastWords[pst] + 1
                            pastWords[pst] = occur
                            if occur >= 3:
                                pVert = Vertex(pst)
                                neighborList.append(pVert)
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

                print("The neighbors of SHALE are:")
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
        
    #if incorrect length, it is caught
    except ValueError as err:
        print(err.args)

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


#Name: LCS_len
#Purpose: To calculate and return the length of a longest-common-subsequence
#   of the given strings
#
#Input: Strings X and Y. Array of values A
#Output: Length of a longest-common-subsequence of the given strings
def LCS_len(X, Y, A):
    #Sets i and j as the last positions in the given strings
    i = len(X) - 1
    j = len(Y) - 1

    #if we haven't run into the end of the string
    if j >=0 and i >= 0:
        #if the last characters of both strings aren't the same
        if X[i] != Y[j]:

            #check to see if left solution already stored
            if i > 0 and A[i-1][j] != -1:   
                answer1 = A[i-1][j]
            else:
                #get it and store it if not
                answer1 = LCS_len(X[0:i], Y, A)
                A[i-1][j] = answer1

            #check to see if right solution already stored
            if j > 0 and A[i][j-1] != -1:
                answer2 = A[i][j-1]
            else:
                #get it and store it if not
                answer2 = LCS_len(X, Y[0:j], A)
                A[i][j-1] = answer2

            #return the max value of both sub-calls
            return max(answer1, answer2)
        else:
            #if both characters are the same

            #check to see if recursive call has already been made
            if i > 0 and j > 0 and A[i-1][j-1] != -1:
                retAnswer = A[i-1][j-1]
            else:
                #if not, call it and store it
                retAnswer = LCS_len(X[0:i], Y[0:j], A)
                A[i-1][j-1] = retAnswer

            #return incremented value
            return 1 + retAnswer
    else:
        #if the end of the string, not a match so return a 0
        return 0


class Vertex:
    """Vertex Class"""

    def __init__(self, word):
        self.key = -1
        self.handle = -1
        self.word = word

    def getHandle(self):
        return self.handle

    def setHandle(self, handle):
        self.handle = handle

    def getKey(self):
        return self.key

    def getWord(self):
        return self.word

