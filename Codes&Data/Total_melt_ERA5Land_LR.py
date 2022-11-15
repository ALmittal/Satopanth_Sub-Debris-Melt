from best_fit_Era5Land_LR import melt_rate
from best_fit_Era5Land_LR import noised_db_thickness
from best_fit_Era5Land_LR import melt_model_1
from best_fit_Era5Land_LR import melt_model_2
from best_fit_Era5Land_LR import melt_model_3
from best_fit_Era5Land_LR import time_period
import pandas as pd

n = 1
periodic_total_melt_n = []
while n < 11:
    total_melt_1 = [] # melts of nth time period for each db band
    meltrate_n = []
    db_thickness_n = []
    obs_day = [10, 14, 13, 18, 16, 15, 17, 14, 14, 21]
    for mr, db, time in zip(melt_rate, noised_db_thickness, time_period):
        if time == n:
            meltrate_n.append(mr)
            db_thickness_n.append(db)
    melt_rate_db1 = []
    melt_rate_db2 = []
    melt_rate_db3 = []
    melt_rate_db4 = []
    melt_rate_db5 = []
    melt_rate_db6 = []
    melt_rate_db7 = []
    melt_rate_db8 = []
    melt_rate_db9 = []

    for i, j in zip(meltrate_n, db_thickness_n):
        if 0 < j < 5.0001:
            melt_rate_db1.append(i)

        elif 5 < j < 15.0001:
            melt_rate_db2.append(i)

        elif 15 < j < 25.0001:
            melt_rate_db3.append(i)

        elif 25 < j < 35.0001:
            melt_rate_db4.append(i)

        elif 35 < j < 45.0001:
            melt_rate_db5.append(i)

        elif 45 < j < 60.0001:
            melt_rate_db6.append(i)

        elif 60 < j < 75.0001:
            melt_rate_db7.append(i)

        elif 75 < j < 100.0001:
            melt_rate_db8.append(i)

        elif 100 < j < 120.0001:
            melt_rate_db9.append(i)
    area = 12.0096
    if len(melt_rate_db1) > 0:
        total_melt_1.append(sum(melt_rate_db1)/len(melt_rate_db1)*obs_day[n-1]*area*0.22811620162583887/100)
    if len(melt_rate_db2) > 0:
        total_melt_1.append(sum(melt_rate_db2)/len(melt_rate_db2)*obs_day[n-1]*area*0.28558041049247607/100)
    if len(melt_rate_db3) > 0:
        total_melt_1.append(sum(melt_rate_db3)/len(melt_rate_db3)*obs_day[n-1]*area*0.13087821700879687/100)
    if len(melt_rate_db4) > 0:
        total_melt_1.append(sum(melt_rate_db4)/len(melt_rate_db4)*obs_day[n-1]*area*0.10558937279127911/100)

    if len(melt_rate_db5) > 0:
        total_melt_1.append(sum(melt_rate_db5)/len(melt_rate_db5)*obs_day[n-1]*area*0.12350830293632936/100)

    if len(melt_rate_db6) > 0:
        total_melt_1.append(sum(melt_rate_db6)/len(melt_rate_db6)*obs_day[n-1]*area*0.0543555133000583/100)

    if len(melt_rate_db7) > 0:
        total_melt_1.append(sum(melt_rate_db7)/len(melt_rate_db7)*obs_day[n-1]*area*0.04154052330139432/100)

    if len(melt_rate_db8) > 0:
        total_melt_1.append(sum(melt_rate_db8)/len(melt_rate_db8)*obs_day[n-1]*area*0.024694405617078932/100)

    if len(melt_rate_db9) > 0:
        total_melt_1.append(sum(melt_rate_db9)/len(melt_rate_db9)*obs_day[n-1]*area*0.005737052926748187/100)

    periodic_total_melt_n.append(sum(total_melt_1))
    n = n + 1

