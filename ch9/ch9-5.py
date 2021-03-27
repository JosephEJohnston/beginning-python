def flatten(nested):
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError

        for sublist in nested:
            for element in flatten(sublist):
                yield element

    except TypeError:
        yield nested


def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new


