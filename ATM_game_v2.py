import os

# welcome message, initialize variables
print("Welcome to the ATM!\n")
chances = 3
welcome = True
username_exists = False
logged_in = False
locked_out = False

# main menu screen
while True:
  if username_exists == False:
    account_login = input("CREATE A NEW ACCOUNT: 'create'\nLOGIN TO AN EXISTING ACCOUNT: 'login'\nCANCEL: 'cancel'\n\n")

    # to login to existing account
    if account_login == "login":
      pass # for logging it to existing account

    # to create new account
    elif account_login == "create":
      print ("CREATE A NEW ACCOUNT:\n\n")
      
      # user picks a username and PIN
      username = input("PLEASE CHOOSE A USERNAME:\n\n")
      pin = input("PLEASE CHOOSE A PIN:\n\n")
    
      # checks to see if account already exists
      if os.path.exists("account_{}.txt".format(username)):
        os.remove("account_{}.txt".format(username))

      # creates file for username and PIN
      f = open("account_{}.txt".format(username), "x")

      # adds username and PIN to file
      f = open("account_{}.txt".format(username), "w")
      f.write(username)
      f.write("\n")
      f.write(pin)
      f.close()

      # reads out file contents (comment out later)
      f = open("account_{}.txt".format(username), "r")
      print (f.read())
      f.close()

      print("THANK YOU FOR CREATING AN ACCOUNT\n")
      print("PLEASE LOGIN TO CONTINUE\n")
    elif account_login == 'cancel':
      welcome = False
      break
    else:
      print("INVALID ENTRY! EITHER LOGIN OR CREATE A NEW ACCOUNT\n\n")
      continue

    # ask to login
    ask_username = input("TO LOGIN, PLEASE ENTER YOUR USERNAME:\n")
    # check if username exists
    if os.path.exists("account_{}.txt".format(ask_username)):

      # if username exists, ask for PIN
      while True:
        ask_pin = input("NOW ENTER YOUR PIN:\n")
        username_exists = True

        # check PIN inside account file
        f = open("account_{}.txt".format(ask_username), "r")
        lines = f.readlines()
        # f.close()
        # see if PIN is correct
        if ask_pin == str(lines[1]):
          # print("CORRECT PIN")
          logged_in = True
          break
        else:
          # if wrong PIN is entered
          chances -= 1
          if chances == 0:
            # if you run out of chances
            print("INCORRECT PIN AGAIN! USER LOCKED OUT OF ACCOUNT")
            welcome = False
            locked_out = True
            break
          print("INCORRECT PIN")
          print("AVAILABLE ATTEMPTS: {}".format(chances))
      # if you get locked out, game ends
      if locked_out == True:
        break
      # once logged in, it takes you to user screen
      if logged_in == True:
        break
    # if account doesn't exist
    else:
      print("ERROR! NO ACCOUNT FOR {} EXISTS\n".format(ask_username))




# BankAccount class
class BankAccount():

  # set attributes
  def __init__(self, c_user, c_pin, c_balance):
    self.c_user = c_user
    self.c_pin = c_pin
    self.c_balance = c_balance

  # to deposit
  def deposit(self, deposit_amount):
    self.c_balance += deposit_amount
    print("CURRENT BALANCE: ${}".format(self.c_balance))
  
  # to withdrawal
  def withdrawal(self, widthdraw_amount):
    self.c_balance -= widthdraw_amount
    print("CURRENT BALANCE: ${}".format(self.c_balance))
  
  # display message from class object
  def __str__(self):
    return "ACCOUNT OWNER: {}\nBALANCE: ${}\n".format(self.c_user, self.c_balance)

if welcome == True:
  # retrieve username and PIN from file
  f = open("account_{}.txt".format(ask_username), "r")
  lines = f.readlines()
  file_user = lines[0].strip()
  file_pin = lines[1].strip()

  # set class object properties according to the account file
  my_account = BankAccount(file_user, file_pin, 100)

# print(my_account)

  # main user screen
  print('WELCOME BACK, ' + my_account.c_user + '!\n')

# ask to make a choice for view balance, make deposit, or make withdrawal
while welcome == True:
    print("\tPLEASE MAKE A SELECTION\n\n")
    select_screen = input("VIEW BALANCE: 'b'\nMAKE DEPOSIT: 'd'\nWITHDRAWAL: 'w'\n")

    # view balance
    if select_screen.lower() == 'b':
        print('ACCOUNT OWNER: ' + my_account.c_user)
        print(f'CURRENT BALANCE: ${my_account.c_balance}\n')

    # make deposit
    elif select_screen.lower() == 'd':
        while True:
            try:
                print('ACCOUNT OWNER: '+my_account.c_user)
                print(f'CURRENT BALANCE: ${my_account.c_balance}\n')
                deposit_screen = int(input("HOW MUCH WOULD YOU LIKE TO DEPOSIT?\n"))
            except ValueError:
                print("INVALID ENTRY. PLEASE ENTER A NUMERIC VALUE\n")
                continue
            else:
                break
        print(f"AMOUNT DEPOSITED: ${deposit_screen}\n")
        my_account.deposit(deposit_screen)


    # make withdrawal
    elif select_screen.lower() == 'w':
        while True:
            try:
                print('ACCOUNT OWNER: ' + my_account.c_user)
                print(f'CURRENT BALANCE: ${my_account.c_balance}\n')
                withdrawal_screen = int(input("HOW MUCH WOULD YOU LIKE TO WITHDRAWAL?\n\n\n"))
            except ValueError:
                print("INVALID ENTRY. PLEASE ENTER A NUMERIC VALUE\n")
                continue
            else:
                break
        if withdrawal_screen > my_account.c_balance:
          print("FUNDS UNAVAILABLE!\n")
          continue
        else:
          print(f"AMOUNT WITHDRAWN: ${withdrawal_screen}\n")
          my_account.withdrawal(withdrawal_screen)

    else:
        print("INVALID ENTRY. PLEASE ENTER 'b', 'd', OR 'w'")

    # ask to make another transaction
    while True:
        return_screen = input("WOULD YOU LIKE TO MAKE ANOTHER TRANSACTION? ENTER 'yes' or 'no'\n\n")
        if return_screen.lower() == 'yes':
            break
        elif return_screen.lower() == 'no':
            welcome = False
            break
        else:
            print("INVALID ENTRY. PLEASE ENTER 'yes' OR 'no'")
            continue
print('THANK YOU FOR USING THIS ATM. \n\nHAVE A NICE DAY!')

