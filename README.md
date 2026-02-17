# nubra_talib

TA-Lib helper functions built on Nubra historical data.

## Install

```
pip install nubra_talib
```

## Usage

```python
from nubra_talib import to_ohlcv_df, add_talib, add_basics

df = to_ohlcv_df(result, symbol="ASIANPAINT")

df = add_talib(
    df,
    funcs={
        "RSI": {"timeperiod": 14},
        "EMA": {"timeperiod": 21},
        "MACD": {"fastperiod": 12, "slowperiod": 26, "signalperiod": 9},
    },
)

df = add_basics(df)
```
