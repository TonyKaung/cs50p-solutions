import project

def test_is_valid_url():
    assert project.is_valid_url("adfdaf") == False
    assert project.is_valid_url("https://cs50.harvard.edu/python/project/") == True

def test_generate_short_code():
    code = project.generate_short_code()
    assert len(code) == 6
    assert code.isalnum()

def test_shorten_url():
    urls = {}
    code = project.shorten_url("https://www.youtube.com/", urls)
    assert code in urls
    assert urls[code] == "https://www.youtube.com/"

def test_expand_url():
    urls = {"abc123": "https://example.com"}
    assert project.expand_url("abc123", urls) == "https://example.com"
    assert project.expand_url("afdasd", urls) == None