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


def printError(errorCode, additionalInfo=None):
    """
    Prints an error message to stderr and exits the program based on the provided error code.

    Args:
        errorCode (str): The error code indicating the type of error.
        additionalInfo (str, optional): Additional information related to the error.
    """
    errorMessages = {
        "httpError400": "400 Bad Request: The server could not understand the request.",
        "httpError401": "401 Unauthorized: Access is denied.",
        "httpError402": "402 Payment Required: Payment required to access the service.",
        "httpError403": "403 Forbidden: Access to the service is forbidden.",
        "httpError404": "404 Not Found: The requested resource was not found.",
        "httpError405": "405 Method Not Allowed: The method is not allowed.",
        "httpError406": "406 Not Acceptable: The requested resource is not acceptable.",
        "httpError407": "407 Proxy Authentication Required: Proxy authentication required.",
        "httpError408": "408 Request Time-out: The request timed out.",
        "httpError409": "409 Conflict: There is a conflict with the request.",
        "httpError410": "410 Gone: The resource is no longer available.",
        "httpError411": "411 Length Required: Length required for the request.",
        "httpError412": "412 Precondition Failed: Precondition failed for the request.",
        "httpError413": "413 Request Entity Too Large: The request entity is too large.",
        "httpError414": "414 Request-URI Too Large: The request-URI is too large.",
        "httpError415": "415 Unsupported Media Type: The media type is unsupported.",
        "httpError416": "416 Requested Range Not Satisfiable: The requested range is not satisfiable.",
        "httpError417": "417 Expectation Failed: Expectation failed for the request.",
        "httpError500": "500 Internal Server Error: The server encountered an error processing the request.",
        "httpError501": "501 Not Implemented: The server does not support the functionality required.",
        "httpError502": "502 Bad Gateway: The server received an invalid response.",
        "httpError503": "503 Service Unavailable: The server is currently unable to handle the request.",
        "httpError504": "504 Gateway Time-out: The gateway timed out while processing the request.",
        "httpError505": "505 HTTP Version Not Supported: The server does not support the HTTP version used in the request.",
        # Add more custom error messages here as needed
    }

    errorMessage = errorMessages.get(errorCode, f"Unknown Error: An unknown error occurred with code {errorCode}.")
    if additionalInfo:
        errorMessage += f" Additional info: {additionalInfo}"

    print(errorMessage, file=sys.stderr)
    sys.exit(1)
