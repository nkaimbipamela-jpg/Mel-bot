history = []


def add_result(value):
    history.append(value)


def get_last(n=10):
    return history[-n:]