import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import pandas as pd

from Database_Transactions import DatabaseTransaction

# matplotlib.use('TKAgg')


class Plot:

    @staticmethod
    def plot_data():
        plot_df = pd.DataFrame(DatabaseTransaction().convert_data(), columns=['Day_in_month', 'No_of_events'])
        print(plot_df)

        sns.jointplot(x='Day_in_month', y='No_of_events', hue='No_of_events', data=plot_df, palette='seismic')
        plt.savefig('jointplot.png', dpi=300)
        plt.show()


