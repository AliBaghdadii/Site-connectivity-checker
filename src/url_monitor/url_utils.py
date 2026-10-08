from urllib.parse import urlsplit, urlunsplit
import ipaddress


def normalize_url(user_input: str) -> str:
    """It returns a normalized URL. If no scheme is provided, HTTPS is used.
    Explicit HTTP/HTTPS schemes are preserved. www. is removed. Trailing slashes are removed.
    Invalid URLs raise ValueError.

    Args:
        user_input (str): a string containing a user-provided website address

    Returns:
        The normalized url.
    """
    if not isinstance(user_input, str):
        raise TypeError("The input must be a string.")

    user_input = user_input.strip() # For removing whitespaces, newlines, tabs and etc.
    if not user_input:
        raise ValueError("URL must be a non-empty string")

    if "://" not in user_input:
        user_input = "https://" + user_input

    try:
        parts = urlsplit(user_input)
    except ValueError as exc:
        raise ValueError("Invalid URL") from exc

    scheme = parts.scheme.lower()
    if scheme not in {"http", "https"}:
        raise ValueError("Only http and https are supported")

    try:
        host = parts.hostname
        port = parts.port
    except ValueError as exc:
        raise ValueError("Invalid URL") from exc

    if not host:
        raise ValueError("URL has no host")

    host = host.lower()
    if host.startswith("www."):
        host = host[4:]

    try:
        ipaddress.ip_address(host)
    except ValueError:
        # Not an IP address: require a dotted hostname with valid labels.
        labels = host.split(".")
        if len(labels) < 2 or any(
            not label
            or label.startswith("-")
            or label.endswith("-")
            or not label.replace("-", "").isalnum()
            for label in labels
        ):
            raise ValueError("Invalid hostname")

    if not host:
        raise ValueError("URL has no host after removing www.")

    path = parts.path.rstrip("/")

    # urlsplit.hostname omits brackets around IPv6 addresses.
    if ":" in host and not host.startswith("["):
        host = f"[{host}]"

    netloc = host if port is None else f"{host}:{port}"

    return urlunsplit((
        scheme,
        netloc,
        path,
        parts.query,
        parts.fragment
    ))