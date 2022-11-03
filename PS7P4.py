def employ_pay(hours,rate):
  pay = float(hours) * float(rate)
  return pay

lastname = str(input("Enter last name: "))
hours = float(input("Enter hours worked: "))
jc = str(input("Enter job code: "))
if jc == "L":
  rate = 25
elif jc == "A":
  rate = 30
elif jc == "J":
  rate = 30
else:
  print("Invalid job code")
pay = employ_pay(hours,rate)

print(lastname, "pay:", pay)
