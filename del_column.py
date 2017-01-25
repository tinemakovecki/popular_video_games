import csv


def del_column(source, output, category):
    with open(source, "r", encoding="utf8") as csv_source:
        with open(output, 'w', encoding="utf8") as csv_dat:
            fieldnames = ['Game', 'Release year', 'Price', 'Userscore', 'Metascore', category, 'Owners', 'Average playtime', 'Median playtime']
            reader = csv.DictReader(csv_source)
            writer = csv.DictWriter(csv_dat, fieldnames, lineterminator='\n')

            dic = []

            for row in reader:
                del row['#']
                dic.append(row)

            writer.writeheader()
            for row in dic:
                writer.writerow(row)


#del_column('Activision-.csv', 'Activision.csv')
#del_column('Electronic Arts.csv', 'Electronic Arts-.csv')
#del_column('Bethesda Softworks.csv', 'Bethesda Softworks-.csv')
#del_column('Klei Entertainment.csv', 'Klei Entertainment-.csv')
#del_column('Paradox Interactive.csv', 'Paradox Interactive-.csv')
#del_column('Ubisoft.csv', 'Ubisoft-.csv')
#del_column('Warner Bros.csv', 'Warner Bros-.csv')
#del_column('2K Games.csv', '2K Games-.csv')
#del_column('SEGA.csv', 'SEGA-.csv')
#del_column('Valve.csv', 'Valve-.csv')