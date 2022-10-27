from src.helper import general


def validate_symbol_code(symbol: str) -> bool:
    """Function is to validate the symbol code is valid or not

    Args:
        symbol (str): symbol

    Returns:
        bool: True is symbol is valid else False
    """
    nse = general.get_nse_object()
    return nse.is_valid_code(symbol)
