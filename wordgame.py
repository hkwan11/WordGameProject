import sys

def main():
    agrumentList = sys.argv
    if len(sys.argv) != 2:
        print("ERROR - Enter correct parameters - wordgame.py [word1] [word2]")
        return
    
    fileName = sys.argv[1]
    
    try:
        #try to read in file
        file = open(fileName, "r")
        
    except IOError:
        print("ERROR - Unable to open specified file " + fileName)
        return

    ### -----CREATE GRAPH------ ###

    lines = fileName.readlines()

    wordGraph = [[]]
    
    for line in lines:
        v = Vertex(line)
        print(line)

    #Run test based on user input
    runTrial(wordGraph)
            

def runTrial(wordGraph):
    #asks the user to input word to check
    try:
        userWord = input("Please enter a five-letter word to check: ")

        #makes sure word is in consistent case
        userWord = userWord.toUpper()

        if len(userWord) != 5:
            raise ValueError("Whoops! Didn't enter a five letter word")
        
    #if incorrect length, it is caught
    except ValueError as err:
        print(err.args)

    #TODO: Check the given word in the graph and list out neighbors with\
        #weights for each in parentheses. If not in graph, print message

    ### ----Ask User If they desire to do another trial---- ###
    while(True):
        doTrial = input("Do you wish to complete another trial? (Y/Yes, N/No) ")
        doTrial = doTrial.toUpper()

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

    def getHandle():
        return self.handle

    def setHandle(handle):
        self.handle = handle

    def getKey():
        return self.key

