from src.helper import general
from src import tick_validate
from typing import Union


def get_quotes_details(symbol: str, as_json: bool) -> Union[dict, str]:
    """Function is to get current quotes details of symbol
    Args:
        symbol (str): Symbol
        as_json (boo): As json or str

    Returns:
        dict: return quotes details
    """
    if tick_validate.validate_symbol_code(symbol=symbol):
        nse = general.get_nse_object()
        return nse.get_quote(code=symbol, as_json=as_json)
    else:
        return "Symbol quotes is not valid"
