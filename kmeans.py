from sklearn.preprocessing import Normalizer
from mywork import *
us_df=pd.concat(us_df)
close_data=us_df["Adj Close"]
open_data=us_df["Open"]

print(close_data.iloc[0])
normalizer=Normalizer()

