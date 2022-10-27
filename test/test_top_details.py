from src.top_details import top_gainer, top_losers


def test_top_gainer():
    assert type(top_gainer()) == list


def test_top_losers():
    assert type(top_gainer()) == list
