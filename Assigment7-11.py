import matplotlib.pyplot as plt
import numpy as np
 
#x-axis
students = ['Bill', 'Mary']

#y-axis
math = [100, 90,]
english = [90, 80,]
physics = [80, 90,]
computer = [80, 80]
 
x = np.arange(len(students))
width = .15
 
#draw grouped bar chart
fig, ax = plt.subplots()
bar1 = ax.bar(x, math, width, label='Math')
bar2 = ax.bar(x + width, english, width, label='English')
bar3 = ax.bar(x + width*2, physics, width, label='Physics')
bar4 = ax.bar(x + width*3, computer, width, label='Computer')

ax.set_xticks(x + width*2, students)
ax.legend((bar1, bar2, bar3, bar4), ('Math', 'English', 'Physics', 'Computer'))
 
#labels
ax.bar_label(bar1)
ax.bar_label(bar2)
ax.bar_label(bar3)
ax.bar_label(bar4)
 
plt.show()