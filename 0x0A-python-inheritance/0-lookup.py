def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings containing the names of attributes and methods.
    """
    import types  # Import the types module here

    if hasattr(obj, '__dir__'):
        return [attr for attr in dir(obj)]
    else:
        return []
