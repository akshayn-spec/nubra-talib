from __future__ import annotations

from typing import Any, Optional

import talib

try:
    from talib import abstract as _abstract
except Exception:
    _abstract = None


def add_talib(df, funcs: Optional[Any] = None, **kwargs):
    """Add TA-Lib indicators dynamically to an OHLCV dataframe.

    funcs can be:
    - list of function names: ["RSI", "EMA"]
    - dict mapping function name -> kwargs for that function
    kwargs are defaults applied to all functions unless overridden in the dict.
    """

    out = df.copy()
    if not funcs:
        return out

    if isinstance(funcs, dict):
        func_map = funcs
    else:
        func_map = {name: {} for name in funcs}

    for name, fkwargs in func_map.items():
        if _abstract is None:
            raise AttributeError(
                "TA-Lib abstract API is not available. "
                "This usually means the wrong package is installed. "
                "Uninstall `talib` and install `ta-lib`."
            )
        f = _abstract.Function(name)
        merged_kwargs = dict(kwargs)
        merged_kwargs.update(fkwargs or {})

        result = f(out, **merged_kwargs)

        if hasattr(result, "columns"):
            for col in result.columns:
                out[f"{name.lower()}_{str(col).lower()}"] = result[col]
        elif hasattr(result, "name"):
            out[name.lower()] = result
        else:
            for i, series in enumerate(result):
                out[f"{name.lower()}_{i}"] = series

    return out


def add_basics(df):
    """Add basic moving averages to an OHLCV dataframe."""

    out = df.copy()
    out["ma_6"] = talib.SMA(out["close"], timeperiod=6)
    out["ma_30"] = talib.SMA(out["close"], timeperiod=30)
    return out
