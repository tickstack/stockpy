from src import historical_prices
from datetime import date
import pytest


def test_get_historical_prices():
    """Function is to test historical prices
    Returns:
    """
    data = historical_prices.get_historical_prices(symbol='INFY', start_date=date(year=2015, month=1, day=1),
                                                   end_date=date(year=2022, month=11, day=1))
    assert len(data) > 1500
