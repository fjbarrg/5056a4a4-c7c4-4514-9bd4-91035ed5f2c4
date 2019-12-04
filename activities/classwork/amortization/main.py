import fire

from util import Amortization


class Main(object):

    @staticmethod
    def future_value(present_value, interest, n):
        return present_value * (1 + interest) ** n

    @staticmethod
    def annuity(amount, interest, n):
        pass

    def table(self, amount, interest, n, rows=10, save=""):
        pass

    def graph(self, amount, interest, n, save=""):
        pass


if __name__ == "__main__":
    fire.Fire(Main)
