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

    user_input.strip()

def has_scheme(user_input: str):
    pass