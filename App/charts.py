import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from Database_Transactions import DatabaseTransaction


class Plot:

    @staticmethod
    def plot_data():
        plot_df = pd.DataFrame(DatabaseTransaction().convert_data(), columns=['Days', 'No_of_events'])
        print(plot_df)

        sns.jointplot(x='Days', y='No_of_events', hue='No_of_events', data=plot_df, palette='seismic')
        plt.show()
