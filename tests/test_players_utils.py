import pytest
from hoopstats import create_player_suffix

def test_create_player_suffix_valid_name():
    mock_first_name = "Lonzo"
    mock_last_name = "Ball"

    suffix = create_player_suffix(
        first_name=mock_first_name, last_name=mock_last_name, unique_id="01"
    )
    assert suffix == "b/balllo01"
    assert suffix is not None
