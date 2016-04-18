import sys

def main():
    agrumentList = sys.argv
    if len(sys.argv) != 1:
        print("ERROR - enter correct number of parameters")
        exit()
    
    fileName = sys.argv[1]
    
    try:
        #try to read in file
        file = open(fileName, "r")
        
    except IOError:
        print("ERROR - Unable to open specified file " + fileName)
        exit()
    
    lines = fileName.readlines()
    
    for line in lines:
        
