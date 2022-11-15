import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

lapse_rate_hourly = []
day = []
T_data_file = open('C:\\Users\\Abhilash Mittal\\Desktop\\All_T_data\\ERA5LAND\\9_tiles_T\\9_tiles_T_data.txt')
t_1 = []  # temp of tile 1
t_2 = []  # temp of tile 2
t_3 = []  # temp of tile 3
t_4 = []  # temp of tile 4
t_5 = []  # temp of tile 5
t_6 = []  # temp of tile 6
t_7 = []  # temp of tile 7
t_8 = []  # temp of tile 8
t_9 = []  # temp of tile 9
for line in T_data_file:
    t_1.append(float(line.split()[1]))
    t_2.append(float(line.split()[2]))
    t_3.append(float(line.split()[3]))
    t_4.append(float(line.split()[4]))
    t_5.append(float(line.split()[5]))
    t_6.append(float(line.split()[6]))
    t_7.append(float(line.split()[7]))
    t_8.append(float(line.split()[8]))
    t_9.append(float(line.split()[9]))
    day.append(float(line.split()[0]))

elevations = [3124.383457, 3645.24332, 3890.974453, 3920.576911, 4443.280526, 4526.863938, 4806.704478, 4843.784374,
              5307.385503]
save_lr_60min = open('C:\\Users\\Abhilash Mittal\\Desktop\\Era5land_lr_sp.txt', 'w')

for temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8, temp9 in zip(t_1, t_2, t_3, t_4, t_5, t_6, t_7, t_8, t_9):
    def func(X, a, c):
        return a * X + c


    # X and Ydata
    X = elevations
    Ydata = [temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8, temp9]
    popt, pcov = curve_fit(func, X, Ydata)
    # print(popt)
    lapse_rate_hourly.append(popt[0] * (-1000))
    save_lr_60min.write(str(popt[0] * (-1000)) + '\n')

file_l6_observed = open('C:\\Users\\Abhilash Mittal\\Desktop\\All_T_data\\ERA5LAND\\9_tiles_T\\Houlry_l6_t.txt')

# adding gaussian noise to hourly Temp_data
noise_L6_temp = np.random.normal(0, 0.2, 4656)
hourly_temp_l6 = []  # noised l6 Temperature
for line, i in zip(file_l6_observed,noise_L6_temp):
    hourly_temp_l6.append(float(line.split()[1]) + i)

continuous_day = []

for d in day:
    cd = (d - int(d)) * 100 / 24 + int(d)
    continuous_day.append(cd)

# Moving average
day_for_ave_lapserate = float(input("Enter the days for average lapserate (if x hours, enter x/24 day) : "))
window_size = int(day_for_ave_lapserate * 24)

numbers_series = pd.Series(lapse_rate_hourly)
windows = numbers_series.rolling(window_size)
moving_averages = windows.mean()

moving_averages_list = moving_averages.tolist()
without_nans_lr = moving_averages_list[window_size - 1:]

y = without_nans_lr
x = continuous_day[window_size - 1:]
'''plt.plot(continuous_day, lapse_rate_hourly, 'y')
plt.plot(x, y, 'r')
degree_sign = u"\N{DEGREE SIGN}"
plt.xlabel("Julian day of 2017")
plt.ylabel("Hourly Lapse Rate ($^\circ$C/km)")
plt.title("Hourly Lapse Rate vs Julian Day of 2017")
# plt.show()'''


# calculating hourly T at Line6 using 2 day average lapse rate and computing bias
bias = []  # hourly bias
for t_l6, lr, t_t1 in zip(hourly_temp_l6[window_size:], without_nans_lr[1:],
                          t_1[window_size:]):  # Add uncertainty in t_l6
    t_l6_era = (lr / 1000) * (elevations[0] - 4376) + t_t1
    bias.append(t_l6 - t_l6_era)

file_bias_lapse_rate_2days = open('C:\\Users\\Abhilash Mittal\\Desktop\\All_T_data\\ERA5LAND\\9_tiles_T'
                                  '\\hourly_5dAve_15_bias_lr_t1.txt', 'w')

bias_ydays_3plus = []  # it has 3 days extra, 195 (345 - 154 +1 = 192)
bias_day = int(input('Enter the number of days for which you want to correct mean bias: '))
for x in range(0, len(bias), bias_day * 24):
    chunk = bias[x:x + bias_day * 24]
    y = bias_day * 24
    while y > 0:
        bias_ydays_3plus.append(sum(chunk) / len(chunk))
        y = y - 1
bias_ydays = bias_ydays_3plus[:4656 - window_size]

for lr, d, b, t1 in zip(without_nans_lr[1:], day[window_size:], bias_ydays, t_1[window_size:]):
    file_bias_lapse_rate_2days.write(str(b) + '\n')

print(day[window_size:])

