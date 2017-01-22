import csv
import re


def divide(source, output):
    '''Divides the scores and times into two separate columns'''
    with open(source, "r") as csv_source:
        with open(output, 'w') as csv_dat:
            fieldnames = ['#','Game','Release date', 'Price', 'Userscore', 'Metascore', 'Owners', 'Average playtime', 'Median playtime']
            reader = csv.DictReader(csv_source)
            writer = csv.DictWriter(csv_dat, fieldnames, lineterminator='\n')


            dic = []

            for row in reader:
                scores = re.search(r'.+\((\d{2}%)/?(\d{2}%)?\)', row['Score rank(Userscore / Metascore)'])
                row['Userscore'] = scores.group(1)
                row['Metascore'] = scores.group(2) if scores.group(2) != None else '/'
                del row['Score rank(Userscore / Metascore)']


                times = re.search(r'0?(.+) \(0?(.+)\)', row['Playtime (Median)'])
                row['Average playtime'] = times.group(1)
                row['Median playtime'] = times.group(2)
                del row['Playtime (Median)']


                dic.append(row)


            writer.writeheader()
            for row in dic:
                writer.writerow(row)



def filter(source, output):
    '''removes games with lacking score data'''
    with open(source, "r") as csv_source:
        with open(output, 'w') as csv_dat:
            fieldnames = ['#','Game','Release date', 'Price', 'Score rank(Userscore / Metascore)', 'Owners', 'Playtime (Median)']
            reader = csv.DictReader(csv_source)
            writer = csv.DictWriter(csv_dat, fieldnames, lineterminator='\n')

            dic = []

            for row in reader:
                if not re.search(r'.*N/A.+', row['Score rank(Userscore / Metascore)']):
                    dic.append(row)

            writer.writeheader()
            for row in dic:
                writer.writerow(row)



def tidy_up(source, output):
    '''tidies up a couple of the data entries'''
    with open(source, "r") as csv_source:
        with open(output, 'w') as csv_dat:
            fieldnames = ['#','Game','Release date', 'Price', 'Score rank(Userscore / Metascore)', 'Owners', 'Playtime (Median)']
            reader = csv.DictReader(csv_source)
            writer = csv.DictWriter(csv_dat, fieldnames, lineterminator='\n')

            dic = []

            for row in reader:
                number = re.search(r'(.+) .*', row['Owners'])
                row['Owners'] = number.group(1)
                dic.append(row)

            writer.writeheader()
            for row in dic:
                writer.writerow(row)



def editing(source, output):
    filter(source, output)
    tidy_up(output, source)
    divide(source, output)