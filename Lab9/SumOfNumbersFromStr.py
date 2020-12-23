def getSumOfNumbersFromStr(strWithNumbers):
    currentNumber = '0'
    sum = 0
    for i in range(0, len(strWithNumbers)):
        if strWithNumbers[i].isdigit():
            currentNumber += strWithNumbers[i]
        else:
            sum += int(currentNumber)
            currentNumber = '0'
        if i==len(strWithNumbers)-1:
            sum += int(currentNumber)
    return sum
