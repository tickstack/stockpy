from src.helper import general


def get_tick_details() -> dict:
    """Function is to get tick detail list

    Returns:
        list: return stock code details

    """
    nse = general.get_nse_object()
    return nse.get_stock_codes()
