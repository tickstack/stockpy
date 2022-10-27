from nsepy import get_history
from datetime import date
from pandas import DataFrame


def get_historical_prices(symbol: str, start_date: date, end_date: date) -> DataFrame:
    """Function is to get historical prices of symbol from start to end date
    Args:
        symbol (str): Symbol or tick
        start_date (date): start date
        end_date (date): end date

    Returns:
        DataFrame: Return dataframe
    """
    return get_history(symbol=symbol, start=start_date, end=end_date)
