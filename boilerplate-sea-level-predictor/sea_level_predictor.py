import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x_values  = df['Year']
    y_values  = df['CSIRO Adjusted Sea Level']


    # Create scatter plot

    fig = plt.scatter(x = x_values,y =y_values )
    plt.title('CSIRO by Years')
    plt.xlabels('Year')
    plt.ylabels('CSIRO')
    plt.show()


    # Create first line of best fit
    lin = linregress(x = None , y = None )


    # Create second line of best fit


    # Add labels and title


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
