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
                if len(currNum) > 0:
                    #perform adjacency test for number and add to partNumbers if adjacent
                    if determineAdjacency(data, arrNums):
                        partNumbers.append(int(currNum))
                    
                    currNum = ""
                    arrNums = []
    return partNumbers

def charIsSymbolic(char):
    return (not char.isnumeric()) and char != "."
    

def determineAdjacency(data, numberList):
    for index in numberList: #[x,y]
        x = index[0]
        y = index[1]
        #check above (check an additional 1 left and right for diagonals)
        if index[1] != 0:
            if charIsSymbolic(data[x][y-1]): #is not checking left or right
                return True
            if index[0] != 0:
                if charIsSymbolic(data[x-1][y-1]): #check NW diagonal
                    return True
            if index[0] != len(data[0])-1:
                if charIsSymbolic(data[x+1][y-1]): #check NE diagonal
                    return True
        #check below  (check an additional 1 left and right for diagonals)
        if index[1] != len(data) - 1:
            if charIsSymbolic(data[x][y+1]):
                return True
            
            if index[0] != 0:
                if charIsSymbolic(data[x-1][y+1]): #check SW diagonal
                    return True
            if index[0] != len(data[0])-1:
                if charIsSymbolic(data[x+1][y+1]): #check NE diagonal
                    return True
        #check left
        if index[0] != 0:
            if charIsSymbolic(data[x-1][y]):
                return True
        #check right
        if index[0] != len(data[0])-1:
            if charIsSymbolic(data[x+1][y]):
                return True
    return False

def main():
    fileData = readFile()
    organizedData = cleanData(fileData)
    validParts = findPartNumbers(organizedData)
    print(validParts)
    print(sum(validParts))
   
    
main()