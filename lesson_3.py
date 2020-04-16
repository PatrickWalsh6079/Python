

# IF/ELIF/ELSE    

x = 0

if x < 0:
  print(True)
else:
  print(False)


if x < 5:
  print("Less than 5!")
  if x == 0:
    print("X is zero!")
elif x >= 5:
  print("Greater than 5!")

if x < 0:
  print("X is negative")
elif x > 0:
  print("X is positive")
else:
  print("X is zero")


# FOR LOOPS  
names = ["Frank","Billy","Tommy","Joey"]

for i in names:
  print(i)

for i in range(0,10):
  print(i)

for i in names:
  if i[-1] == 'y':
    print(i,"ends in 'y'")
  else:
    print(i,"does not end in 'y'")

# WHILE LOOPS  

x = 0

while x < 10:
  print(x)
  x += 1

while True:
  # provides infinite loop until you break out of loop   
  break



# break
x = 0

while x < 50:
  print(x)
  x += 1
  if x == 10:
    break

names = ["Frank","Billy","Tommy","Joey"]

for i in names:
  print(i)
  if i[0] == "T":
    break

# continue  

for i in range(0,20):
  if i == 10:
    continue
  print(i)





