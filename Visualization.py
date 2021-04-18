import pandas as pd
import matplotlib.pyplot as plt
import csv
from pylab import rcParams

rcParams['figure.figsize'] = 16, 5

FILENAME = 'Head.csv'

Number_OF_Keystrokes = {}

with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    s = 0
    for row in reader:

        if len(row[1]) > 3:
            a = row[1][1:-1].split(',')
            for element in a:

                if element not in Number_OF_Keystrokes:
                    Number_OF_Keystrokes[element] = 1
                else:
                    Number_OF_Keystrokes[element] += 1
print(Number_OF_Keystrokes)

Number_OF_Keystrokes = pd.Series(Number_OF_Keystrokes)
plt.title("Количество нажатий клавиш")
plt.bar(Number_OF_Keystrokes.index, height=Number_OF_Keystrokes)
plt_output = plt.gcf()
plt.show()
plt.draw()
plt_output.savefig('NumberOfKeystrokes.png', dpi=100)
