import csv


ShortenedRaptorOffense= []
DecimalRaptorOffense = []

ShortenedRaptorDefense= []
DecimalRaptorDefense = []

ShortenedRaptorTotal= []
DecimalRaptorTotal = []

with open('RAPTOR 2022-23.csv') as file:
    rows = csv.DictReader(file)

    for row in rows:
        s_o = float(row['raptor_offense']) // 1
        d_o = float(row['raptor_offense']) % 1

        s_d = float(row['raptor_offense']) // 1
        d_d = float(row['raptor_offense']) % 1

        s_t = float(row['raptor_offense']) // 1
        d_t = float(row['raptor_offense']) % 1

        ShortenedRaptorOffense.append(s_o)
        DecimalRaptorOffense.append(d_o)

        ShortenedRaptorDefense.append(s_d)
        DecimalRaptorDefense.append(d_d)

        ShortenedRaptorTotal.append(s_t)
        DecimalRaptorTotal.append(d_t)



DecimalRaptorOffense = [[e] for e in DecimalRaptorOffense]
ShortenedRaptorOffense = [[e] for e in ShortenedRaptorOffense]

DecimalRaptorDefense = [[e] for e in DecimalRaptorOffense]
ShortenedRaptorDefense = [[e] for e in ShortenedRaptorDefense]

DecimalRaptorTotal = [[e] for e in DecimalRaptorTotal]
ShortenedRaptorTotal = [[e] for e in ShortenedRaptorTotal]

NewValues = []
for x in range(len(ShortenedRaptorOffense)):
    row = [ShortenedRaptorOffense[x], DecimalRaptorOffense[x], ShortenedRaptorDefense[x], DecimalRaptorDefense[x], ShortenedRaptorTotal[x], DecimalRaptorTotal[x]]
    NewValues.append(row)




with open(r'RAPTOR 2022-23 With New Data.csv', 'w', newline="\n") as f:
    wr = csv.writer(f)
    wr.writerow(['offense_shortened', 'offense_decimal', 'defense_shortened', 'defense_decimal', 'total_shortened', 'total_decimal'])
    wr.writerows(NewValues)

#test


