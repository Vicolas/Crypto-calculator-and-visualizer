import streamlit as st 
import yfinance as yf
from PIL import Image
from urllib.request import urlopen
import pandas as pd


st.set_page_config(layout='wide')

st.title('Cryptocurrency Realtime Prices From Binance API And CoinMarketCap.')
st.markdown("""
This app visualizes cryptocurrency prices from the **CoinMarketCap** & **Binance** To Highlight Differences OR Similarities In Displayed Prices!
""")



# About
expander_bar = st.expander("About")
expander_bar.markdown("""
* **A display of crypto prices from 2 different markets!**
* **Data sources:** [CoinMarketCap](http://coinmarketcap.com) & [Binance API](https://api.binance.com/api/v3/ticker/24hr)
* **Credit:** This is a combination of the works of **Chanin Nantasenamat** and **Bek Brace** both great teachers whose works inspire me.
""")


st.markdown('----')

# Load market data from Binance API
st.subheader('Selected Price')
df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

# Custom function for rounding values
def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 8))
    return a

col1, col2, col3 = st.columns(3)


# Widget (Cryptocurrency selection box)
st.sidebar.header('**Select Cryptocurrency**')
col1_selection = st.sidebar.selectbox('Price 1', df.symbol, list(df.symbol).index('BTCBUSD') )
col2_selection = st.sidebar.selectbox('Price 2', df.symbol, list(df.symbol).index('ETHBUSD') )
col3_selection = st.sidebar.selectbox('Price 3', df.symbol, list(df.symbol).index('BNBBUSD') )
col4_selection = st.sidebar.selectbox('Price 4', df.symbol, list(df.symbol).index('XRPBUSD') )
col5_selection = st.sidebar.selectbox('Price 5', df.symbol, list(df.symbol).index('ADABUSD') )
col6_selection = st.sidebar.selectbox('Price 6', df.symbol, list(df.symbol).index('DOGEBUSD') )
col7_selection = st.sidebar.selectbox('Price 7', df.symbol, list(df.symbol).index('SHIBBUSD') )
col8_selection = st.sidebar.selectbox('Price 8', df.symbol, list(df.symbol).index('DOTBUSD') )
col9_selection = st.sidebar.selectbox('Price 9', df.symbol, list(df.symbol).index('MATICBUSD') )



# DataFrame of selected Cryptocurrency
col1_df = df[df.symbol == col1_selection]
col2_df = df[df.symbol == col2_selection]
col3_df = df[df.symbol == col3_selection]
col4_df = df[df.symbol == col4_selection]
col5_df = df[df.symbol == col5_selection]
col6_df = df[df.symbol == col6_selection]
col7_df = df[df.symbol == col7_selection]
col8_df = df[df.symbol == col8_selection]
col9_df = df[df.symbol == col9_selection]



# Apply a custom function to conditionally round values
col1_price = round_value(col1_df.weightedAvgPrice)
col2_price = round_value(col2_df.weightedAvgPrice)
col3_price = round_value(col3_df.weightedAvgPrice)
col4_price = round_value(col4_df.weightedAvgPrice)
col5_price = round_value(col5_df.weightedAvgPrice)
col6_price = round_value(col6_df.weightedAvgPrice)
col7_price = round_value(col7_df.weightedAvgPrice)
col8_price = round_value(col8_df.weightedAvgPrice)
col9_price = round_value(col9_df.weightedAvgPrice)



# Select the priceChangePercent column
col1_percent = f'{float(col1_df.priceChangePercent)}%'
col2_percent = f'{float(col2_df.priceChangePercent)}%'
col3_percent = f'{float(col3_df.priceChangePercent)}%'
col4_percent = f'{float(col4_df.priceChangePercent)}%'
col5_percent = f'{float(col5_df.priceChangePercent)}%'
col6_percent = f'{float(col6_df.priceChangePercent)}%'
col7_percent = f'{float(col7_df.priceChangePercent)}%'
col8_percent = f'{float(col8_df.priceChangePercent)}%'
col9_percent = f'{float(col9_df.priceChangePercent)}%'



# Create a metrics price box
col1.metric(col1_selection, col1_price, col1_percent)
col2.metric(col2_selection, col2_price, col2_percent)
col3.metric(col3_selection, col3_price, col3_percent)
col1.metric(col4_selection, col4_price, col4_percent)
col2.metric(col5_selection, col5_price, col5_percent)
col3.metric(col6_selection, col6_price, col6_percent)
col1.metric(col7_selection, col7_price, col7_percent)
col2.metric(col8_selection, col8_price, col8_percent)
col3.metric(col9_selection, col9_price, col9_percent)

st.subheader('All Binance Price')
table = st.dataframe(df)

st.markdown('----')

st.markdown('----')

st.header('**Visualizing Price Difference on CoinMarketCap**')
st.markdown("""
Thie dashboard visualizes prices of 5 distinct cryptocurrencies from the **CoinMarketCap** 
""")
#defining the ticker symbol
Bitcoin = 'BTC-USD'
Binance = 'BNB-USD'
Ethereum = 'ETH-USD'
Ripple = 'XRP-USD'
BitcoinCash = 'BCH-USD'


#access data from yahoo finance
BTC_Data = yf.Ticker(Bitcoin)
BNB_Data = yf.Ticker(Binance)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(BitcoinCash)


#getting history data
BTChis = BTC_Data.history(period='max')
BNBhis = BNB_Data.history(period='max')
ETHhis = ETH_Data.history(period='max')
XRPhis = XRP_Data.history(period='max')
BCHhis = BCH_Data.history(period='max')


#crypto data table
BTC = yf.download(Bitcoin, start='2023-03-17', end='2023-03-17')
BNB = yf.download(Binance, start='2023-03-17', end='2023-03-17')
ETH = yf.download(Ethereum, start='2023-03-17', end='2023-03-17')
XRP = yf.download(Ripple, start='2023-03-17', end='2023-03-17')
BCH = yf.download(BitcoinCash, start='2023-03-17', end='2023-03-17')
 

#bitcoin
st.write('Bitcoin ($)')
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
st.image(imageBTC)
st.bar_chart(BTChis.Close)


#Binance
st.write('Binance ($)')
imageBNB = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1839.png'))
st.image(imageBNB)
st.bar_chart(BNBhis.Close)


#Ethereum
st.write('Ethereum ($)')
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
st.image(imageETH)
st.bar_chart(ETHhis.Close)


#Ripple
st.write('Ripple ($)')
imageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
st.image(imageXRP)
st.bar_chart(XRPhis.Close)


#BitcoinCash
st.write('BitcoinCash ($)')
imageBCH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png'))
st.image(imageBCH)
st.bar_chart(BCHhis.Close)