m = 1
periodic_total_melt_m = []
while m < 11:
    total_melt_1 = [] # melts of nth time period for each db band
    meltrate_n = []
    db_thickness_n = []
    obs_day = [10, 14, 13, 18, 16, 15, 17, 14, 14, 21]
    for mr, db, time in zip(melt_model_1, noised_db_thickness, time_period):
        if time == m:
            meltrate_n.append(mr)
            db_thickness_n.append(db)
    melt_rate_db1 = []
    melt_rate_db2 = []
    melt_rate_db3 = []
    melt_rate_db4 = []
    melt_rate_db5 = []
    melt_rate_db6 = []
    melt_rate_db7 = []
    melt_rate_db8 = []
    melt_rate_db9 = []

    for i, j in zip(meltrate_n, db_thickness_n):
        if 0 < j < 5.0001:
            melt_rate_db1.append(i)

        elif 5 < j < 15.0001:
            melt_rate_db2.append(i)

        elif 15 < j < 25.0001:
            melt_rate_db3.append(i)

        elif 25 < j < 35.0001:
            melt_rate_db4.append(i)

        elif 35 < j < 45.0001:
            melt_rate_db5.append(i)

        elif 45 < j < 60.0001:
            melt_rate_db6.append(i)

        elif 60 < j < 75.0001:
            melt_rate_db7.append(i)

        elif 75 < j < 100.0001:
            melt_rate_db8.append(i)

        elif 100 < j < 120.0001:
            melt_rate_db9.append(i)
    area = 12.0096
    if len(melt_rate_db1) > 0:
        total_melt_1.append(sum(melt_rate_db1)/len(melt_rate_db1)*obs_day[m-1]*area*0.22811620162583887/100)
    if len(melt_rate_db2) > 0:
        total_melt_1.append(sum(melt_rate_db2)/len(melt_rate_db2)*obs_day[m-1]*area*0.28558041049247607/100)
    if len(melt_rate_db3) > 0:
        total_melt_1.append(sum(melt_rate_db3)/len(melt_rate_db3)*obs_day[m-1]*area*0.13087821700879687/100)
    if len(melt_rate_db4) > 0:
        total_melt_1.append(sum(melt_rate_db4)/len(melt_rate_db4)*obs_day[m-1]*area*0.10558937279127911/100)

    if len(melt_rate_db5) > 0:
        total_melt_1.append(sum(melt_rate_db5)/len(melt_rate_db5)*obs_day[m-1]*area*0.12350830293632936/100)

    if len(melt_rate_db6) > 0:
        total_melt_1.append(sum(melt_rate_db6)/len(melt_rate_db6)*obs_day[m-1]*area*0.0543555133000583/100)

    if len(melt_rate_db7) > 0:
        total_melt_1.append(sum(melt_rate_db7)/len(melt_rate_db7)*obs_day[m-1]*area*0.04154052330139432/100)

    if len(melt_rate_db8) > 0:
        total_melt_1.append(sum(melt_rate_db8)/len(melt_rate_db8)*obs_day[m-1]*area*0.024694405617078932/100)

    if len(melt_rate_db9) > 0:
        total_melt_1.append(sum(melt_rate_db9)/len(melt_rate_db9)*obs_day[m-1]*area*0.005737052926748187/100)

    periodic_total_melt_m.append(sum(total_melt_1))
    m = m + 1

o = 1
periodic_total_melt_o = []
while o < 11:
    total_melt_1 = [] # melts of nth time period for each db band
    meltrate_n = []
    db_thickness_n = []
    obs_day = [10, 14, 13, 18, 16, 15, 17, 14, 14, 21]
    for mr, db, time in zip(melt_model_2, noised_db_thickness, time_period):
        if time == o:
            meltrate_n.append(mr)
            db_thickness_n.append(db)
    melt_rate_db1 = []
    melt_rate_db2 = []
    melt_rate_db3 = []
    melt_rate_db4 = []
    melt_rate_db5 = []
    melt_rate_db6 = []
    melt_rate_db7 = []
    melt_rate_db8 = []
    melt_rate_db9 = []

    for i, j in zip(meltrate_n, db_thickness_n):
        if 0 < j < 5.0001:
            melt_rate_db1.append(i)

        elif 5 < j < 15.0001:
            melt_rate_db2.append(i)

        elif 15 < j < 25.0001:
            melt_rate_db3.append(i)

        elif 25 < j < 35.0001:
            melt_rate_db4.append(i)

        elif 35 < j < 45.0001:
            melt_rate_db5.append(i)

        elif 45 < j < 60.0001:
            melt_rate_db6.append(i)

        elif 60 < j < 75.0001:
            melt_rate_db7.append(i)

        elif 75 < j < 100.0001:
            melt_rate_db8.append(i)

        elif 100 < j < 120.0001:
            melt_rate_db9.append(i)
    area = 12.0096
    if len(melt_rate_db1) > 0:
        total_melt_1.append(sum(melt_rate_db1)/len(melt_rate_db1)*obs_day[o-1]*area*0.22811620162583887/100)
    if len(melt_rate_db2) > 0:
        total_melt_1.append(sum(melt_rate_db2)/len(melt_rate_db2)*obs_day[o-1]*area*0.28558041049247607/100)
    if len(melt_rate_db3) > 0:
        total_melt_1.append(sum(melt_rate_db3)/len(melt_rate_db3)*obs_day[o-1]*area*0.13087821700879687/100)
    if len(melt_rate_db4) > 0:
        total_melt_1.append(sum(melt_rate_db4)/len(melt_rate_db4)*obs_day[o-1]*area*0.10558937279127911/100)

    if len(melt_rate_db5) > 0:
        total_melt_1.append(sum(melt_rate_db5)/len(melt_rate_db5)*obs_day[o-1]*area*0.12350830293632936/100)

    if len(melt_rate_db6) > 0:
        total_melt_1.append(sum(melt_rate_db6)/len(melt_rate_db6)*obs_day[o-1]*area*0.0543555133000583/100)

    if len(melt_rate_db7) > 0:
        total_melt_1.append(sum(melt_rate_db7)/len(melt_rate_db7)*obs_day[o-1]*area*0.04154052330139432/100)

    if len(melt_rate_db8) > 0:
        total_melt_1.append(sum(melt_rate_db8)/len(melt_rate_db8)*obs_day[o-1]*area*0.024694405617078932/100)

    if len(melt_rate_db9) > 0:
        total_melt_1.append(sum(melt_rate_db9)/len(melt_rate_db9)*obs_day[o-1]*area*0.005737052926748187/100)

    periodic_total_melt_o.append(sum(total_melt_1))
    o = o + 1

