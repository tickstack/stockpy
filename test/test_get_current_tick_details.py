from src import get_current_tick_details


def test_get_current_tick_details():
    data = get_current_tick_details.get_quotes_details(symbol='INFY', as_json=True)
    print(data)
    assert type(data) == str
    data = get_current_tick_details.get_quotes_details(symbol='INFY', as_json=False)
    print(data)
    assert type(data) == dict
