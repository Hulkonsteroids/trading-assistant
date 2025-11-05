import pandas as pd
from .compute import rsi, macd


def generate_signals(df: pd.DataFrame):
df = df.copy()
df["rsi14"] = rsi(df["close"], 14)
macd_line, signal_line, hist = macd(df["close"])
df["macd"] = macd_line
df["macd_signal"] = signal_line
df["macd_hist"] = hist


# Very simple rule: RSI cross + MACD confirmation
df["signal"] = "hold"
buy = (df["rsi14"].shift(1) < 30) & (df["rsi14"] >= 30) & (df["macd_hist"] > 0)
sell = (df["rsi14"].shift(1) > 70) & (df["rsi14"] <= 70) & (df["macd_hist"] < 0)
df.loc[buy, "signal"] = "buy"
df.loc[sell, "signal"] = "sell"
return df