p = 1
periodic_total_melt_p = []
while p < 11:
    total_melt_1 = [] # melts of nth time period for each db band
    meltrate_n = []
    db_thickness_n = []
    obs_day = [10, 14, 13, 18, 16, 15, 17, 14, 14, 21]
    for mr, db, time in zip(melt_model_3, noised_db_thickness, time_period):
        if time == p:
            meltrate_n.append(mr)
            db_thickness_n.append(db)
    melt_rate_db1 = []
    melt_rate_db2 = []
    melt_rate_db3 = []
    melt_rate_db4 = []
    melt_rate_db5 = []
    melt_rate_db6 = []
    melt_rate_db7 = []
    melt_rate_db8 = []
    melt_rate_db9 = []

    for i, j in zip(meltrate_n, db_thickness_n):
        if 0 < j < 5.0001:
            melt_rate_db1.append(i)

        elif 5 < j < 15.0001:
            melt_rate_db2.append(i)

        elif 15 < j < 25.0001:
            melt_rate_db3.append(i)

        elif 25 < j < 35.0001:
            melt_rate_db4.append(i)

        elif 35 < j < 45.0001:
            melt_rate_db5.append(i)

        elif 45 < j < 60.0001:
            melt_rate_db6.append(i)

        elif 60 < j < 75.0001:
            melt_rate_db7.append(i)

        elif 75 < j < 100.0001:
            melt_rate_db8.append(i)

        elif 100 < j < 120.0001:
            melt_rate_db9.append(i)
    area = 12.0096
    if len(melt_rate_db1) > 0:
        total_melt_1.append(sum(melt_rate_db1)/len(melt_rate_db1)*obs_day[p-1]*area*0.22811620162583887/100)
    if len(melt_rate_db2) > 0:
        total_melt_1.append(sum(melt_rate_db2)/len(melt_rate_db2)*obs_day[p-1]*area*0.28558041049247607/100)
    if len(melt_rate_db3) > 0:
        total_melt_1.append(sum(melt_rate_db3)/len(melt_rate_db3)*obs_day[p-1]*area*0.13087821700879687/100)
    if len(melt_rate_db4) > 0:
        total_melt_1.append(sum(melt_rate_db4)/len(melt_rate_db4)*obs_day[p-1]*area*0.10558937279127911/100)

    if len(melt_rate_db5) > 0:
        total_melt_1.append(sum(melt_rate_db5)/len(melt_rate_db5)*obs_day[p-1]*area*0.12350830293632936/100)

    if len(melt_rate_db6) > 0:
        total_melt_1.append(sum(melt_rate_db6)/len(melt_rate_db6)*obs_day[p-1]*area*0.0543555133000583/100)

    if len(melt_rate_db7) > 0:
        total_melt_1.append(sum(melt_rate_db7)/len(melt_rate_db7)*obs_day[p-1]*area*0.04154052330139432/100)

    if len(melt_rate_db8) > 0:
        total_melt_1.append(sum(melt_rate_db8)/len(melt_rate_db8)*obs_day[p-1]*area*0.024694405617078932/100)

    if len(melt_rate_db9) > 0:
        total_melt_1.append(sum(melt_rate_db9)/len(melt_rate_db9)*obs_day[p-1]*area*0.005737052926748187/100)

    periodic_total_melt_p.append(sum(total_melt_1))
    p = p + 1

jd1 = [155, 169, 182, 200, 216, 231, 248, 262, 276]
jd2 = [168, 181, 199, 215, 230, 247, 261, 275, 296]
df = pd.DataFrame(jd1, columns=['Jd1'], index=list(range(2,11)))
df['Jd2'] = jd2
df['Observed Melt'] = periodic_total_melt_n[1:]
df['Model 1'] = periodic_total_melt_m[1:]
df['Model 2'] = periodic_total_melt_o[1:]
df['Model 3'] = periodic_total_melt_p[1:]


df.to_csv('F:\\Abhilah_First\\Results\\Era5Land\\Total_periodic_melt.csv')
