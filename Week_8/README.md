# URL Shortener

#### Description:

This is a command-line URL shortener built in Python. It takes a long URL, validates that it's properly formatted, and generates a short, random 6-character code that maps back to the original URL. Users can then use that code to retrieve the original URL at any time during the program's run.

The project has four core functions besides `main`:

- `is_valid_url(url)` — uses a regular expression to check that a URL starts with `http://` or `https://` and contains no whitespace, returning `True` or `False`.
- `generate_short_code(length=6)` — generates a random 6-character alphanumeric code using Python's `random` and `string` modules.
- `shorten_url(long_url, urls)` — generates a unique short code (regenerating if a collision occurs), stores the mapping in a dictionary, and returns the code.
- `expand_url(short_code, urls)` — looks up a short code in the dictionary and returns the original URL, or `None` if the code doesn't exist.

`main()` ties everything together with a simple loop: the user chooses to shorten a URL, expand a code, or quit. URL-to-code mappings are stored in memory using a Python dictionary for the duration of the program.

One design decision I made early on was to keep storage simple with an in-memory dictionary rather than a database, since the goal of this version was to get the core logic working first. Validating uniqueness of short codes was an interesting problem — I used a `while` loop that keeps generating new codes until it finds one that isn't already in use, which prevents two different URLs from accidentally sharing the same short code.

The biggest challenge was understanding how Python looks up values in a dictionary by key versus how it indexes a list by position, since the short code itself is a string key rather than a numeric index. Writing the tests in `test_project.py` also helped me think more carefully about edge cases, like what should happen when someone tries to expand a code that was never created.

This project is also the starting point for a bigger goal: turning this into a real, deployed REST API using FastAPI, where users could shorten URLs through an actual web interface instead of the command line. The in-memory dictionary would eventually be replaced with a proper database like PostgreSQL.