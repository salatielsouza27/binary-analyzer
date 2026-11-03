import ta

def add_indicators(df):
    df["rsi"] = ta.momentum.RSIIndicator(close=df["Close"], window=14).rsi()
    df["ema9"] = ta.trend.EMAIndicator(close=df["Close"], window=9).ema_indicator()
    df["ema21"] = ta.trend.EMAIndicator(close=df["Close"], window=21).ema_indicator()
    macd = ta.trend.MACD(close=df["Close"])
    df["macd"] = macd.macd()
    df["macd_signal"] = macd.macd_signal()
    bb = ta.volatility.BollingerBands(close=df["Close"])
    df["bb_high"] = bb.bollinger_hband()
    df["bb_low"] = bb.bollinger_lband()
    df.dropna(inplace=True)
    return df
