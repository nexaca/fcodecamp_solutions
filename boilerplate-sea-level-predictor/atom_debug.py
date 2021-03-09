import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


# Read data from file
df = pd.read_csv('epa-sea-level.csv')

#values
year_values  = df['Year']
sea_values  = df['CSIRO Adjusted Sea Level']

#extend years - 1880 - 2051
import numpy as np
year_values_ext = np.arange(1880, 2051 , 1)
print(extended_years)

#second extended years - 2000 -2051
year_values_ext_2 = np.arange(2000, 2051, 1)
print(extended_years2)


fig = plt.scatter(x = year_values,y =sea_values, color = 'red', alpha = 0.5)
plt.title('CSIRO by Years')
plt.xlabel('Year')
plt.ylabel('CSIRO')
plt.show()

# Create first line of best fit

#slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
lin = linregress(x = year_values , y =sea_values)
print(lin)

#linregress plot
plt.plot(year_values_ext , lin.slope*year_values_ext + lin.intercept, color='green', alpha = 0.5)


#final plot
fig = plt.scatter(x = year_values_ext,y =sea_values, color = 'red', alpha = 0.5)
plt.plot(year_values_ext , lin.slope*year_values_ext + lin.intercept, color='green', alpha = 0.5)
plt.title('CSIRO by Years')
plt.xlabel('Year')
plt.ylabel('CSIRO')
plt.show()
