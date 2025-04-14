import csv

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print('\t'.join(row))

# Example
read_csv("students.csv")
