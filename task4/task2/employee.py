from dealer_shop import DealerShop


class Employee(object):
    def __init__(self, first_name, last_name, position):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position

    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def greet_customer(self):
        DealerShop.amount_of_visitors += 1
        print("Hello! My name is {0}. How can I help you?"
              .format(self.full_name()))

    @staticmethod
    def purpose_cars(cars):
        print("Here are the cars I can purpose you:")
        for i in cars:
            print("{0}: ${1}".format(i.name, i.price))
