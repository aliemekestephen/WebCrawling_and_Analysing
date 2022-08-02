import matplotlib.pyplot as plt
import numpy as np

from Utils.Database_Transactions import DatabaseTransaction

y, x = np.asarray(DatabaseTransaction().convert_data())

fig = plt.figure('Plot 1')

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y, ls='dashed', marker='*')
axes.set_xlabel('Days in the month')
axes.set_ylabel('No of events')
axes.set_title('Number of events per day')

plt.show()

