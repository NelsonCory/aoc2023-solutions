# Day 3: Gear Rations
# Problem: https://adventofcode.com/2023/day/3
#

def readFile():
    fileInput = open("input.txt")
    fileData = fileInput.read()
    fileInput.close()
    return fileData


# clean data
# need to preserve adjacency, no data can be removed
def cleanData(fileData):
    cleanData = []
    splitData = fileData.split("\n")
    for i in splitData:
        cleanData.append(list(i))
    return cleanData

#return a list of part numbers which are adjacent to at least one symbol
# adjacency may be diagonal
def findPartNumbers(data):
    #strategy - identify coordinates for numbers,
    #           - sweep area around number to see if adjacent to a symbol
    
    partNumbers = []
    for i in range(len(data)):
        currNum = ""
        arrNums = []
        for j in range(len(data[0])): #assumes data has rectangular shape
            if data[i][j].isnumeric():
                currNum += data[i][j]
                arrNums.append([i,j])
            else:
                if len(currNum > 0):
                    #perform adjacency test for number
                    
                    # if adjacent to a symbol, add number to partNumbers
                    pass
                    currNum = ""
                    arrNums = []
    
def determineAdjacency(data, numberList):
    for element in numberList:
        #check above (check an additional 1 left and right for diagonals)
        
        #check below  (check an additional 1 left and right for diagonals)
        
        #check left
        
        #check right
        pass


def main():
    fileData = readFile()
    organizedData = cleanData(fileData)
    #print(organizedData)
    input()
    
main()