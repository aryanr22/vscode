import csv

Name = []
Posessions = []
MinutesPlayed = []

ShortenedRaptorOffense = []
DecimalRaptorOffense = []

ShortenedRaptorDefense = []
DecimalRaptorDefense = []

ShortenedRaptorTotal = []
DecimalRaptorTotal = []

with open('RAPTOR 2022-23.csv') as file:
	rows = csv.DictReader(file)

	for row in rows:
		name = str(row['player_name'])
		posessions = int(row['poss'])
		minutes = int(row['mp'])

		s_o = float(row['raptor_offense']) // 1
		d_o = float(row['raptor_offense']) % 1

		s_d = float(row['raptor_offense']) // 1
		d_d = float(row['raptor_offense']) % 1

		s_t = float(row['raptor_offense']) // 1
		d_t = float(row['raptor_offense']) % 1

		Name.append(name)
		Posessions.append(posessions)
		MinutesPlayed.append(minutes)

		ShortenedRaptorOffense.append(s_o)
		DecimalRaptorOffense.append(d_o)

		ShortenedRaptorDefense.append(s_d)
		DecimalRaptorDefense.append(d_d)

		ShortenedRaptorTotal.append(s_t)
		DecimalRaptorTotal.append(d_t)



NewValues = []
for x in range(len(ShortenedRaptorOffense)):
    row = [Name[x], Posessions[x], MinutesPlayed[x], ShortenedRaptorOffense[x], DecimalRaptorOffense[x], ShortenedRaptorDefense[x], DecimalRaptorDefense[x], ShortenedRaptorTotal[x], DecimalRaptorTotal[x]]
    NewValues.append(row)


with open(r'RAPTOR 2022-23 With New Data.csv', 'w', newline="\n") as f:
    wr = csv.writer(f)
    wr.writerow(['name', 'posessions', 'minutes', 'offense_shortened', 'offense_decimal', 'defense_shortened', 'defense_decimal', 'total_shortened', 'total_decimal',])
    wr.writerows(NewValues)


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

		o_s = float(row['offense_shortened'])
		d_s = float(row['defense_shortened'])
		t_s = float(row['total_shortened'])

		shortName.append(name)
		shortPosessions.append(posessions)
		shortMinutesPlayed.append(minutes)

		shortOffense.append(o_s)
		shortDefense.append(d_s)
		shortTotal.append(t_s)

for x in range(len(ShortenedRaptorOffense)):
	if(shortMinutesPlayed[x] >= 2500):
		row = [shortName[x], shortPosessions[x], shortMinutesPlayed[x], shortOffense[x], shortDefense[x], shortTotal[x]]
		values.append(row)
	else:
		x +=1

#print(shortName)

with open(r'Shortened RAPTOR.csv', 'w', newline="\n") as f:
    wr = csv.writer(f)
    wr.writerow(['name', 'posessions', 'minutes', 'offense', 'defense', 'total'])
    wr.writerows(values)



anotherName = []
anotherPosession = []
anotherMinutes = []
anotherOffense = []
anotherDefense = []
anotherTotal = []

with open('Shortened RAPTOR.csv') as fiddle:
	rows = csv.DictReader(fiddle)
	for row in rows:
		name = str(row['name'])
		posessions = int(row['posessions'])
		minutes = int(row['minutes'])

		o = float(row['offense'])
		d = float(row['defense'])
		t = float(row['total'])

		anotherName.append(name)
		anotherPosession.append(posessions)
		anotherMinutes.append(minutes)

		anotherOffense.append(o)
		anotherDefense.append(d)
		anotherTotal.append(t)

NextValues = []
for x in range(len(anotherName)):
    row = [anotherName[x], anotherPosession[x], anotherMinutes[x], anotherOffense[x], anotherDefense[x], anotherTotal[x]]
    NextValues.append(row)



class BasketBallPlayer:
    def __init__(self, name, posessions, minutes, offense, defense, total):
        self.name = name
        self.posessions = posessions
        self.minutes = minutes
        self.offense = offense
        self.defense = defense
        self.total = total

    def __str__(self):
        return f"{self.name} had {self.posessions} posessions and played a total of {self.minutes} minutes this season. \
    	His RAPTOR offense was {self.offense}, RAPTOR defense was {self.defense}, and his RAPTOR total was {self.total}."

    def possPerMin(self):
        print(f"He averaged approx. {self.posessions // self.minutes} posessions per minute")
    def possPerGame(self):
        print(f"He would have averaged approx. {self.posessions // 82} posessions per game, if their numbers spread across 82 games")
    def minPerGame(self):
    	print(f"He would have averaged approx. {self.minutes // 82} posessions per game, if their numbers spread across 82 games")


found_player = None





people_objects = []
for data in NextValues:
    name, posessions, minutes, offense, defense, total = data
    player = BasketBallPlayer(name, posessions, minutes, offense, defense, total)
    people_objects.append(player)

for player in people_objects:
    print(player)

name_input = input("Enter a Player Name: ")


for player in people_objects:
    if player.name == name_input:
        found_player = player
        break


if found_player:
    print(found_player)
    found_player.possPerMin()
    found_player.possPerGame()
    found_player.minPerGame()
else:
    print("Player not found.")






