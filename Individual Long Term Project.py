import csv

name = []
posessions = []
minutesPlayed = []

intRaptorOffense = []
decimalRaptorOffense = []

intRaptorDefense = []
decimalRaptorDefense = []

intRaptorTotal = []
decimalRaptorTotal = []

with open('RAPTOR 2022-23.csv') as file:
	rows = csv.DictReader(file)

	for row in rows:
		nameStr = str(row['player_name'])
		posessionsInt = int(row['poss'])
		minutesInt = int(row['mp'])

		sO = float(row['raptor_offense']) // 1
		dO = float(row['raptor_offense']) % 1

		sD = float(row['raptor_offense']) // 1
		dD = float(row['raptor_offense']) % 1

		sT = float(row['raptor_offense']) // 1
		dT = float(row['raptor_offense']) % 1

		name.append(nameStr)
		posessions.append(posessionsInt)
		minutesPlayed.append(minutesInt)

		intRaptorOffense.append(sO)
		decimalRaptorOffense.append(dO)

		intRaptorDefense.append(sD)
		decimalRaptorDefense.append(dD)

		intRaptorTotal.append(sT)
		decimalRaptorTotal.append(dT)



newValues = []
for x in range(len(intRaptorOffense)):
    row = [name[x], posessions[x], minutesPlayed[x], intRaptorOffense[x], decimalRaptorOffense[x], intRaptorDefense[x], decimalRaptorDefense[x], intRaptorTotal[x], decimalRaptorTotal[x]]
    newValues.append(row)


with open(r'RAPTOR 2022-23 With New Data.csv', 'w', newline="\n") as f:
    wr = csv.writer(f)
    wr.writerow(['name', 'posessions', 'minutes', 'offense_shortened', 'offense_decimal', 'defense_shortened', 'defense_decimal', 'total_shortened', 'total_decimal',])
    wr.writerows(newValues)


shortName = []
shortPosessions = []
shortMinutesPlayed = []

shortOffense = []
shortDefense = []
shortTotal = []

values = []

with open('RAPTOR 2022-23 With New Data.csv') as file:
	rows = csv.DictReader(file)


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

for x in range(len(intRaptorOffense)):
	if(shortMinutesPlayed[x] >= 2500):
		row = [shortName[x], shortPosessions[x], shortMinutesPlayed[x], shortOffense[x], shortDefense[x], shortTotal[x]]
		values.append(row)
	else:
		x +=1



with open(r'Shortened RAPTOR.csv', 'w', newline="\n") as f:
    wr = csv.writer(f)
    wr.writerow(['name', 'posessions', 'minutes', 'offense', 'defense', 'total'])
    wr.writerows(values)

#stats = {'names': [],
#         'possessions': []}
#stats['names'][3]

smallestName = []
smallestPosession = []
smallestMinutes = []
smallestOffense = []
smallestDefense = []
smallestTotal = []

with open('Shortened RAPTOR.csv') as fiddle:
	rows = csv.DictReader(fiddle)
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

nextValues = []
for x in range(len(smallestName)):
    row = [smallestName[x], smallestPosession[x], smallestMinutes[x], smallestOffense[x], smallestDefense[x], smallestTotal[x]]
    nextValues.append(row)



class BasketBallPlayer:
    def __init__(self, name, posessions, minutes, offense, defense, total):
        self.name = name
        self.posessions = posessions
        self.minutes = minutes
        self.offense = offense
        self.defense = defense
        self.total = total

    def __str__(self):
        return f"{self.name} had {self.posessions} posessions and played a total of {self.minutes} minutes this season. His RAPTOR offense was {self.offense}, RAPTOR defense was {self.defense}, and his RAPTOR total was {self.total}."

    def possPerMin(self):
        print(f"He averaged approx. {self.posessions // self.minutes} posessions per minute")
    def possPerGame(self):
        print(f"He would have averaged approx. {self.posessions // 82} posessions per game, if his numbers spread across 82 games")
    def minPerGame(self):
    	print(f"He would have averaged approx. {self.minutes // 82} minutes per game, if his numbers spread across 82 games")


foundPlayer = None


playerObjects = []
for data in nextValues:
    name, posessions, minutes, offense, defense, total = data
    player = BasketBallPlayer(name, posessions, minutes, offense, defense, total)
    playerObjects.append(player)

#for player in people_objects:
#    print(player)

nameInput = input("Enter a Player Name: ")


for player in playerObjects:
    if player.name == nameInput:
        foundPlayer = player
        break


if foundPlayer:
    print(foundPlayer)
    foundPlayer.possPerMin()
    foundPlayer.possPerGame()
    foundPlayer.minPerGame()
else:
    print("Player not found.")






