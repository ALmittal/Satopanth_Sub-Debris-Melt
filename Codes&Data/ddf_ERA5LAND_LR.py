# this code is for pdd calculation using Era5 land data, lapse rate is calculated using
# 9 grids around l6, bias corrected


fhand_ablation = open('Ablation_data_2017_reduced.txt')

pdd = []

from lapse_rate_models import day
from lapse_rate_models import window_size
from lapse_rate_models import without_nans_lr
from lapse_rate_models import bias_ydays
from lapse_rate_models import t_1
from lapse_rate_models import elevations


def ddf(range_days, elevation, melt):
    temp = []
    for time_step, b, lr, temp_at_1 in zip(day[window_size:], bias_ydays, without_nans_lr[1:], t_1[window_size:]):
        if int(time_step) in range_days:
            temp.append((lr / 1000) * (elevations[0] - elevation) + temp_at_1 + b)

    # now for pdd calculation I need positive values from  x hourly_temp list
    PDD = sum([x for x in temp if x > 0]) / 24  # divided by 24 because delta t is 1/24
    if PDD == 0:
        DDF = 'null'
    else:
        DDF = (melt * 10) / PDD
    return PDD


ranges = []  # list of lists, each list is the list of days, e.g.[ 232, 233, 234......, 252]
rh = []
for line in fhand_ablation:
    if float(line.split()[5]) > 0:
        n = int(line.split()[3])  # n is number of days, not number of intervals for pdd, that will be 24*n
        last_day = int(line.split()[2])
        starting_day = last_day - n + 1
        range_days = list(range(starting_day, last_day + 1))

        # now I will have to calculate DDF and write it in the file
        # fhand_ddf.write(str(ddf(range_days, int(line.split()[4]), float(line.split()[6]))) + '\n')
        pdd.append(ddf(range_days, int(line.split()[4]), float(line.split()[6])))
        # rh.append(ddf(range_days, int(line.split()[4]), float(line.split()[6])))
