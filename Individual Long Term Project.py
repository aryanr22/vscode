#-----------------------------------------------------------------------------------------------
# Name: Individual Long Term Project (python.py)
# Purpose: To visualize and manipulate data sets using different aspects of Python
#
# References: 	This program uses the NumPy/SciPy style of documentation as found
#				here: https://numpydoc.readthedocs.io/en/latest/format.html with
#				some minor modifications based on Python 3 function annotations
#				(the -> notation).
#
# Author: Aryan Rahman
# Created: 04-October-2023
# Updated: 15-November-2023
#-----------------------------------------------------------------------------------------------
import csv

import time

import numpy

from BasketBallPlayer import BasketBallPlayer

from Scorer import Scorer

from Defender import Defender

# Creating arrays for each row in the "Raptor New Data" csv file (int = truncated number, decimal = the leftover decimals)
name = []
posessions = []
minutesPlayed = []

intRaptorOffense = []
decimalRaptorOffense = []

intRaptorDefense = []
decimalRaptorDefense = []

intRaptorTotal = []
decimalRaptorTotal = []

# Opening the main RAPTOR csv file
with open('RAPTOR 2022-23.csv') as file:
	rows = csv.DictReader(file)

	# Going through first three rows, converting data types to string, integer, and integer respectively, for all values in the rows
	for row in rows:
		nameStr = str(row['player_name'])
		posessionsInt = int(row['poss'])
		minutesInt = int(row['mp'])

		# Using integer division and modulo to get a nice integer value, and leftover decimals for RAPTOR offense, defense, and total
		sO = float(row['raptor_offense']) // 1
		dO = float(row['raptor_offense']) % 1

		sD = float(row['raptor_defense']) // 1
		dD = float(row['raptor_defense']) % 1

		sT = float(row['raptor_total']) // 1
		dT = float(row['raptor_total']) % 1


		# Taking each value from above, and adding them to their respective arrays, spliting up, organizing, and completing the conversion process
		name.append(nameStr)
		posessions.append(posessionsInt)
		minutesPlayed.append(minutesInt)

		intRaptorOffense.append(sO)
		decimalRaptorOffense.append(dO)

		intRaptorDefense.append(sD)
		decimalRaptorDefense.append(dD)

		intRaptorTotal.append(sT)
		decimalRaptorTotal.append(dT)


# Setting up the 2-d array with all new converted values
newValues = []

# Incorporating each 1-d array from above, one value from each array at a time, then creating a new row for a new player
for x in range(len(intRaptorOffense)):
    row = [name[x], posessions[x], minutesPlayed[x], intRaptorOffense[x], decimalRaptorOffense[x], intRaptorDefense[x], decimalRaptorDefense[x], intRaptorTotal[x], decimalRaptorTotal[x]]
    newValues.append(row)


# Opening new csv file to write all new values into
with open(r'RAPTOR 2022-23 With New Data.csv', 'w', newline="\n") as f:
    wr = csv.writer(f)

    #writing headers and values into this csv file
    wr.writerow(['name', 'posessions', 'minutes', 'offense_shortened', 'offense_decimal', 'defense_shortened', 'defense_decimal', 'total_shortened', 'total_decimal',])
    wr.writerows(newValues)


# Next set of arrays for the name, posessions, minutes played, and rounded offense, defense, and total taken from the "RAPTOR New Data" csv file
shortName = []
shortPosessions = []
shortMinutesPlayed = []

shortOffense = []
shortDefense = []
shortTotal = []

# Creating a 2-d array for these values to be placed into
values = []

# Opening "RAPTOR New Data" csv file
with open('RAPTOR 2022-23 With New Data.csv') as file:
	rows = csv.DictReader(file)

	# Taking values from each row, converting types, and placing into their respective 1-d arrays
	for row in rows:
		name = str(row['name'])
		posessions = int(row['posessions'])
		minutes = int(row['minutes'])

		oS = float(row['offense_shortened'])
		dS = float(row['defense_shortened'])
		tS = float(row['total_shortened'])

		shortName.append(name)
		shortPosessions.append(posessions)
		shortMinutesPlayed.append(minutes)

		shortOffense.append(oS)
		shortDefense.append(dS)
		shortTotal.append(tS)

