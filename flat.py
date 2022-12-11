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

    #  now how to get the other flatmates days: either by manually adding the flatmate2 amount in or call flatmate 2
    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay