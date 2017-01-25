import csv
import re

def add_column(source, output, column_name, extra):
    with open(source, "r", encoding="utf8") as csv_source:
        with open(output, 'w', encoding="utf8") as csv_dat:
            fieldnames = ['#','Game','Release year', 'Price', 'Userscore', 'Metascore', column_name, 'Owners', 'Average playtime', 'Median playtime']
            reader = csv.DictReader(csv_source)
            writer = csv.DictWriter(csv_dat, fieldnames, lineterminator='\n')

            dic = []

            for row in reader:
                row[column_name] = extra
                dic.append(row)

            writer.writeheader()
            for row in dic:
                writer.writerow(row)



