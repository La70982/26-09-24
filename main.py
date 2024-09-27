import os
import pandas as pandas
import matplotlib.pyplot as pyplot
market:caps={
    'AAPL':2300,
    'MSFT':2100
    'GOOGL':1600
    'AMZN':1700
    'TSLA':900
    'BRK-B':600
    'NVDA':500
    'META':700
    'JNJ':400
    'V'"500
}
TOP-10-COMPANIES={
    'AAPL':'APPLE  INC.',
    'MSFT':'MICROSOFT CORPORATION',
    'GOOGL':'ALPHABET INC.',
    'AMZN':'AMAZON.COM,INC.',
    'JSLA':'TESLA,INC.',
    'BRK-B':'BERKSHLRE HATHAWAY INC.',
    'NVDA':'NVIDIA CORPORATION',
    'META':'META PLATFORM,INC.',
    'JNJ':'JOHNSON& JOHNSON',
    'V':'VISA INC'.
}
current-directory=OS.path.dirname(OS.path abspath(file-))
csv-file-path=os.path.join(current-directory,'top-10-stocks-sample-2013-2023.csv')
df=pd.read-csv(csv-file-path)
df('pate')=pd.to-datetime(df['date'])
df('year')=df['date'].dt.year
stock-colums=['AAPL-CLOSE','MSFT-CLOSE','GOOGL-CLOSE','AMZN-CLOSE','BRK-B-CLOSE','NVDA-CLOSE','META-CLOSE','JNJ-CLOSE','V-CLOSE']
AVERAGE-prices=df.group by('year')[stock-colums].mean().reset-index()
plt.figure(figsize=(20,10))
bar-width=0.1
years=average-prices['year']
positions=[years+i*bar-width for i in range (len(stock-columns))]
for i,column in enumerate (stock-column):
    plt.bar(position[i] ,average-prices[column],width=bar-width,label=column.split('-') [0])
    plt.x label('year')
    plt.y label('average closing price of top 10 stocks (2013-2023)')
    plt.xticks(years+bar-width*4.5,years)
    plt.legend()
    plt.tight-layout()
    plt.show 