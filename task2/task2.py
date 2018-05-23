dollars = int(input('Enter amount of dollars: '))
cents = int(input('Enter amount of cents: '))
quantity = int(input('Enter quantity: '))

total_price = (dollars + cents / 100) * quantity
print("Total price is {0} dollars {1} cents."
      .format(int(total_price), int((total_price % 1) * 100)))
