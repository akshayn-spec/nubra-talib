# nubra_talib

TA-Lib helper functions built on Nubra historical data.

## Install

```
pip install -i https://test.pypi.org/simple/ nubra-talib
```

## Usage

```python
from nubra_python_sdk.marketdata.market_data import MarketData
from nubra_python_sdk.start_sdk import InitNubraSdk, NubraEnv

from nubra_talib import to_ohlcv_df, to_ist, add_talib, add_basics


def main():
    # Initialize the Nubra SDK client
    # Use NubraEnv.UAT for testing or NubraEnv.PROD for production
    nubra = InitNubraSdk(NubraEnv.PROD)

    # Initialize MarketData with the client
    md_instance = MarketData(nubra)

    result = md_instance.historical_data({
        "exchange": "NSE",
        "type": "STOCK",
        "values": ["ASHOKLEY", "TMPV"],
        "fields": ["close", "high", "low", "open", "cumulative_volume"],
        "startDate": "2026-01-01T11:01:57.000Z",
        "endDate": "2026-02-16T06:13:57.000Z",
        "interval": "3m",
        "intraDay": False,
        "realTime": False,
    })

    # By default, datetime is converted to IST and prices to rupees
    df = to_ohlcv_df(result, symbol="ASHOKLEY", interval="3m")

    df = add_talib(
        df,
        funcs={
            "RSI": {"timeperiod": 14},
            "EMA": {"timeperiod": 21},
            "CCI": {"timeperiod": 14},
            # "MACD": {"fastperiod": 12, "slowperiod": 26, "signalperiod": 9},
        },
    )

    # df = add_basics(df)

    print(df.tail())


if __name__ == "__main__":
    main()
```

# Indicator Groups

- Cycle Indicators
- Math Operators
- Math Transform
- Momentum Indicators
- Overlap Studies
- Pattern Recognition
- Price Transform
- Statistic Functions
- Volatility Indicators
- Volume Indicators

## Cycle Indicators

| Type | Description | Code Line |
|---|---|---|
| `HT_DCPERIOD` | Hilbert Transform - Dominant Cycle Period | `"HT_DCPERIOD": {}` |
| `HT_DCPHASE` | Hilbert Transform - Dominant Cycle Phase | `"HT_DCPHASE": {}` |
| `HT_PHASOR` | Hilbert Transform - Phasor Components | `"HT_PHASOR": {}` |
| `HT_SINE` | Hilbert Transform - SineWave | `"HT_SINE": {}` |
| `HT_TRENDMODE` | Hilbert Transform - Trend vs Cycle Mode | `"HT_TRENDMODE": {}` |

## Math Operators

| Type | Description | Code Line |
|---|---|---|
| `ADD` | Vector Arithmetic Add | `"ADD": {}` |
| `DIV` | Vector Arithmetic Div | `"DIV": {}` |
| `MAX` | Highest value over a specified period | `"MAX": {"timeperiod": 30}` |
| `MAXINDEX` | Index of highest value over a specified period | `"MAXINDEX": {"timeperiod": 30}` |
| `MIN` | Lowest value over a specified period | `"MIN": {"timeperiod": 30}` |
| `MININDEX` | Index of lowest value over a specified period | `"MININDEX": {"timeperiod": 30}` |
| `MINMAX` | Lowest and highest values over a specified period | `"MINMAX": {"timeperiod": 30}` |
| `MINMAXINDEX` | Indexes of lowest and highest values over a specified period | `"MINMAXINDEX": {"timeperiod": 30}` |
| `MULT` | Vector Arithmetic Mult | `"MULT": {}` |
| `SUB` | Vector Arithmetic Subtraction | `"SUB": {}` |
| `SUM` | Summation | `"SUM": {"timeperiod": 30}` |

## Math Transform

