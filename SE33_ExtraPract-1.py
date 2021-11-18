netamount=0
while True:
  s=input("enter transaction:")
  transaction=s.split(" ")
  type=transaction[0]
  amount=int(transaction[1])
  if type=="D":
    netamount+=amount
  elif type=="W":
    netamount-=amount
  else:
    pass
  s=input("want to continue(Y for yes):")
  if not (s[0]=="Y" or s[0]=="Y"):
    break
print(netamount)