#!/usr/bin/env python
# @Time    : 2019/3/23 15:39
# @Author  : wb
# @File    : arima_test.py

# arima的时间序列

from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

dta=[10930,10318,10595,10972,7706,6756,9092,10551,9722,10913,11151,8186,6422,

6337,11649,11652,10310,12043,7937,6476,9662,9570,9981,9331,9449,6773,6304,9355,

10477,10148,10395,11261,8713,7299,10424,10795,11069,11602,11427,9095,7707,10767,

12136,12812,12006,12528,10329,7818,11719,11683,12603,11495,13670,11337,10232,

13261,13230,15535,16837,19598,14823,11622,19391,18177,19994,14723,15694,13248,

9543,12872,13101,15053,12619,13749,10228,9725,14729,12518,14564,15085,14722,

11999,9390,13481,14795,15845,15271,14686,11054,10395]



dta=np.array(dta,dtype=np.float)

#生成时间序列并画图

dta=pd.Series(dta)

dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2001','2090'))

dta.plot(figsize=(12,8))

plt.show()