from car import Car
from dealer_shop import DealerShop
from employee import Employee

cars = list()
cars.append(Car("Suzuki", 4500))
cars.append(Car("Toyota", 2500))
cars.append(Car("BMW", 1500))

employees = list()
employees.append(Employee("Jhon", "Doe", "Sales Manager"))

ds = DealerShop("Cars", employees, cars)

employee = employees[0]
employee.greet_customer()
employee.purpose_cars(cars)

for car in cars:
    car.ride()
    car.beep()
    car.park()

ds.info()
