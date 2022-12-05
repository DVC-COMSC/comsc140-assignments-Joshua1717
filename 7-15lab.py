import matplotlib.pyplot as plt



x = [0, 10, 20, 30, 40]
y = [100, 200, 300, 200, 100]

bar_width = 5
plt.bar(x, y, bar_width, color=('r', 'g', 'b', 'g', 'r'))
plt.show()