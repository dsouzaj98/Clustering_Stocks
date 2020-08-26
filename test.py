import pandas_datareader.data as web
import numpy as np
def testing(key, val):

    data_source='yahoo'

    start_date='2017-01-01'
    end_date='2020-08-24'
    test_dict={key:val}
    test_data=web.DataReader(list(us_dict.values())),data_source, start_date, end_date
    test_open=test_data["Open"]
    test_close=test_data["Close"]
    test_open=np.array(test_open).T 
    test_close=np.array(test_close).T 
    row, col=test_close.shape
    movement=np.zeros([row, col])
    for i in range(0, row):
        movement[i,:]=np.subtract(us_close[i,:], us_open[i,:])
    