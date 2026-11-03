from sklearn.ensemble import RandomForestClassifier
import joblib
FEATURES=["rsi","ema9","ema21","macd"]

def train_model(df):
    df=df.copy()
    df["target"]=(df["Close"].shift(-1)>df["Close"]).astype(int)
    df.dropna(inplace=True)
    X=df[FEATURES]; y=df["target"]
    m=RandomForestClassifier(n_estimators=200,random_state=42)
    m.fit(X,y)
    joblib.dump(m,'random_forest.pkl')
    return m
