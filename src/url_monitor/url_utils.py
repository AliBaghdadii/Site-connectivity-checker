from urllib.parse import urlsplit, urlunsplit

def normalize_url(user_input: str) -> str:
    """It returns a normalized URL. If no scheme is provided, HTTPS is used.
    Explicit HTTP/HTTPS schemes are preserved. www. is removed. Trailing slashes are removed.
    Invalid URLs raise ValueError.

    Args:
        user_input (str): a string containing a user-provided website address

    Returns:
        (str): _description_
    """
    if not isinstance(user_input, str):
        raise ValueError("The input must be a string.")

    user_input.strip() # For removing whitespaces, newlines, tabs and etc.

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

    if not host:
        raise ValueError("URL has no host after removing www.")

    # Preserve the root URL as "/" while removing other trailing slashes.
    path = parts.path.rstrip("/") or "/"

    # urlsplit.hostname omits brackets, so restore them for IPv6 addresses.
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