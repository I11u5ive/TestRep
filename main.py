#String functions:
def stringLen(newStr = ''):
    return len(newStr)

def concatStrings(newStr1 = '', newStr2 = ''):
    return newStr1 + newStr2

#Int/float functions:
def powFunction(number = 0):
    return pow(number, 2)                       #can be written as: return number * number

def sumFunction(number1 = 0, number2 = 0):
    return number1 + number2

def divisionFunction(number1 = 0, number2 = 1):
    try:
        return number1 / number2
    except ZeroDivisionError:
        return  'Divisor cannot be 0'

#List functions:
def averageListValue(newList = [0]):
    try:
        return sum(newList) / len(newList)
    except ZeroDivisionError:
        return 'List length must be at least 1'

def commonElementsInList(newList1 = [0], newList2 = [0]):
    if len(newList1) > 0 and len(newList2) > 0:     #can be written through custom exception
        return list(set(newList1) & set(newList2))  #can be written as: return [el for el in newList1 if el in newList2]
    return 'Length of lists must be at least 1'

#Dictionary functions:
def retKeysFunction(newDict = {0: 0}):
    return newDict.keys()

def combineTwoDicts(newDict1 = {0: 0}, newDict2 = {0: 0}):
    return {**newDict1, **newDict2}                 #can be written as: return newDict1 | newDict2
                                                    #or as: newDict1.update(newDict)
                                                    #       return newDict1

#Set functions:
def combineTwoSets(newSet1 = {0}, newSet2 = {0}):
    return newSet1 | newSet2                        #can be written as: return newSet1.union(newSet2)
                                                    #or as:
                                                    #   newSet1.update(newSet2)
                                                    #   return newSet1

def isSubsetFunction(newSet1 = {0}, newSet2 = {0}):
    return f'{newSet1} is subset of {newSet2}' if newSet1.issubset(newSet2) else f'{newSet2} is subset of {newSet1}' if newSet2.issubset(newSet1) else 'There are no subsets'

#Conditions and Loops functions:
def evenOrUneven(number = 0):
    return f'{number} is even' if number % 2 == 0 else f'{number} is uneven'

def evenList(newList = [0]):
    return [el for el in newList if el % 2 == 0]

#String functions prints:
print('The string length is ', stringLen('Some string'))
print('The new string is: ', concatStrings('Some string ', 'is the new string'))

#Int/float functions prints:
print('The pow is: ', powFunction(3))
print('The sum is: ', sumFunction(1, 2))
print('The division is: ', divisionFunction(9, 2.7))
print('Exception in divisionFunction was caught: ', divisionFunction(3, 0))

#List functions prints:
print('The average value of list is: ', averageListValue([3, 3, 3]))
print('The exception in averageListValue is caught: ', averageListValue([]))
print('The intersections between lists are: ', commonElementsInList([1, 2, 3, 4], [5, 2, 3, 6]))
print('The empty list condition is caught in commonElementsInList function: ', commonElementsInList([],
                                                                                                    []))

#Dictionary functions prints:
print('The keys are: ', retKeysFunction({'0': 'zero', '1': 'one', '2': 'two'}))
print('The combined dictionary is: ', combineTwoDicts({'0': 'zero', '1': 'one', '2': 'two'},
                                                      {'3': 'three', '4': 'four', '5': 'five'}))
#Set functions prints:
print('The combined set is: ', combineTwoSets({0, 1, 2}, {3, 4, 5}))
print(isSubsetFunction({0, 1, 2}, {0, 1, 2, 3, 4, 5}))
print(isSubsetFunction({0, 1, 2, 3, 4, 5}, {3, 4, 5}))
print(isSubsetFunction({0, 1, 2, 3}, {3, 4, 5}))

#Conditions and Loops functions prints:
print(evenOrUneven(1))
print(evenOrUneven(2))
print('There is even list: ', evenList([0, 1, 2, 3, 4, 5]))

#Lambda function:
lambdaEvenOrUneven = lambda number : 'even' if number % 2 == 0 else 'uneven'
print('Lambda number is ',lambdaEvenOrUneven(1))
print('Lambda number is ',lambdaEvenOrUneven(2))
