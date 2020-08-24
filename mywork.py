import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook 
import numpy as np
import datetime


#creates dataframes for each country
US_tickers=["AAPL", "AMZN","BRK-B","FB","GOOGL","HD","INTC", "JNJ","JPM","MA","MSFT","PG","UNH","V","VZ"]
US_names=["Apple", "Amazon", "Berkshire Hathaway", "Facebook", "Google","Home Depot", "Intel", "Johnson and Johnson", "JP Morgan Chase", "Mastercard","Microsoft","Proctor and Gamble","United Health","Visa","Verizon"]
China_tickers=["0700.HK", "0005.HK","0939.HK","0941.HK","1288.HK","1299.HK","1398.HK","1658.HK","2318.HK","2628.HK", "3690.HK","3698.HK","3988.HK","9618.HK","9988.HK"]
China_names=["Tencent","HSBC", "CCB","China Mobile", "ABC", "AIA", "ICBC", "PSBC", "PING AN", "China Life", "Metuan","CM Bank", "Bank of China", "JD.com", "Alibaba"]
us_df={}
china_df={}
us_data=[]
china_data=[]

years=mdates.YearLocator()
months=mdates.MonthLocator()
years_fmt=mdates.DateFormatter('%Y')
for df, tick in zip(US_names, US_tickers):
    fig, ax=plt.subplots(1,1)
    us_df[df]=pd.read_csv(f'data/American/{tick}.csv')
    us_array=np.array(us_df[df]["Adj Close"])
    
    ax.plot(us_df[df]["Date"], us_array, label=df)
    # ax.xaxis.set_major_locator(years)
    # ax.xaxis.set_major_formatter(years_fmt)
    # ax.xaxis.set_minor_locator(months)
    # datemin=np.datetime64(us_df[df]["Date"][0], 'M')
    # datemax=np.datetime64(us_df[df]["Date"].iloc[-1], 'M')+np.timedelta64(1,'M')
    # ax.set_xlim(datemin, datemax)
    ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
    ax.format_ydata = lambda x: '$%1.2f' % x  # format the price.
    ax.grid(True)
    fig.autofmt_xdate()
    plt.title(f"{df} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Stock Price ($)")
    plt.legend()
    plt.show()


    

# fig1, ax1=plt.subplots(1,1)
# for df, tick in zip(China_names, China_tickers):
    
#     china_df[df]=pd.read_csv(f"data/Chinese/{tick}.csv")
#     china_data.append(china_df[df]["Adj Close"])
#     china_array=np.array(china_data)
#     ax1.plot(china_df[df]["Date"], china_array, label=df)
#     plt.legend()
#     plt.show()





