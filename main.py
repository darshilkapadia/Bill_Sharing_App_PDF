class Bill:
    """
    Object that contains data about the bill such as
    total amount and period of bill
    """

    def __init__(self, amount, period):
        self.period = period
        self.amount = amount


class Flatmate:
    """
    Creates a flatmate person who lives in in the flat and
    pays the share of the bill
    """

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pays(self, bill):
        pass

class PdfReport:
    """
    Creates a pdf files that contains data about their names , due amount
    and period over the bills
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, fmate1, fmate2, bill):
        pass

