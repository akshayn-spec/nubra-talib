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
            #"MACD": {"fastperiod": 12, "slowperiod": 26, "signalperiod": 9},
        },
    )

    #df = add_basics(df)

    print(df.tail())


if __name__ == "__main__":
    main()
