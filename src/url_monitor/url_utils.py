def normalize_url(user_input: str) -> str:
    """It returns a normalized URL. If no scheme is provided, HTTPS is used.
    Explicit HTTP/HTTPS schemes are preserved. www. is removed. Trailing slashes are removed.
    Invalid URLs raise ValueError.

    Args:
        user_input (str): a string containing a user-provided website address

    Returns:
        (str): _description_
    """
    if type(user_input) != str:
        raise ValueError("The input must be a string.")

    user_input.replace(" ", "")
    user_input.replace("\t", "")
    user_input.replace("\n", "")

def scheme_detect(user_input: str):
    pass