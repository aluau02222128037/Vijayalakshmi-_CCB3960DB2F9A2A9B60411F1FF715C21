# leap year
# year % 4 == 0
def isleapyear(year):
 if (year % 4 == 0):
  return True
 else:
  return False
 
year=int(input("enter the year:"))
if(isleapyear(year)):
  print("{} isleap year".format(year)) 
else:
 print("{} is not leap year".format(year))