


'''

ATM GAME   



1. print a welcome screen
2. ask for user to enter a PIN   
3. check if the PIN is correct
4. make it so ATM asks for PIN until it is correct

'''


# 1. print a welcome screen
print("WELCOME TO THE ATM!!!!\n")


# 4. make it so ATM asks for PIN until it is correct
chances = 3
while True:

  # 2. ask for user to enter a PIN
  ask_pin = input("PLEASE ENTER A PIN:\n")

  # 3. check if the PIN is correct
  if ask_pin == "1234":
    print("CORRECT!\n")
    break

  else:
    print("ERROR! INVALID PIN\n")
    chances -= 1
    print("CHANCES LEFT: {}".format(chances))
    if chances == 0:
      print("YOU HAVE REACHED THE MAXIMUM NUMBER OF ATTEMPTS.")
      print("YOU HAVE BEEN LOCKED OUT OF THE ATM!")
      break


