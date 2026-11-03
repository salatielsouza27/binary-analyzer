import yfinance as yf
from indicators import add_indicators
from model import train_model
df=yf.download('EURUSD=X',period='60d',interval='5m',auto_adjust=True)
df=add_indicators(df)
train_model(df)
print('Modelo treinado')
