from settings import DEFAULT_ROUND_VALUE


def read_file(filename, mode='r'):
    with open(filename, mode) as file:
        return file.read()


def check_if_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def round_data(df, round_value=DEFAULT_ROUND_VALUE):
    return df.round(round_value)
