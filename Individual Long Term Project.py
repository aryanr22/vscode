import csv

ShortenedRaptorOffense = []
DecimalRaptorOffense = []

ShortenedRaptorDefense = []
DecimalRaptorDefense = []

ShortenedRaptorTotalTotal = []
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
