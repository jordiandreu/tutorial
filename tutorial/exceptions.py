
def run_assertion():
    x = -5

    try:
        assert x >= 0, 'x is not positive'
    except AssertionError as e:
        print(e)
        print('caught assertion error!')
    else:
        print('Everything went fine')
    finally:
        print('This is always executed')


class ValueTooHighError(Exception):
    pass


def run_my_error_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')



