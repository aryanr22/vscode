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


with open(r'Shortened RAPTOR.csv', 'w', newline="\n") as f:
    wr = csv.writer(f)
    wr.writerow(['name', 'posessions', 'minutes', 'offense', 'defense', 'total'])
    wr.writerows(values)




for x in range(len(shortName)):
    user_input = input("Enter a Player Name: ")
    if user_input == shortName[x]:
        print(values[x])
        break
    else:
        print("didnt work try agin")
        x += 1
        break