| Type | Description | Code Line |
|---|---|---|
| `ACOS` | Vector Trigonometric ACos | `"ACOS": {}` |
| `ASIN` | Vector Trigonometric ASin | `"ASIN": {}` |
| `ATAN` | Vector Trigonometric ATan | `"ATAN": {}` |
| `CEIL` | Vector Ceil | `"CEIL": {}` |
| `COS` | Vector Trigonometric Cos | `"COS": {}` |
| `COSH` | Vector Trigonometric Cosh | `"COSH": {}` |
| `EXP` | Vector Arithmetic Exp | `"EXP": {}` |
| `FLOOR` | Vector Floor | `"FLOOR": {}` |
| `LN` | Vector Log Natural | `"LN": {}` |
| `LOG10` | Vector Log10 | `"LOG10": {}` |
| `SIN` | Vector Trigonometric Sin | `"SIN": {}` |
| `SINH` | Vector Trigonometric Sinh | `"SINH": {}` |
| `SQRT` | Vector Square Root | `"SQRT": {}` |
| `TAN` | Vector Trigonometric Tan | `"TAN": {}` |
| `TANH` | Vector Trigonometric Tanh | `"TANH": {}` |

## Momentum Indicators

| Type | Description | Code Line |
|---|---|---|
| `ADX` | Average Directional Movement Index | `"ADX": {"timeperiod": 14}` |
| `ADXR` | Average Directional Movement Index Rating | `"ADXR": {"timeperiod": 14}` |
| `APO` | Absolute Price Oscillator | `"APO": {"fastperiod": 12, "slowperiod": 26, "matype": 0}` |
| `AROON` | Aroon | `"AROON": {"timeperiod": 14}` |
| `AROONOSC` | Aroon Oscillator | `"AROONOSC": {"timeperiod": 14}` |
| `BOP` | Balance Of Power | `"BOP": {}` |
| `CCI` | Commodity Channel Index | `"CCI": {"timeperiod": 14}` |
| `CMO` | Chande Momentum Oscillator | `"CMO": {"timeperiod": 14}` |
| `DX` | Directional Movement Index | `"DX": {"timeperiod": 14}` |
| `MACD` | Moving Average Convergence/Divergence | `"MACD": {"fastperiod": 12, "slowperiod": 26, "signalperiod": 9}` |
| `MACDEXT` | MACD with controllable MA type | `"MACDEXT": {"fastperiod": 12, "fastmatype": 0, "slowperiod": 26, "slowmatype": 0, "signalperiod": 9, "signalmatype": 0}` |
| `MACDFIX` | Moving Average Convergence/Divergence Fix 12/26 | `"MACDFIX": {"signalperiod": 9}` |
| `MFI` | Money Flow Index | `"MFI": {"timeperiod": 14}` |
| `MINUS_DI` | Minus Directional Indicator | `"MINUS_DI": {"timeperiod": 14}` |
| `MINUS_DM` | Minus Directional Movement | `"MINUS_DM": {"timeperiod": 14}` |
| `MOM` | Momentum | `"MOM": {"timeperiod": 10}` |
| `PLUS_DI` | Plus Directional Indicator | `"PLUS_DI": {"timeperiod": 14}` |
| `PLUS_DM` | Plus Directional Movement | `"PLUS_DM": {"timeperiod": 14}` |
| `PPO` | Percentage Price Oscillator | `"PPO": {"fastperiod": 12, "slowperiod": 26, "matype": 0}` |
| `ROC` | Rate of change : ((price/prevPrice)-1)*100 | `"ROC": {"timeperiod": 10}` |
| `ROCP` | Rate of change Percentage: (price-prevPrice)/prevPrice | `"ROCP": {"timeperiod": 10}` |
| `ROCR` | Rate of change ratio: (price/prevPrice) | `"ROCR": {"timeperiod": 10}` |
| `ROCR100` | Rate of change ratio 100 scale: (price/prevPrice)*100 | `"ROCR100": {"timeperiod": 10}` |
| `RSI` | Relative Strength Index | `"RSI": {"timeperiod": 14}` |
| `STOCH` | Stochastic | `"STOCH": {"fastk_period": 5, "slowk_period": 3, "slowk_matype": 0, "slowd_period": 3, "slowd_matype": 0}` |
| `STOCHF` | Stochastic Fast | `"STOCHF": {"fastk_period": 5, "fastd_period": 3, "fastd_matype": 0}` |
| `STOCHRSI` | Stochastic Relative Strength Index | `"STOCHRSI": {"timeperiod": 14, "fastk_period": 5, "fastd_period": 3, "fastd_matype": 0}` |
| `TRIX` | 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA | `"TRIX": {"timeperiod": 30}` |
| `ULTOSC` | Ultimate Oscillator | `"ULTOSC": {"timeperiod1": 7, "timeperiod2": 14, "timeperiod3": 28}` |
| `WILLR` | Williams' %R | `"WILLR": {"timeperiod": 14}` |

