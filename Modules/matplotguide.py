# Average temperature rise each month since 1880
import numpy as np
from matplotlib import pyplot as plt
plt.style.use("ggplot")

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

year_2016 = [1.17, 1.35, 1.3, 1.09, 0.93, 0.76, 0.83, 0.98, 0.87, 0.89, 0.93, 0.81]
year_2015 = [0.81, 0.86, 0.9, 0.74, 0.78, 0.78, 0.71, 0.78 , 0.81, 1.06, 1.04, 1.1]
year_2014 = [0.73, 0.51, 0.77, 0.78, 0.87, 0.66, 0.57, 0.82, 0.9, 0.85, 0.67, 0.79]
year_2013 = [0.68, 0.55, 0.66, 0.52, 0.61, 0.65, 0.59, 0.66, 0.78, 0.69, 0.81, 0.67]

for i, year in enumerate([year_2016, year_2015, year_2014, year_2013]):
    plt.plot(months, year, color=np.random.rand(3,), linestyle="-", label=str(int(2016 - i)))

plt.xlabel("Months")
plt.ylabel("Mean Temperature Rise")
plt.title("Matplotlib Mean Temperature Illustration")
plt.grid(True)
plt.legend()
plt.show()

