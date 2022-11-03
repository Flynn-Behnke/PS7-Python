def bat_avg(hits, bats):
  avg = int(hits)/int(bats)

  return avg

lastname = str(input("Enter player last name: "))
bats = int(input("Enter number of times at bat: "))
hits = int(input("Enter number of hits: "))
batavg = bat_avg(hits, bats)

print(lastname, "batting average:", batavg)
