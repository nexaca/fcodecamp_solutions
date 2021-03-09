import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']
    x2=df[(df.Year>=2000)]['Year']
    y2=df[(df.Year>=2000)]['CSIRO Adjusted Sea Level']
    years_extended = np.arange(1880, 2051, 1)
    years_extended2 = np.arange(2000, 2051, 1)
    # Create scatter plot
    plt.scatter(x=x,y=y)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x,y)
    y_pred = [slope*xi + intercept for xi in years_extended]
    plt.plot(years_extended,y_pred, color="green", label="Fitted line")
    # Create second line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x2,y2)
    y_pred = [slope*xi + intercept for xi in years_extended2]
    plt.plot(years_extended2,y_pred, color="red", label="Fitted line")

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()