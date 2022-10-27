from src.index_details import get_index_list, get_current_index_details


def test_get_index_list():
    assert type(get_index_list()) == list


def test_get_current_index_details():
    data = get_current_index_details(index_detail='NIFTY 50')
    print(data)
    assert data['change']