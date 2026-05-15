from data import get_last


def moving_average(values):
    if len(values) == 0:
        return 0
    return sum(values) / len(values)


class DoubleCashStrategy:
    def __init__(self, threshold=2.0):
        self.threshold = threshold

    def signal(self):
        last_values = get_last(5)

        if len(last_values) < 5:
            return "WAIT"

        avg = moving_average(last_values)

        if avg > self.threshold:
            return "PLAY"

        return "WAIT"