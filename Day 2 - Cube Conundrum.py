# Day 2: Cube Conundrum
# Problem: https://adventofcode.com/2023/day/2
#

def readFile():
    fileInput = open("input.txt")
    fileData = fileInput.read()
    fileInput.close()
    return fileData

#returns a multidimensional array, each position is an array of dictionaries, where each dictionary represents the results of a drawing
# and each array of dictionaries represents the results of a game
def cleanData(data):
    dataList = data.split("\n") #seperate 
    dataDictArr = []
    for i in range(len(dataList)):
        dataList[i] = dataList[i].split(":")[1]
        dataList[i] = dataList[i].split(";") # split each game into rounds

        #each game, construct a list of dictionaries where each dictionary
        # contains the result of the round 
        for game in range(len(dataList[i])):
            resultsArr = []
            #gameInfo = dataList[game].split() # list, where results of each item are results of round
            gameInfo = [g.split(",") for g in dataList[i]] # seperate each round into drawings
            for roundIndex in range(len(gameInfo)):
                gameInfo[roundIndex] = [r.strip() for r in gameInfo[roundIndex]] #strip leading white space from each drawing
                tempDict = {}
                for r in gameInfo[roundIndex]:
                    temp = r.split()
                    #print(temp)
                    tempDict[temp[1]] = int(temp[0]) # temp[1]: color, temp[0]:value
                resultsArr.append(tempDict.copy())
        dataDictArr.append(resultsArr.copy())
    return dataDictArr #my baby, its hideous

def determineIfReal(gameRound):
    maxDict = {"red":12,"green":13,"blue":14}
    for drawing in gameRound:
        for key in drawing.keys():
            if(drawing[key] > maxDict[key]):
                return False
    return True

def main():
    data = readFile()
    data = cleanData(data)
    
    # part 1
    sumOfRealGames = 0
    for gameRound in range(len(data)):
        if(determineIfReal(data[gameRound])):
            sumOfRealGames += gameRound+1
    print(sumOfRealGames)
    
main()