## Overlap Studies

| Type | Description | Code Line |
|---|---|---|
| `BBANDS` | Bollinger Bands | `"BBANDS": {"timeperiod": 5, "nbdevup": 2.0, "nbdevdn": 2.0, "matype": 0}` |
| `DEMA` | Double Exponential Moving Average | `"DEMA": {"timeperiod": 30}` |
| `EMA` | Exponential Moving Average | `"EMA": {"timeperiod": 30}` |
| `HT_TRENDLINE` | Hilbert Transform - Instantaneous Trendline | `"HT_TRENDLINE": {}` |
| `KAMA` | Kaufman Adaptive Moving Average | `"KAMA": {"timeperiod": 30}` |
| `MA` | Moving average | `"MA": {"timeperiod": 30, "matype": 0}` |
| `MAMA` | MESA Adaptive Moving Average | `"MAMA": {"fastlimit": 0.5, "slowlimit": 0.05}` |
| `MAVP` | Moving average with variable period | `"MAVP": {"minperiod": 2, "maxperiod": 30, "matype": 0}` |
| `MIDPOINT` | MidPoint over period | `"MIDPOINT": {"timeperiod": 14}` |
| `MIDPRICE` | Midpoint Price over period | `"MIDPRICE": {"timeperiod": 14}` |
| `SAR` | Parabolic SAR | `"SAR": {"acceleration": 0.02, "maximum": 0.2}` |
| `SAREXT` | Parabolic SAR - Extended | `"SAREXT": {"startvalue": 0.0, "offsetonreverse": 0.0, "accelerationinitlong": 0.02, "accelerationlong": 0.02, "accelerationmaxlong": 0.2, "accelerationinitshort": 0.02, "accelerationshort": 0.02, "accelerationmaxshort": 0.2}` |
| `SMA` | Simple Moving Average | `"SMA": {"timeperiod": 30}` |
| `T3` | Triple Exponential Moving Average (T3) | `"T3": {"timeperiod": 5, "vfactor": 0.7}` |
| `TEMA` | Triple Exponential Moving Average | `"TEMA": {"timeperiod": 30}` |
| `TRIMA` | Triangular Moving Average | `"TRIMA": {"timeperiod": 30}` |
| `WMA` | Weighted Moving Average | `"WMA": {"timeperiod": 30}` |

## Pattern Recognition

