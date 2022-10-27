from src.helper import general


def get_index_list() -> list:
    """Function is to get index list

    Returns:
        list: index list
    """
    nse = general.get_nse_object()
    return nse.get_index_list()


def get_current_index_details(index_detail: str) -> dict:
    """Function is to get current index details

    Args:
        index_detail (str): Index detail

    Returns:
        dict:  current index detail
    """
    nse = general.get_nse_object()
    return nse.get_index_quote(index_detail)
