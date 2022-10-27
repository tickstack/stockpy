from src.tick_validate import validate_symbol_code


def test_validate_symbol_code():
    assert validate_symbol_code(symbol='INFY')