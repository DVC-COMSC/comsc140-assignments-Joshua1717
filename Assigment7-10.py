import matplotlib.pyplot as plt


labels = ["Math","English","Physics", "Computer"]
Bill = [100, 90, 80, 60]
Marly = [90, 80, 70, 100]
bill_std = [2, 3, 4, 1]
marly_std = [3, 5, 2, 3]
width = 0.40       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, Bill, width, yerr=bill_std, label='Bill')
ax.bar(labels, Marly, width, yerr=marly_std, bottom=Bill,
       label='Marly')

ax.set_ylabel('Scores')
ax.set_title('Stacked graph of scores')
ax.legend()

plt.show()