import csv

def add_column(source, output, column_name, extra):
    with open(source, "r") as csv_source:
        with open(output, 'w') as csv_dat:
            fieldnames = ['#','Game','Release date', 'Price', 'Score rank(Userscore / Metascore)', 'Owners', 'Playtime (Median)', column_name]
            reader = csv.DictReader(csv_source)
            writer = csv.DictWriter(csv_dat, fieldnames, lineterminator='\n')

            dic = []

            for row in reader:
                row[column_name] = extra
                dic.append(row)

            writer.writeheader()
            for row in dic:
                writer.writerow(row)


add_column('Activision.csv', 'Activison_fix.csv', 'Publisher', 'Activision')