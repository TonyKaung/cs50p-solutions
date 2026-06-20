from um import count

def test_search_in_word():
    assert count("Yummy") == 0
    assert count("um, hello, um...") == 2

def test_case_sensitivity():
    assert count("UM, um, um um") == 4