| Type | Description | Code Line |
|---|---|---|
| `CDL2CROWS` | Two Crows | `"CDL2CROWS": {}` |
| `CDL3BLACKCROWS` | Three Black Crows | `"CDL3BLACKCROWS": {}` |
| `CDL3INSIDE` | Three Inside Up/Down | `"CDL3INSIDE": {}` |
| `CDL3LINESTRIKE` | Three-Line Strike | `"CDL3LINESTRIKE": {}` |
| `CDL3OUTSIDE` | Three Outside Up/Down | `"CDL3OUTSIDE": {}` |
| `CDL3STARSINSOUTH` | Three Stars In The South | `"CDL3STARSINSOUTH": {}` |
| `CDL3WHITESOLDIERS` | Three Advancing White Soldiers | `"CDL3WHITESOLDIERS": {}` |
| `CDLABANDONEDBABY` | Abandoned Baby | `"CDLABANDONEDBABY": {"penetration": 0.3}` |
| `CDLADVANCEBLOCK` | Advance Block | `"CDLADVANCEBLOCK": {}` |
| `CDLBELTHOLD` | Belt-hold | `"CDLBELTHOLD": {}` |
| `CDLBREAKAWAY` | Breakaway | `"CDLBREAKAWAY": {}` |
| `CDLCLOSINGMARUBOZU` | Closing Marubozu | `"CDLCLOSINGMARUBOZU": {}` |
| `CDLCONCEALBABYSWALL` | Concealing Baby Swallow | `"CDLCONCEALBABYSWALL": {}` |
| `CDLCOUNTERATTACK` | Counterattack | `"CDLCOUNTERATTACK": {}` |
| `CDLDARKCLOUDCOVER` | Dark Cloud Cover | `"CDLDARKCLOUDCOVER": {"penetration": 0.5}` |
| `CDLDOJI` | Doji | `"CDLDOJI": {}` |
| `CDLDOJISTAR` | Doji Star | `"CDLDOJISTAR": {}` |
| `CDLDRAGONFLYDOJI` | Dragonfly Doji | `"CDLDRAGONFLYDOJI": {}` |
| `CDLENGULFING` | Engulfing Pattern | `"CDLENGULFING": {}` |
| `CDLEVENINGDOJISTAR` | Evening Doji Star | `"CDLEVENINGDOJISTAR": {"penetration": 0.3}` |
| `CDLEVENINGSTAR` | Evening Star | `"CDLEVENINGSTAR": {"penetration": 0.3}` |
| `CDLGAPSIDESIDEWHITE` | Up/Down-gap side-by-side white lines | `"CDLGAPSIDESIDEWHITE": {}` |
| `CDLGRAVESTONEDOJI` | Gravestone Doji | `"CDLGRAVESTONEDOJI": {}` |
| `CDLHAMMER` | Hammer | `"CDLHAMMER": {}` |
| `CDLHANGINGMAN` | Hanging Man | `"CDLHANGINGMAN": {}` |
| `CDLHARAMI` | Harami Pattern | `"CDLHARAMI": {}` |
| `CDLHARAMICROSS` | Harami Cross Pattern | `"CDLHARAMICROSS": {}` |
| `CDLHIGHWAVE` | High-Wave Candle | `"CDLHIGHWAVE": {}` |
| `CDLHIKKAKE` | Hikkake Pattern | `"CDLHIKKAKE": {}` |
| `CDLHIKKAKEMOD` | Modified Hikkake Pattern | `"CDLHIKKAKEMOD": {}` |
| `CDLHOMINGPIGEON` | Homing Pigeon | `"CDLHOMINGPIGEON": {}` |
| `CDLIDENTICAL3CROWS` | Identical Three Crows | `"CDLIDENTICAL3CROWS": {}` |
| `CDLINNECK` | In-Neck Pattern | `"CDLINNECK": {}` |
| `CDLINVERTEDHAMMER` | Inverted Hammer | `"CDLINVERTEDHAMMER": {}` |
| `CDLKICKING` | Kicking | `"CDLKICKING": {}` |
| `CDLKICKINGBYLENGTH` | Kicking - bull/bear determined by the longer marubozu | `"CDLKICKINGBYLENGTH": {}` |
| `CDLLADDERBOTTOM` | Ladder Bottom | `"CDLLADDERBOTTOM": {}` |
| `CDLLONGLEGGEDDOJI` | Long Legged Doji | `"CDLLONGLEGGEDDOJI": {}` |
| `CDLLONGLINE` | Long Line Candle | `"CDLLONGLINE": {}` |
| `CDLMARUBOZU` | Marubozu | `"CDLMARUBOZU": {}` |
| `CDLMATCHINGLOW` | Matching Low | `"CDLMATCHINGLOW": {}` |
| `CDLMATHOLD` | Mat Hold | `"CDLMATHOLD": {"penetration": 0.5}` |
| `CDLMORNINGDOJISTAR` | Morning Doji Star | `"CDLMORNINGDOJISTAR": {"penetration": 0.3}` |
| `CDLMORNINGSTAR` | Morning Star | `"CDLMORNINGSTAR": {"penetration": 0.3}` |
| `CDLONNECK` | On-Neck Pattern | `"CDLONNECK": {}` |
| `CDLPIERCING` | Piercing Pattern | `"CDLPIERCING": {}` |
| `CDLRICKSHAWMAN` | Rickshaw Man | `"CDLRICKSHAWMAN": {}` |
| `CDLRISEFALL3METHODS` | Rising/Falling Three Methods | `"CDLRISEFALL3METHODS": {}` |
| `CDLSEPARATINGLINES` | Separating Lines | `"CDLSEPARATINGLINES": {}` |
| `CDLSHOOTINGSTAR` | Shooting Star | `"CDLSHOOTINGSTAR": {}` |
| `CDLSHORTLINE` | Short Line Candle | `"CDLSHORTLINE": {}` |
| `CDLSPINNINGTOP` | Spinning Top | `"CDLSPINNINGTOP": {}` |
| `CDLSTALLEDPATTERN` | Stalled Pattern | `"CDLSTALLEDPATTERN": {}` |
| `CDLSTICKSANDWICH` | Stick Sandwich | `"CDLSTICKSANDWICH": {}` |
| `CDLTAKURI` | Takuri (Dragonfly Doji with very long lower shadow) | `"CDLTAKURI": {}` |
| `CDLTASUKIGAP` | Tasuki Gap | `"CDLTASUKIGAP": {}` |
| `CDLTHRUSTING` | Thrusting Pattern | `"CDLTHRUSTING": {}` |
| `CDLTRISTAR` | Tristar Pattern | `"CDLTRISTAR": {}` |
| `CDLUNIQUE3RIVER` | Unique 3 River | `"CDLUNIQUE3RIVER": {}` |
| `CDLUPSIDEGAP2CROWS` | Upside Gap Two Crows | `"CDLUPSIDEGAP2CROWS": {}` |
| `CDLXSIDEGAP3METHODS` | Upside/Downside Gap Three Methods | `"CDLXSIDEGAP3METHODS": {}` |

