import matplotlib.pyplot as plt
import csv
import numpy as np

x = []
y = []
z = []
log_file='../logs/train_readme.log'
with open(log_file,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append((row[0]))
        y.append((row[3]))
        z.append((row[4]))
x_l, y_l, z_l = x.pop(0), y.pop(0), z.pop(0)
x = np.asarray(x).astype(int)
y = np.asarray(y).astype(float)
z = np.asarray(z).astype(float)

plt.plot(x,z)
plt.xlabel(x_l)
plt.ylabel(z_l)
plt.title('Loss vs Epoch')
plt.legend()
plt.savefig('../figs/readme/loss_ep.png')
plt.show()
