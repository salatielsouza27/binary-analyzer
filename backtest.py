def run_backtest(df):
    wins=0; losses=0
    for i in range(50,len(df)-1):
        c=df.iloc[i]; n=df.iloc[i+1]
        if c["ema9"]>c["ema21"]:
            wins += int(n["Close"]>c["Close"])
            losses += int(n["Close"]<=c["Close"])
        elif c["ema9"]<c["ema21"]:
            wins += int(n["Close"]<c["Close"])
            losses += int(n["Close"]>=c["Close"])
    t=wins+losses
    return round((wins/t)*100,2) if t else 0