## Price Transform

| Type | Description | Code Line |
|---|---|---|
| `AVGPRICE` | Average Price | `"AVGPRICE": {}` |
| `MEDPRICE` | Median Price | `"MEDPRICE": {}` |
| `TYPPRICE` | Typical Price | `"TYPPRICE": {}` |
| `WCLPRICE` | Weighted Close Price | `"WCLPRICE": {}` |

## Statistic Functions

| Type | Description | Code Line |
|---|---|---|
| `BETA` | Beta | `"BETA": {"timeperiod": 5}` |
| `CORREL` | Pearson's Correlation Coefficient (r) | `"CORREL": {"timeperiod": 30}` |
| `LINEARREG` | Linear Regression | `"LINEARREG": {"timeperiod": 14}` |
| `LINEARREG_ANGLE` | Linear Regression Angle | `"LINEARREG_ANGLE": {"timeperiod": 14}` |
| `LINEARREG_INTERCEPT` | Linear Regression Intercept | `"LINEARREG_INTERCEPT": {"timeperiod": 14}` |
| `LINEARREG_SLOPE` | Linear Regression Slope | `"LINEARREG_SLOPE": {"timeperiod": 14}` |
| `STDDEV` | Standard Deviation | `"STDDEV": {"timeperiod": 5, "nbdev": 1.0}` |
| `TSF` | Time Series Forecast | `"TSF": {"timeperiod": 14}` |
| `VAR` | Variance | `"VAR": {"timeperiod": 5, "nbdev": 1.0}` |

## Volatility Indicators

| Type | Description | Code Line |
|---|---|---|
| `ATR` | Average True Range | `"ATR": {"timeperiod": 14}` |
| `NATR` | Normalized Average True Range | `"NATR": {"timeperiod": 14}` |
| `TRANGE` | True Range | `"TRANGE": {}` |

## Volume Indicators

| Type | Description | Code Line |
|---|---|---|
| `AD` | Chaikin A/D Line | `"AD": {}` |
| `ADOSC` | Chaikin A/D Oscillator | `"ADOSC": {"fastperiod": 3, "slowperiod": 10}` |
| `OBV` | On Balance Volume | `"OBV": {}` |

