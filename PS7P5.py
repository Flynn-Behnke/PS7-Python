def tuitowed(credit, cost):
  tuition = int(credit)*float(cost)
  return tuition
lastname = str(input("Enter student last name: "))
credit = int(input("Enter credit hours taken: "))
code = str(input("Enter district code I or O: "))
if code == "I":
  cost = 250.00
elif code == "O":
  cost = 550.00
else:
  print("Invalid district code")
tuit = tuitowed(credit, cost)
print(lastname, "tuition owed:", tuit)
