import csv
import re

def add_column(source, output, column_name, extra):
    with open(source, "r") as csv_source:
        with open(output, 'w') as csv_dat:
            fieldnames = ['#','Game','Release date', 'Price', 'Userscore', 'Metascore', column_name, 'Owners', 'Average playtime', 'Median playtime']
            reader = csv.DictReader(csv_source)
            writer = csv.DictWriter(csv_dat, fieldnames, lineterminator='\n')

            dic = []

            for row in reader:
                row[column_name] = extra
                dic.append(row)

            writer.writeheader()
            for row in dic:
                writer.writerow(row)



#column_name = 'Publisher'
#tidy_up('Electronic Arts.csv', 'Electronic Arts-.csv')
#tidy_up('Bethesda Softworks.csv', 'Bethesda Softworks-.csv')
#tidy_up('Klei Entertainment.csv', 'Klei Entertainment-.csv')
#tidy_up('Paradox Interactive.csv', 'Paradox Interactive-.csv')
#tidy_up('Ubisoft.csv', 'Ubisoft-.csv')
#tidy_up('Warner Bros.csv', 'Warner Bros-.csv')
#tidy_up('2K Games.csv', '2K Games-.csv')
#tidy_up('SEGA.csv', 'SEGA-.csv')
#tidy_up('Valve.csv', 'Valve-.csv')