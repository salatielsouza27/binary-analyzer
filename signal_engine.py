def generate_signal(df):
    if len(df)==0: return "SEM DADOS",0
    last=df.iloc[-1]
    call_score=0; put_score=0
    if last["rsi"]<30: call_score+=1
    elif last["rsi"]>70: put_score+=1
    if last["ema9"]>last["ema21"]: call_score+=1
    elif last["ema9"]<last["ema21"]: put_score+=1
    if last["macd"]>last["macd_signal"]: call_score+=1
    elif last["macd"]<last["macd_signal"]: put_score+=1
    total=call_score+put_score
    if total==0: return "AGUARDAR",50
    if call_score>put_score: return "CALL",round(call_score/total*100,2)
    if put_score>call_score: return "PUT",round(put_score/total*100,2)
    return "AGUARDAR",50
