import streamlit as st, yfinance as yf, plotly.graph_objects as go
from indicators import add_indicators
from signal_engine import generate_signal
from backtest import run_backtest
st.title('Binary Options Analyzer')
df=yf.download('EURUSD=X',period='30d',interval='5m',auto_adjust=True)
if df.empty: st.stop()
df=add_indicators(df)
signal,prob=generate_signal(df)
st.metric('Sinal',signal)
st.metric('Probabilidade',f'{prob}%')
st.metric('Backtest',f'{run_backtest(df)}%')
fig=go.Figure(data=[go.Candlestick(x=df.index,open=df['Open'],high=df['High'],low=df['Low'],close=df['Close'])])
st.plotly_chart(fig,use_container_width=True)
