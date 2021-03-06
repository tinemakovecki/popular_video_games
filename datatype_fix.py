import csv
import numpy



def Datatype_fix(source, output, category):
    '''Corrects the types of columns containing number data'''
    with open(source, "r", encoding="utf8") as csv_source:
        with open(output, 'w', encoding="utf8") as csv_dat:
            fieldnames = ['Game','Release year', 'Price', 'Userscore', 'Metascore', category, 'Owners', 'Average playtime', 'Median playtime']
            reader = csv.DictReader(csv_source)
            writer = csv.DictWriter(csv_dat, fieldnames, lineterminator='\n')

            dic = []

            for row in reader:

                row['Release year'] = int(row['Release year']) if row['Release year'] != '/' else ''

                row['Userscore'] = int(row['Userscore'].replace('%', '')) if row['Userscore'] != '/' and row['Userscore'] != '' else '/'

                row['Metascore'] = int(row['Metascore'].replace('%', '')) if row['Metascore'] != '/' and row['Metascore'] != '' else '/'

                row['Owners'] = int(row['Owners'].replace(',', ''))

                large, small = row['Average playtime'].split(':')
                row['Average playtime'] = float(large) + (float('0.' + small) * 0.6)

                large, small = row['Median playtime'].split(':')
                row['Median playtime'] = float(large) + (float('0.' + small) * 0.6)

                dic.append(row)

            writer.writeheader()
            for row in dic:
                writer.writerow(row)


#Datatype_fix('Electronic Arts.csv', 'Electronic Arts-.csv')
#Datatype_fix('Bethesda Softworks.csv', 'Bethesda Softworks-.csv')
#Datatype_fix('Klei Entertainment.csv', 'Klei Entertainment-.csv')
#Datatype_fix('Paradox Interactive.csv', 'Paradox Interactive-.csv')
#Datatype_fix('Ubisoft.csv', 'Ubisoft-.csv')
#Datatype_fix('Warner Bros.csv', 'Warner Bros-.csv')
#Datatype_fix('2K Games.csv', '2K Games-.csv')
#Datatype_fix('SEGA.csv', 'SEGA-.csv')
#Datatype_fix('Valve.csv', 'Valve-.csv')
#Datatype_fix('Activision.csv', 'Activision-.csv')
