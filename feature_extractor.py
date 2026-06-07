from urllib.parse import urlparse
import re

def extract_features(url):
    parsed = urlparse(url)

    num_dots = url.count('.')
    url_length = len(url)
    num_dash = url.count('-')

    no_https = 0 if url.startswith("https") else 1

    ip_address = 1 if re.search(r'(\d{1,3}\.){3}\d{1,3}', url) else 0

    hostname_length = len(parsed.netloc)
    path_length = len(parsed.path)
    query_length = len(parsed.query)

    sensitive_words = [
        "login",
        "verify",
        "secure",
        "account",
        "bank",
        "update",
        "password"
    ]

    num_sensitive_words = sum(
        word in url.lower()
        for word in sensitive_words
    )

    num_numeric_chars = sum(c.isdigit() for c in url)

    return [[
        num_dots,
        url_length,
        num_dash,
        no_https,
        ip_address,
        hostname_length,
        path_length,
        query_length,
        num_sensitive_words,
        num_numeric_chars
    ]]