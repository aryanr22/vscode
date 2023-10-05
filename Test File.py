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

#Name = [i for i in Name]
Posessions = [[i] for i in Posessions]
MinutesPlayed = [[i] for i in MinutesPlayed]

ShortenedRaptorOffense = [[i] for i in ShortenedRaptorOffense]
DecimalRaptorOffense = [[i] for i in DecimalRaptorOffense]

ShortenedRaptorDefense = [[i] for i in ShortenedRaptorDefense]
DecimalRaptorDefense = [[i] for i in DecimalRaptorDefense]

ShortenedRaptorTotal = [[i] for i in ShortenedRaptorTotal]
DecimalRaptorTotal = [[i] for i in DecimalRaptorTotal]





#test