# Taking all values from the 6 different 1-d arrays
for x in range(len(intRaptorOffense)):

    # Checking if the player's total minutes played is over 1500, then adding all of their main values (name, possessions, minutes, offense, defense, total) if is true
	if(shortMinutesPlayed[x] >= 1500):
		row = [shortName[x], shortPosessions[x], shortMinutesPlayed[x], shortOffense[x], shortDefense[x], shortTotal[x]]
		values.append(row)
	else:
		x +=1

# Opening "Shortened RAPTOR" csv file to place the main values of the players with over 2500 total minutes
with open(r'Shortened RAPTOR.csv', 'w', newline="\n") as f:
    wr = csv.writer(f)
    # Headers + incorporating the 2-d array
    wr.writerow(['name', 'posessions', 'minutes', 'offense', 'defense', 'total'])
    wr.writerows(values)


# Another set of arrays to put these selective player's values into
smallestName = []
smallestPosession = []
smallestMinutes = []
smallestOffense = []
smallestDefense = []
smallestTotal = []

# Opening "Shortened RAPTOR" csv file
with open('Shortened RAPTOR.csv') as newfile:
	rows = csv.DictReader(newfile)

	# Taking all values in each row, converting types, and assigning to their respective 1-d arrays
	for row in rows:
		name = str(row['name'])
		posessions = int(row['posessions'])
		minutes = int(row['minutes'])

		o = float(row['offense'])
		d = float(row['defense'])
		t = float(row['total'])

		smallestName.append(name)
		smallestPosession.append(posessions)
		smallestMinutes.append(minutes)

		smallestOffense.append(o)
		smallestDefense.append(d)
		smallestTotal.append(t)


# Creating a 2-d array which combines each of these 1-d arrays, taking one value at a time, then beginning a new row for each player
nextValues = []
for x in range(len(smallestName)):
    row = [smallestName[x], smallestPosession[x], smallestMinutes[x], smallestOffense[x], smallestDefense[x], smallestTotal[x]]
    nextValues.append(row)


# Creating a 2d array with each of the objects (players) and their attributes (statistics)
playerObjects = []



# Unpacking the 2-d array with all of the selective players' (those with >1500 min played) values, creating an object for each player, and storing it in the "playerObjects 2-d array"
for data in nextValues:
	name, posessions, minutes, offense, defense, total = data
	player = BasketBallPlayer(name, posessions, minutes, offense, defense, total)
	playerObjects.append(player)


# Printing all names that qualified for >1500 minutes played, thus are objects of the BasketBallPlayer Class
#for player in playerObjects:
#   print(player.name)

# Taking user input to find a player to search from selective list
nameInput = input("Enter a Player Name: ")

# Comparing user input to selective list of players, then printing stats if it matches
for player in playerObjects:
    if nameInput != player.name:
       print(f"[PLAYER NOT FOUND] {player.name} found instead. Trying again...")
    elif nameInput == player.name:
       print("[PLAYER FINALLY FOUND]")
       print(player)
       player.possPerMin()
       player.possPerGame()
       player.minPerGame()
       player.projectedSalary()
       break


# Taking players from NextValues, creating new csv files that are ordered


# Ordered Raptor Offense - Bubble sort (low to high)


lenOffense = len(smallestOffense)


for y in range(lenOffense):
    for z in range(0, lenOffense - y - 1):
        if smallestOffense[z] > smallestOffense[z + 1]:
            smallestOffense[z], smallestOffense[z + 1] = smallestOffense[z + 1], smallestOffense[z]




# Creating a tracker number to give context to rankings of each value
trackerNumber = []

for a in range(1, lenOffense + 1):
    trackerNumber.append(a)

offenseOrd = []
# Writing to Ordered Offense CSV
for x in range(lenOffense):
    row = [trackerNumber[x], smallestOffense[x]]
    offenseOrd.append(row)

with open(r'Ordered Offense RAPTOR.csv', 'w', newline="\n") as f:
    wr = csv.writer(f)
    # Headers + incorporating the 2-d array
    wr.writerow(['Ranking', 'Offense'])
    wr.writerows(offenseOrd)


# Ordered Raptor Defense - selection sort

lenDefense = len(smallestDefense)


