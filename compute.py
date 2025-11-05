import pandas as pd


def rsi(series: pd.Series, period: int = 14) -> pd.Series:
delta = series.diff()
gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
rs = gain / loss
return 100 - (100 / (1 + rs))


def macd(series: pd.Series, fast=12, slow=26, signal=9):
ema_fast = series.ewm(span=fast, adjust=False).mean()
ema_slow = series.ewm(span=slow, adjust=False).mean()
macd_line = ema_fast - ema_slow
signal_line = macd_line.ewm(span=signal, adjust=False).mean()
hist = macd_line - signal_line
return macd_line, signal_line, hist
