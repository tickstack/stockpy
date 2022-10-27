from src.helper import general


def top_gainer() -> list:
    """Function is to get today's top gainer on NIFTY50

    Returns:
        list: Top gainer list
    """
    nse = general.get_nse_object()
    return nse.get_top_gainers()


def top_losers() -> list:
    """Function is to get today's top losers on NIFTY50

    Returns:
         list: Top losers list
    """
    nse = general.get_nse_object()
    return nse.get_top_losers()


# if __name__ == '__main__':
#     nse = Nse()
#     print(nse.get_top_gainers())
