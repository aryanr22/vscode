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
# Updtaed: 04-October-2023
#-----------------------------------------------------------------------------------------------
import csv

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

    # Checking if the player's total minutes played is over 2500, then adding all of their main values (name, possessions, minutes, offense, defense, total) if is true
	if(shortMinutesPlayed[x] >= 2500):
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
with open('Shortened RAPTOR.csv') as fiddle:
	rows = csv.DictReader(fiddle)

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



class BasketBallPlayer():
    '''
    A basketball players class that holds the name, posessions, minutes, offense, defense, and total of basketball players

    Attributes
    ----------
    name : str
			Full name of the basketball player
    posessions : int
			The # of total posessions played by the basketball player
    minutes : int
			The # of total minutes played by the basketball player
    offense : float
			The truncated RAPTOR offense rating for this player
    defense : float
			The truncated RAPTOR defense rating for this player
    total : float
		    The truncated RAPTOR total rating for this player

    Methods
    -------
    possPerMin() -> int
			Prints the # of posessions each player averages per minute
	possPerGame() -> int
			Prints the # of posessions each player averages per game, if their total stats were spread across 82 games
	minPerGame() -> int
			Prints the # of minutes each player averages per game, if their total stats were spread across 82 games

    '''
    def __init__(self, name, posessions, minutes, offense, defense, total):
        '''
        Constructor to build a basketball player object


        Parameters
        ----------
        name : str
				Full name of the basketball player
    	posessions : int
				The # of total posessions played by the basketball player
    	minutes : int
				The # of total minutes played by the basketball player
    	offense : float
				The truncated RAPTOR offense rating for this player
    	defense : float
				The truncated RAPTOR defense rating for this player
    	total : float
		    	The truncated RAPTOR total rating for this player



        '''
        self.name = name
        self.posessions = posessions
        self.minutes = minutes
        self.offense = offense
        self.defense = defense
        self.total = total

    def __str__(self):
        '''
        Returns a string with the basketball player's name, # of posessions, # of minutes, RAPTOR offense, RAPTOR defense, and RAPTOR total

        Returns
        -------
        The basketball player's name, posessionss, minutes, offense, defense, total in a string


        '''
        return f"{self.name} had {self.posessions} posessions and played a total of {self.minutes} minutes this season. His RAPTOR offense was {self.offense}, RAPTOR defense was {self.defense}, and his RAPTOR total was {self.total}."

    def possPerMin(self):
        '''
        Prints basketball player's posessions per minute

        This divides the player's total posessions by their total minutes

        Prints
        ------
        String
				Includes the player's posessions per minute

        '''
        print(f"He averaged approx. {self.posessions // self.minutes} posessions per minute")

    def possPerGame(self):
        '''
        Prints basketball player's posessions per game, if spread across 82 games

        This divides the player's total posessions by 82 (# of games in a season)

        Prints
        ------
        String
				Includes the player's posessions per game

        '''
        print(f"He would have averaged approx. {self.posessions // 82} posessions per game, if his numbers were spread across 82 games")

    def minPerGame(self):
        '''
        Prints basketball player's posessions per minute

        This divides the player's total minutes by 82 (# of games in a season)

        Prints
        ------
        String
				Includes the player's minutes per game

        '''
        print(f"He would have averaged approx. {self.minutes // 82} minutes per game, if his numbers were spread across 82 games")




foundPlayer = None

# Creating a 2d array with each of the objects (players) and their attributes (statistics)
playerObjects = []


# Unpacking the 2-d array with all of the selective players' (those with >2500 min played) values, creating an object for each player, and storing it in the "playerObjects 2-d array"
for data in nextValues:
	name, posessions, minutes, offense, defense, total = data
	player = BasketBallPlayer(name, posessions, minutes, offense, defense, total)
	playerObjects.append(player)


# Taking user input to find a player to search from selective list
nameInput = input("Enter a Player Name: ")


# Comparing user input to selective list of players
for player in playerObjects:
	if player.name == nameInput:
		foundPlayer = player
		break


# If match is found, the player's key values are printed, along with their posessions per minute, posessions per game, and minutes per game
# If not found, a print statement is delivered, stating that
if foundPlayer:
	print(foundPlayer)
	foundPlayer.possPerMin()
	foundPlayer.possPerGame()
	foundPlayer.minPerGame()
else:
   	print("Player not found.")






