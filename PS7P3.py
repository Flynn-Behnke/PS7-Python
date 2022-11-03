def calc_mpg(mi,gal):
  mpg = float(mi)/float(gal)
  return mpg
dest = str(input("Enter destination: "))
mi = float(input("Enter miles driven: "))
gal = float(input("Enter gallons of fuel used: "))
mpg = calc_mpg(mi,gal)


print("Average fuel economy for traveling to", dest, ":", mpg)