for a in range(lenDefense):
    minIndex = a

    for b in range (a + 1, lenDefense):
         if smallestDefense[b] < smallestDefense[minIndex]:
              minIndex = b
    smallestDefense[a], smallestDefense[minIndex] = smallestDefense[minIndex], smallestDefense[a]




defenseOrd = []
# Writing to Ordered Defense CSV
for x in range(lenDefense):
    row = [trackerNumber[x], smallestDefense[x]]
    defenseOrd.append(row)


with open(r'Ordered Defense RAPTOR.csv', 'w', newline="\n") as f:
    wr = csv.writer(f)
    # Headers + incorporating the 2-d array
    wr.writerow(['Ranking', 'Defense'])
    wr.writerows(defenseOrd)



#Ordered Raptor Total - quick sort, bubble sort, and selection sort

#QUICK--------------------------------------------------------------------------


totalQuickSortStartTime = time.perf_counter_ns()

def quickSort(smallestTotal):
    if len(smallestTotal) <= 1:
       return smallestTotal
    else:
        pivot = smallestTotal[0]
        lessThanPivot = [c for c in smallestTotal[1:] if c <= pivot]
        greaterThanPivot = [c for c in smallestTotal[1:] if c > pivot]
        return(quickSort(lessThanPivot) + [pivot] + quickSort(greaterThanPivot))

quickSortTotal = quickSort(smallestTotal)

totalQuickSortEndTime = time.perf_counter_ns()

totalQuickSortTime = totalQuickSortEndTime - totalQuickSortStartTime

print(f"It took quick sort {totalQuickSortTime} nanoseconds to sort the total raptor ratings from low - high")



# BUBBLE --------------------------------------------------------------------------------------------


totalBubbleSortStartTime = time.perf_counter_ns()

def bubbleSort(array):
	for y in range(len(smallestTotal)):
		for z in range(0, len(array) - y - 1):
			if array[z] > array[z + 1]:
				array[z], array[z + 1] = array[z + 1], array[z]

bubbleSortTotal = bubbleSort(smallestTotal)

totalBubbleSortEndTime = time.perf_counter_ns()

totalBubbleSortTime = totalBubbleSortEndTime - totalBubbleSortStartTime

print(f"It took bubble sort {totalBubbleSortTime} nanoseconds to sort the total raptor ratings from low - high")


# SELECTION ----------------------------------------------------------------------------------------

totalSelectionSortStartTime = time.perf_counter_ns()

def selectionSort(array):
	for a in range(len(smallestTotal)):
		minIndex = a

		for b in range (a + 1, len(array)):
			if array[b] < array[minIndex]:
				minIndex = b
		array[a], array[minIndex] = array[minIndex], array[a]

selectionSortTotal = selectionSort(smallestTotal)
totalSelectionSortEndTime = time.perf_counter_ns()

totalSelectionSortTime = totalSelectionSortEndTime - totalSelectionSortStartTime

print(f"It took selection sort {totalSelectionSortTime} nanoseconds to sort the total raptor ratings from low - high")

#----------------------------------------------------------------------------------------------------------------------


# Creating a tracker number to give context to rankings of each value


totalOrd = []


# Writing to Ordered Offense CSV
for x in range(len(smallestTotal)):
    row = [trackerNumber[x], smallestTotal[x]]
    totalOrd.append(row)

#print(smallestTotal)



with open(r'Ordered Total RAPTOR.csv', 'w', newline="\n") as f:
    wr = csv.writer(f)
    # Headers + incorporating the 2-d array
    wr.writerow(['Ranking', 'Total'])
    wr.writerows(totalOrd)



nameOrd = []
# Writing to Ordered Offense CSV
for x in range(len(smallestName)):
    row = [trackerNumber[x], sortedNames[x]]
    nameOrd.append(row)


with open(r'Ordered Name RAPTOR.csv', 'w', newline='\n') as g:
    wr = csv.writer(g)
    # Headers + incorporating the 2-d array
    wr.writerow(['Tracker', 'Name'])
    wr.writerows(nameOrd)

# creating id's
numpy.random.seed(86)

randomID = numpy.random.randint(1000, 10000, 197)


idRandom = []

for x in range(len(smallestName)):
    row = [randomID[x]]
    idRandom.append(row)

#create loop that incorporates values at a time

idNextValues = []


for x in range(len(smallestName)):
    row = [idRandom[x], smallestName[x], smallestPosession[x], smallestMinutes[x]]
    idNextValues.append(row)

