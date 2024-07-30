import re
import sys

def checkBaseUrl(url):
    """
    Validates a base URL, ensuring it ends with a slash and does not contain a path or query string.
    If the URL is valid but does not end with a slash, a slash is appended.

    Args:
        url (str): The URL to validate.

    Returns:
        str: The validated URL, guaranteed to end with a slash.

    Exits:
        Exits the program with status 1 if the URL is not valid or contains a path/query string.
    """
    # Regular expression to validate a base URL without path or query string
    urlPattern = re.compile(
        r'^(?:http|https)://'  # http or https
        r'(?:\S+(?::\S*)?@)?'  # optional user:pass authentication
        r'(?:'  # IP address or domain
        r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})'  # IP address
        r'|'  # or
        r'(?P<domain>'  # domain
        r'(?:(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})'  # domain name
        r')'
        r')'
        r'(?::\d{2,5})?'  # optional port
        r'(?:(?:/[^\s/?#]*)*)'  # optional path
        r'(?:\?[^\s#]*)?'  # optional query string
        r'(?:#[^\s]*)?$'  # optional fragment
    )

    # Match the URL against the pattern
    match = re.match(urlPattern, url)
    if not match:
        print("Invalid URL format.", file=sys.stdout)
        sys.exit(1)

    # Ensure no path or query string is present
    if '?' in url or '#' in url:
        print("URL must not contain a query string or fragment.", file=sys.stdout)
        sys.exit(1)

    # Ensure the URL ends with a slash
    if not url.endswith('/'):
        url += '/'

    return url
