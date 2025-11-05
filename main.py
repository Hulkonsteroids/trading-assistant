from fastapi import FastAPI
from .routers import health, candles, indicators, signals


app = FastAPI(title="Trading Assistant API", version="0.1.0")
app.include_router(health.router)
app.include_router(candles.router, prefix="/candles", tags=["candles"])
app.include_router(indicators.router, prefix="/indicators", tags=["indicators"])
app.include_router(signals.router, prefix="/signals", tags=["signals"])


@app.get("/tickers")
def tickers():
return ["AMD","NVDA","AAPL","MSFT","PLTR","ORCL","COIN","WMT","SNAP","NIO","TLRY"]