sortedNextValues = sorted(idNextValues, key=lambda x: x[1])



with open(r'Ordered with ID RAPTOR.csv', 'w', newline='\n') as g:
    wr = csv.writer(g)
    # Headers + incorporating the 2-d array
    wr.writerow(['id','name', 'posessions', 'minutes'])
    wr.writerows(sortedNextValues)


# Recursion ------------------------------------------------------------------------------------------------------------

# Fib sequence---------------------
memorized = {}

def recursiveFib(n):
    if n in memorized:
        return memorized[n]
    if n <= 1:
        result = n
    else:
        result = recursiveFib(n - 1) + recursiveFib(n - 2)
    memorized[n] = result
    return result

fanInput = int(input("How many fans (in millions) does your favourite player have right now? "))

fibCalc = recursiveFib(fanInput)

print(f"Your favourite player will have {fibCalc} million fans in 10 years!")


# Without Recursion------------------------------------------

#def nonRecursiveFibonacci(x):
#    series = []
#    a, b = 0, 1
#
#    while len(series) < x:
#        series.append(a)
#        a, b = b, a + b
#
#    return series

#x = 10

#fibResult = nonRecursiveFibonacci(x)
#print(fibResult)


#Linear --------------------------------------------------------------------------------------------------------------------
searchedNameInput = input("Input a player to return their personal id, poss, mins, offense, defense, and total! ")

linearSearchStart = time.perf_counter_ns()

def linearSearch(array, target):
    for player in array:
        if len(player) >= 2 and player[1] == target:
        	return(player)

linearSearchName = linearSearch(sortedNextValues, searchedNameInput)

print(linearSearchName)

linearSearchEnd = time.perf_counter_ns()

linearSearchTime = linearSearchEnd - linearSearchStart

print(f"It took linear search {linearSearchTime} nanoseconds to look for {searchedNameInput}")

# Binary -------------------------------------------------------------------------------------------------------------------


binarySearchStart = time.perf_counter_ns()

def binarySearch(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        middle = (start + end) // 2
        midpoint = array[middle][1]
        if midpoint == target:
            return array[middle]
        elif midpoint < target:
            start = middle + 1
        else:
            end = middle - 1
    return None

nameBinarySearch = binarySearch(sortedNextValues, searchedNameInput)

print(nameBinarySearch)

binarySearchEnd = time.perf_counter_ns()

binarySearchTime = binarySearchEnd - binarySearchStart

print(f"It took binary search {binarySearchTime} nanoseconds to look for {searchedNameInput}")

#-----------------------------------------------------------------------------------------------

# Creating objects of children classes (Scorer and Defender)
DMitchell = Scorer("Donovan Mitchell", 5302, 2639, 5.0, -2.0, 4.0, 98, 27, 98)
TYoung = Scorer("Trae Young", 6020, 2771, 4.0, -1.0, 3.0, 97, 25, 98)
LJames = Scorer("Lebron James", 5487, 2573, 4.0, 0.0, 4.0, 95, 38, 90)

BAdebayo = Defender("Bam Adebayo", 6933, 3448, -2.0, 2.0, 1.0, 87, 26, 90)
ADavis = Defender("Anthony Davis", 5327, 2512, 2.0, 4.0, 7.0, 88, 30, 84)
DrGreen = Defender("Draymond Green", 5768, 2664, -1.0, 3.0, 2.0, 78, 33, 77)


# Calling methods for multiple objects of each child class
#print(DMitchell)
#DMitchell.skillCalc()
#DMitchell.remainingStamina()
#DMitchell.projectedSalary()

#print(TYoung)
#TYoung.skillCalc()
#TYoung.remainingStamina()
#TYoung.projectedSalary()

#print(LJames)
#LJames.skillCalc()
#LJames.remainingStamina()
#LJames.projectedSalary()

#print(BAdebayo)
#BAdebayo.speedTraining()
#BAdebayo.shootingPercentCalc()
#BAdebayo.projectedSalary()

#print(ADavis)
#ADavis.speedTraining()
#ADavis.shootingPercentCalc()
#ADavis.projectedSalary()

#print(DrGreen)
#DrGreen.speedTraining()
#DrGreen.shootingPercentCalc()
#DrGreen.projectedSalary()




