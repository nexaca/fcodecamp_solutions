import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df['date'] = pd.to_datetime(df['date'])


# Clean data

bigger_percentage = df['value'] < df['value'].quantile(0.025)
smaller_percentage = df['value'] > df['value'].quantile(0.975)

#df.drop(df.loc[df['line_race']==0].index, inplace=True)

sil_1 = df.loc[bigger_percentage]
sil_2 = df.loc[smaller_percentage]

df.drop(sil_1.index , inplace=True)
df.drop(sil_2.index , inplace=True)

#df = None


def draw_line_plot():
    # Draw line plot
    fig = plt.plot(df)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot

    bardata = df.groupby(by='month').sum()
    fig = sns.barplot(x = bardata.index,y=bardata['value'])
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    sns.boxplot(x="month", y="value", data=bf_box)
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
