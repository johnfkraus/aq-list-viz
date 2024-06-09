import csv

id_to_link_dict = {}
with open('links.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        print(row)
        id_to_link_dict[row[0]] = row[2]

print(id_to_link_dict)
