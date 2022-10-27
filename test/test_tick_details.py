from src.tick_details import get_tick_details


def test_get_tick_details():
    assert type(get_tick_details()) == dict
