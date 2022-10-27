from src.helper.general import get_nse_object
from nsetools import Nse


def test_get_nse_object():
    assert type(get_nse_object()) == Nse
