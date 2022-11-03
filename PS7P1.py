def comp_total(quant, price):
  total = float(quant) * float(price)

  if total >= 10000.00:
    total = total*0.9
  else:
    total = total

  return total

quant = float(input("Enter quantity: "))
price = float(input("Enter price of each unit: "))
total = comp_total(quant, price)

print("The total is: $" , total)
