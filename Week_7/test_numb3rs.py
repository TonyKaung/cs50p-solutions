from numb3rs import validate

def test_range():
    assert validate("255.67.8.1") == True
    assert validate("265.6.8.7") == False