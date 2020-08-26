import pandas_datareader.data as web
import numpy as np
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import make_pipeline
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from kmeans import movements, km
def testing(key, val, clusters=2):

    data_source='yahoo'
    start_date='2017-01-01'
    end_date='2020-08-24'
    test_dict={key:val}
    test_data=web.DataReader(val,data_source, start_date, end_date)
    test_open=test_data["Open"]
    test_close=test_data["Close"]
    test_open=np.array(test_open).T 
    test_close=np.array(test_close).T 
    test_movement=np.subtract(test_close[:900], test_open[:900])
    new_movements=np.append(movements, test_movement, axis=0)
    x=km(new_movements)
    return (movements.shape)
    
print(testing('Tesla', 'TSLA'))

    