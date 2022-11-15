# this code is for modeling melt using Era5 land T data, lapse rate is calculated using
# 9 grids around l6, bias corrected
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from ddf_ERA5LAND_LR import pdd

fhand_stake_data = open('Ablation_data_2017_reduced.txt')

melt = []
db_thickness = []
obs_days = []
elevation = []
time_period = []
jd_day = []

for line in fhand_stake_data:
    obs_days.append(int(line.split()[3]))
    melt.append(float(line.split()[6]))
    db_thickness.append(float(line.split()[5]))
    elevation.append(float(line.split()[4]))
    time_period.append(float(line.split()[7]))
    jd_day.append(int(line.split()[2]))

# adding gaussian noise in the obs melt and debris thickness
numbers = list(range(1, 325))
noise_of_Obs_melt = list(np.random.normal(0, 2, 324))
noised_Obs_melt = []
for i, j in zip(melt, noise_of_Obs_melt):
    noised_Obs_melt.append(i + j)
noise_of_db = list(np.random.normal(0, 2, 324))
noised_db_thickness = []
for i, j in zip(db_thickness, noise_of_db):
    noised_db_thickness.append(i + j)

for i in range(324):
    if noised_db_thickness[i] < 0:
        noised_db_thickness[i] = db_thickness[i]

for i in range(324):
    if noise_of_Obs_melt[i] < 0:
        noise_of_Obs_melt[i] = melt[i]

melt_rate = []
for m, d in zip(noised_Obs_melt, obs_days):
    melt_rate.append(m / d)

melt_model_1 = []
melt_model_2 = []
melt_model_3 = []


def func1(X, TF1, TF2):
    p, d = X
    return (TF1 * d ** TF2) * p / 10


def func2(X, ddf, d0):
    p, d = X
    return ddf * p / (1 + (d / d0)) / 10


def func3(X, ddf, d0, a):
    p, d = X
    return ddf * p / ((1 + (d / d0) ** 2)**a) / 10


# p,d and y data
p = pdd
d = noised_db_thickness
yData = noised_Obs_melt

initial_values1 = [8, -1]
popt1, pcov1 = curve_fit(func1, (p, d), yData, p0=np.asarray(initial_values1))  # fitting the data in the model
print("Model1 : ", popt1, " Initial values ", initial_values1)
# print(pcov)


initial_values2 = [5, 10]
popt2, pcov2 = curve_fit(func2, (p, d), yData, p0=np.asarray(initial_values2))  # fitting the data in the model
print("Model2 : ", popt2, " Initial values ", initial_values2)
#print(pcov2)

initial_values3 = [5, 10, 0.5]
popt3, pcov3 = curve_fit(func3, (p, d), yData, p0=np.asarray(initial_values3))  # fitting the data in the model
print("Model3 : ", popt3, " Initial values ", initial_values3)
#print(pcov3)

for p, d, od in zip(pdd, db_thickness, obs_days):
    melt_model_1.append((popt1[0] * d ** popt1[1]) * p / od / 10)
    melt_model_2.append(popt2[0] * p / (1 + (d / popt2[1])) / od / 10)
    melt_model_3.append(p * popt3[0] / ((1 + (d / popt3[1]) ** 2)**popt3[2]) / od / 10)

# Saving noised data into csv
df = pd.DataFrame(jd_day, columns= ['Julian Day'])
df['obs_period(days)'] = obs_days
df['elevation(m)'] = elevation
df['Derbis thickness (cm)'] = noised_db_thickness
df['melt (cm)'] = noised_Obs_melt
df['pdd'] = pdd
df['Model-1 Melt Rate (cm/day)'] = melt_model_1
df['Model-2 Melt Rate (cm/day)'] = melt_model_2
df['Model-3 Melt Rate (cm/day)'] = melt_model_3

df.to_csv('F:\\Abhilah_First\\Results\\Era5Land\\noised_stake_data.csv')

std_sq1 = []
std_sq2 = []
std_sq3 = []

for i, j, l, m in zip(melt_rate, melt_model_1, melt_model_2, melt_model_3):
    std_sq1.append((i - j) ** 2)
    std_sq2.append((i - l) ** 2)
    std_sq3.append((i - m) ** 2)

# saving parameters in csv files
model1_param = [popt1[0], pcov1[0][0] ** 0.5, popt1[1], pcov1[1][1] ** 0.5, (sum(std_sq1) / len(std_sq1)) ** 0.5]
df_model1 = pd.DataFrame({'TF1':[model1_param[0]],
                          'Uncertainty of TF1':[model1_param[1]],
                          'TF2':[model1_param[2]],
                          'Uncertainty of TF2':[model1_param[3]], 'RMSE':[model1_param[4]]})

model2_param = [popt2[0], pcov2[0][0] ** 0.5, popt2[1], pcov2[1][1] ** 0.5, (sum(std_sq2) / len(std_sq2)) ** 0.5]
df_model2 = pd.DataFrame({'DDF':[model2_param[0]],
                          'Uncertainty of DDF':[model2_param[1]],
                          'd0':[model2_param[2]],
                          'Uncertainty of d0':[model2_param[3]], 'RMSE':[model2_param[4]]})

model3_param = [popt3[0], pcov3[0][0] ** 0.5, popt3[1], pcov3[1][1] ** 0.5, popt3[2], pcov3[2][2] ** 0.5,
                (sum(std_sq1) / len(std_sq1)) ** 0.5]
df_model3 = pd.DataFrame({'DDF':[model3_param[0]],
                          'Uncertainty of DDF':[model3_param[1]],
                          'd0':[model3_param[2]],
                          'Uncertainty of d0':[model3_param[3]],
                          'a':[model3_param[4]],
                          'Uncertainty of a':[model3_param[5]], 'RMSE':[model3_param[6]]})
df_model1.to_csv('F:\\Abhilah_First\\Results\\Era5Land\\Model1param.csv')
df_model2.to_csv('F:\\Abhilah_First\\Results\\Era5Land\\Model2param.csv')
df_model3.to_csv('F:\\Abhilah_First\\Results\\Era5Land\\Model3param.csv')


print("RMSD1 =", (sum(std_sq1) / len(std_sq1)) ** 0.5)
print("RMSD2 =", (sum(std_sq2) / len(std_sq2)) ** 0.5)
print("RMSD3 =", (sum(std_sq3) / len(std_sq3)) ** 0.5)
print(pcov1)
print(pcov2)
print(pcov3)

