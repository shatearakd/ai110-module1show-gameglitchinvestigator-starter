import pytest

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_winning_guess():
    assert check_guess(50, 50) == ("Win", "🎉 Correct!")

#FIX - Refactored logic into test_game_logic to check hinting system.
@pytest.mark.parametrize(
    ("guess", "secret", "expected"),
    [
        (60, 50, ("Too High", "📈 Go LOWER!")),
        (40, 50, ("Too Low", "📉 Go Higher!")),
        (10, 2, ("Too High", "📈 Go LOWER!")),
        (2, 10, ("Too Low", "📉 Go Higher!")),
    ],
)
def test_guess_feedback_and_hint_direction(guess, secret, expected):
    assert check_guess(guess, secret) == expected


def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("42", (True, 42, None)),
        ("42.9", (True, 42, None)),
        ("", (False, None, "Enter a guess.")),
        ("not a number", (False, None, "That is not a number.")),
    ],
)
def test_parse_guess_value(raw, expected):
    assert parse_guess(raw) == expected


def test_update_score():
    assert update_score(100, "Win", 1) == 100
    assert update_score(95, "Win", 2) == 95
    assert update_score(100, "Too High", 1) == 95
    assert update_score(95, "Too Low", 2) == 90
    assert update_score(100, "Tie", 1) == 100
