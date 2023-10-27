import matplotlib.pyplot as plt
# Sample data (replace this with your own data)
ages = ['0-9', '10-19', '20-29', '30-39', '40-49']
population = [500, 800, 1200, 950, 600]

# Create a bar chart
plt.bar(ages, population, color='skyblue')
plt.xlabel('Age Groups')
plt.ylabel('Population')
plt.title('Distribution of Ages in the Population')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace this with your own data)
income_data = np.random.normal(50000, 15000, 1000)  # Random income data

# Create a histogram
plt.hist(income_data, bins=20, edgecolor='black', color='lightblue')
plt.xlabel('Income')
plt.ylabel('Frequency')
plt.title('Income Distribution Histogram')
plt.show()


