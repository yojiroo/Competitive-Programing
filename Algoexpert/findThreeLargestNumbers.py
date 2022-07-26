def findThreeLargestNumbers(array):
    threelargetst = [None,None,None]
    for num in array:
        updateLargest(threelargetst,num)
    return threelargetst

def updateLargest(threelargest,num):
    if threelargest[2] is None or num > threelargest[2]:
        ShiftAndUpdate(threelargest,num,2)
    elif threelargest[1] is None or num > threelargest[1]:
        ShiftAndUpdate(threelargest,num,1)
    elif threelargest[0] is None or num > threelargest[0]:
        ShiftAndUpdate(threelargest,num,0)

def ShiftAndUpdate(array,num,idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i+1]

print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))