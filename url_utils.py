# utils/url_utils.py

import validators
from urllib.parse import urlparse

def is_phishing_url(url):
    print("Function is_phishing_url called with:", url)
    ...

    if not validators.url(url):
        return False  # Invalid URL format

    parsed_url = urlparse(url)

    # Check for suspicious patterns in URL domain (e.g., common phishing terms)
    suspicious_keywords = ["login", "secure", "signin", "bank", "verify", "account"]
    if any(keyword in parsed_url.netloc for keyword in suspicious_keywords):
        return True

    # Check if the URL uses HTTPS (non-HTTPS could be suspicious)
    if parsed_url.scheme != 'https':
        return True  # Non-HTTPS URLs are often phishing sites

    return False
