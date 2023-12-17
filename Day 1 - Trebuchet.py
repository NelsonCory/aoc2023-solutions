#Day 1: Trebuchet?!
# Problem: https://adventofcode.com/2023/day/1
#

def readFile():
    fileInput = open("input.txt")
    fileData = fileInput.read()
    fileInput.close()
    return fileData

def cleanData(data):
    arr = data.split("\n")
    return arr

# two-pointer solution
# find first and last value, going in either direction
# this assumes at least one digit is in the string
def findValues(data):
    numList = []
    #print(data)
    for word in data:
        low_index = 0
        high_index = len(word)-1
        first_digit = None
        second_digit = None
        for i in range(len(word)):
            low_index = i
            high_index = len(word) - i - 1
            if (first_digit == None):
                # check if next char is a digit
                if word[low_index].isnumeric():
                    first_digit = word[low_index]
            if (second_digit == None):
                #check if next char is a digit
                if word[high_index].isnumeric():
                    second_digit = word[high_index]
        numList.append(int(first_digit+second_digit))
    return numList
        
            
def calculate_sum(arr):
    return sum(arr)

def findDigitsByText(data):
    digitList = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    #strategy
    # - create a buffer of text as long as text is not numeric, check for if value is in digit list
    
    numList = []
    for word in data:
        frontBuffer = ""
        backBuffer = ""
        first_digit = None
        second_digit = None
        for i in range(len(word)):
            high_index = len(word) - i - 1
            if first_digit == None and not word[i].isnumeric():
                frontBuffer += word[i]
                for digit in digitList:
                    if digit in frontBuffer:
                        first_digit = digit   
            elif word[i].isnumeric() and first_digit == None:
                first_digit = word[i]
            if second_digit == None and not word[high_index].isnumeric():
                backBuffer = word[high_index] + backBuffer
                for digit in digitList:
                    if digit in backBuffer:
                        second_digit = digit
            elif word[high_index].isnumeric() and second_digit == None:
                second_digit = word[high_index]
        first_digit = convertToDigit(first_digit,digitList)
        second_digit = convertToDigit(second_digit,digitList)
        numList.append(int(first_digit + second_digit))
    return numList
            
            
                
def convertToDigit(value,digitList):
    if value.isnumeric():
        return value
    else:
        return str(digitList.index(value))
    

def main():
    data = readFile()
    data = cleanData(data)
    
    #part 1
    numList = findValues(data)
    sumOfList = calculate_sum(numList)
    print("Part 1 -",sumOfList)
    
    #part 2
    numList = findDigitsByText(data)
    sumOfList = calculate_sum(numList)
    print("Part 2 -",sumOfList)

main()