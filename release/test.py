import csv

Number_OF_Keystrokes = {}

with open('keys.csv', "r", newline="") as file:
    reader = csv.reader(file)
    s = 0
    reader = list(reader)
    for row in reader[1:]:
        element = row[0]
        if element not in Number_OF_Keystrokes:
            Number_OF_Keystrokes[element] = 1
        else:
            Number_OF_Keystrokes[element] +=1

print(Number_OF_Keystrokes)