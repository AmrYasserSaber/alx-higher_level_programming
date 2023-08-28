#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as err:
        result = None
        print("Exception: {}".format(err))
    finally:
        return result
