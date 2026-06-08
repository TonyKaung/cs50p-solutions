import inflect
from datetime import date
from seasons import minutes_since, minutes_to_words

p = inflect.engine()


# ── minutes_since ─────────────────────────────────────────────────────────────
# pass two dates directly so tests don't depend on when they are run

def test_minutes_since_one_day():
    dob   = date(2024, 1, 1)
    today = date(2024, 1, 2)
    assert minutes_since(dob, today) == 1_440          # 1 day × 24 h × 60 min

def test_minutes_since_one_week():
    dob   = date(2024, 3, 1)
    today = date(2024, 3, 8)
    assert minutes_since(dob, today) == 10_080         # 7 days × 1 440

def test_minutes_since_one_non_leap_year():
    dob   = date(2022, 1, 1)
    today = date(2023, 1, 1)
    assert minutes_since(dob, today) == 525_600        # 365 days

def test_minutes_since_one_leap_year():
    dob   = date(2024, 1, 1)
    today = date(2025, 1, 1)
    assert minutes_since(dob, today) == 527_040        # 366 days

def test_minutes_since_same_day():
    dob   = date(2024, 6, 15)
    today = date(2024, 6, 15)
    assert minutes_since(dob, today) == 0


# ── minutes_to_words ──────────────────────────────────────────────────────────

def test_minutes_to_words_zero():
    assert minutes_to_words(0) == "Zero"

def test_minutes_to_words_one():
    assert minutes_to_words(1) == "One"

def test_minutes_to_words_small():
    # 1 440 minutes = one thousand, four hundred forty
    assert minutes_to_words(1_440) == "One thousand, four hundred forty"

def test_minutes_to_words_large():
    # 525 600 minutes = one non-leap year
    result = minutes_to_words(525_600)
    assert "five hundred" in result.lower()
    assert "twenty" in result.lower()

def test_minutes_to_words_no_and():
    expected = p.number_to_words(525_600, andword="").capitalize()
    assert minutes_to_words(525_600) == expected

def test_minutes_to_words_starts_with_capital():
    assert minutes_to_words(42)[0].isupper()