import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from Utils.Database_Transactions import DatabaseTransaction


event = sns.load_dataset('tips')
events = DatabaseTransaction().read_database()

# sns.distplot(events['date'].day)

plot_df = pd.DataFrame(DatabaseTransaction().convert_data(), columns=['Days', 'No_of_events'])
print(plot_df)

# Plot 1
# sns.distplot(plot_df['No_of_events'])
# plt.show()

# Plot 2 # TODO Needed
sns.jointplot(x='Days', y='No_of_events', hue='No_of_events', data=plot_df, palette='seismic')
plt.show()

# Plot 3
# sns.pairplot(plot_df)
# plt.show()

