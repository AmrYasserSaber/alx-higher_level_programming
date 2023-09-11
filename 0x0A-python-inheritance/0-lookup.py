def list_attributes_and_methods(obj):
    """
    List available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings containing the names of attributes and methods.
    """
    if hasattr(obj, '__dir__'):
        return [attr for attr in dir(obj) if isinstance(getattr(obj, attr), (type, types.FunctionType))]
    else:
        return []
