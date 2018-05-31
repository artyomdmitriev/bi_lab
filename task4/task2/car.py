import time


class Car(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def ride(self):
        print("{0} wroom-wroom".format(self.name))

    def beep(self):
        print("{0} beep-beep".format(self.name))

    def park(self):
        print("{0} parking...".format(self.name))
        time.sleep(3)
        print("{0} Parked".format(self.name))
