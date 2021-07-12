open_file=open("CupcakeInvoices.csv")

for row in open_file:
    # print(row)
    for row in open_file:
        values = row.split(',')
        #   print(values[2])
        for row in open_file:
          values = row.split(',')
          total = int(values[3]) * round(float(values[4]))
        #   print(total)
        for row in open_file:
                values = row.split(',')
                total = total + (int(values[3]) * float(values[4]))
        print(total)


open_file.close()

# Close your open file.

# Challenge: Do some research and see if you can limit your floats to never exceed
#  two characters after the decimal point.

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()