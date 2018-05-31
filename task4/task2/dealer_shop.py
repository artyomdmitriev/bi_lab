class DealerShop:
    amount_of_visitors = 0

    def __init__(self, name, employees, cars):
        self.name = name
        self.employees = employees
        self.cars = cars

    def amount_of_employees(self):
        return len(self.employees)

    def amount_of_cars(self):
        return len(self.cars)

    def info(self):
        print("-- Shop info --")
        print("Shop name: {0}".format(self.name))
        print("Amount of employees: {0}".format(len(self.employees)))
        print("Amount of cars: {0}".format(len(self.cars)))
        print("Amount of visitors: {0}".format(DealerShop.amount_of_visitors))
