import streamlit as st 
import yfinance as yf
from PIL import Image
from urllib.request import urlopen
#import pandas as pd
import requests


st.set_page_config(layout='wide')


def get_price(coin, currency='usd'):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}'
    response = requests.get(url)
    data = response.json()
    return data[coin][currency]

st.title('Cryptocurrency Price Calculator and Close Price Visualizer')

st.markdown('----')

# About
expander_bar = st.expander("About")
expander_bar.markdown("""
* **A crypto calculator to check cryptocurrency prices and visisual dashboard to view daily closing price of selected cryptocurrencies!**
* **Credit:** This is a modification of the work of **Bek Brace** a great teacher whose works inspire me.
""")

st.markdown('----')


coin = st.selectbox('Select a cryptocurrency', ['bitcoin', 'ethereum', 'dogecoin', 'ripple', 'cardano', 'dai', 'solana', 'litecoin'])

amount = st.number_input('Enter the amount of cryptocurrency')

usd_price = get_price(coin)

value = amount * usd_price

st.write(f'The current price of {coin} is {usd_price:.2f} USD.')
st.write(f'{amount} {coin.upper()} is worth {value:.2f} USD.')



st.markdown('----')

st.markdown('----')

st.header('**Visualizing Selected Daily Closing Price**')
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













