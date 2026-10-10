import pytest
from src.url_monitor.url_utils import normalize_url


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("google.com", "https://google.com"),
        ("www.google.com", "https://google.com"),
        ("https://google.com", "https://google.com"),
        ("http://google.com", "http://google.com"),
        ("https://google.com/", "https://google.com"),
        ("   google.com   ", "https://google.com"),
        ("google.com/path", "https://google.com/path"),
        ("http://google.com/path/", "http://google.com/path"),
        ("HTTPS://WWW.GOOGLE.COM", "https://google.com"),
        ("google.com:8080/path", "https://google.com:8080/path"),
        ("google.com/search?q=python#results",
         "https://google.com/search?q=python#results"),
        ("https://[2001:db8::1]:8080/path/",
         "https://[2001:db8::1]:8080/path"),
    ],
)
def test_normalize_url_returns_expected_url(raw, expected):
    assert normalize_url(raw) == expected


@pytest.mark.parametrize("raw", ["", "   ", "\n\t"])
def test_normalize_url_rejects_empty_input(raw):
    with pytest.raises(ValueError):
        normalize_url(raw)


@pytest.mark.parametrize(
    "raw",
    [
        "hello",
        "https://",
        "ftp://google.com",
        "https://google.com:invalid",
    ],
)
def test_normalize_url_rejects_invalid_url(raw):
    with pytest.raises(ValueError):
        normalize_url(raw)


@pytest.mark.parametrize("raw", [None, 123, [], {}])
def test_normalize_url_rejects_non_string_input(raw):
    with pytest.raises(TypeError):
        normalize_url(raw)
