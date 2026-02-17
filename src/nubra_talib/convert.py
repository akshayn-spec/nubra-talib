from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional

import pandas as pd


def _get_attr(obj: Any, name: str, default: Any = None) -> Any:
    if hasattr(obj, name):
        return getattr(obj, name)
    if isinstance(obj, dict):
        return obj.get(name, default)
    return default


def _points_to_map(points: Optional[Iterable[Any]]) -> Dict[int, Any]:
    if not points:
        return {}
    out: Dict[int, Any] = {}
    for p in points:
        ts = _get_attr(p, "timestamp")
        val = _get_attr(p, "value")
        if ts is None:
            continue
        out[int(ts)] = val
    return out


def to_ohlcv_df(
    result: Any,
    symbol: str,
    tz: str = "Asia/Kolkata",
    paise_to_rupee: bool = True,
    interval: str = "1d",
) -> pd.DataFrame:
    """Convert Nubra historical data response to an OHLCV dataframe for one symbol."""

    rows: List[Dict[str, Any]] = []

    result_list = _get_attr(result, "result") or []
    for data in result_list:
        values = _get_attr(data, "values") or []
        for stock_data in values:
            stock_chart = None
            if isinstance(stock_data, dict):
                stock_chart = stock_data.get(symbol)
            if stock_chart is None:
                continue

            open_s = _points_to_map(_get_attr(stock_chart, "open"))
            high_s = _points_to_map(_get_attr(stock_chart, "high"))
            low_s = _points_to_map(_get_attr(stock_chart, "low"))
            close_s = _points_to_map(_get_attr(stock_chart, "close"))
            vol_s = _points_to_map(_get_attr(stock_chart, "cumulative_volume"))

            all_ts = set(open_s) | set(high_s) | set(low_s) | set(close_s) | set(vol_s)
            for ts in sorted(all_ts):
                rows.append({
                    "timestamp": ts,
                    "open": open_s.get(ts),
                    "high": high_s.get(ts),
                    "low": low_s.get(ts),
                    "close": close_s.get(ts),
                    "volume": vol_s.get(ts),
                })

    df = pd.DataFrame(rows, columns=["timestamp", "open", "high", "low", "close", "volume"])
    if df.empty:
        return df

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ns", utc=True, errors="coerce")
    if tz:
        df["timestamp"] = df["timestamp"].dt.tz_convert(tz)

    if paise_to_rupee:
        for col in ("open", "high", "low", "close"):
            df[col] = (df[col].astype(float) / 100.0).round(2)

    df = df.sort_values("timestamp").reset_index(drop=True)

    if interval.lower() != "1d":
        df["volume"] = df["volume"].astype(float).diff()

    return df


def to_ist(df: pd.DataFrame, column: str = "timestamp") -> pd.DataFrame:
    """Return a copy with the timestamp column converted to IST."""
    out = df.copy()
    if column in out.columns:
        out[column] = pd.to_datetime(out[column], utc=True, errors="coerce").dt.tz_convert(
            "Asia/Kolkata"
        )
    return out
