
'''
ATM GAME   

welcome screen

1. display a welcome screen
2. ask for a PIN  
3. check the value of the PIN       

'''

# 1. display a welcome screen
# 2. ask for a PIN 
while True: 
  welcome = input("WELCOME TO THE ATM\nPLEASE ENTER YOUR PIN:\n\n\n")

  if welcome == "1234":
    print("PIN ACCEPTED")
    break
  else:
    print("INCORRECT PIN.PLEASE TRY AGAIN")



'''
create a class with two attriutes: owner, and balance

give it two methods: deposit and withdrawal

'''

# create BankAccount class  

class BankAccount():

  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance

  # make deposit
  def deposit(self, deposit_amount):
    print("Amount deposited: ${}".format(deposit_amount))
    self.balance += deposit_amount
    return self.balance

  # make withdrawal
  def withdrawal(self, withdrawal_amount):
    print("Amount withdrawn: ${}".format(withdrawal_amount))
    self.balance -= withdrawal_amount
    return self.balance

  # display message with __str__ methods
  def __str__(self):
    return "Account owner: {}\nCurrent balance: ${}\n".format(self.owner,self.balance)



my_account = BankAccount("Kai", 1000)
# print(my_account)


'''
1. set up a selection screen
2. allow user to view balance, deposit or withdrawal money

'''

print("WHAT WOULD YOU LIKE TO DO?")

while True:
  selection_screen = input("VIEW BALANCE: 'B', DEPOSIT: 'D', WITHDRAWAL: 'W'\n")

  if selection_screen == 'b':
    print("CURRENT BALANCE: ${}".format(my_account.balance))
  elif selection_screen == 'd':
    deposit_screen = int(input("HOW MUCH WOULD YOU LIKE TO DEPOSIT?\n"))
    my_account.deposit(deposit_screen)
    # print("DEPOSIT AMOUNT: ${}".format(deposit_screen))
    print("NEW BALANCE: ${}".format(my_account.balance))
  elif selection_screen == 'w':
    withdrawal_screen = int(input("HOW MUCH WOULD YOU LIKE TO WITHDRAWAL?\n"))
    if withdrawal_screen > my_account.balance:
      print("FUNDS UNAVAILABLE\n")
      continue
    my_account.withdrawal(withdrawal_screen)
    # print("WITHDRAWAL AMOUNT: ${}".format(withdrawal_screen))
    print("NEW BALANCE: ${}".format(my_account.balance))
  else:
    print("THAT IS NOT A VALID SECTION\n")
    continue

  '''
  1. ask if user wants to make another selection   
  2. end game if answer is no, otherwise return to the selection_screen

  '''
  end_game = False 
  
  question_screen = input("WOULD YOU LIKE TO MAKE ANOTHER TRANSACTION?\nYES: 'Y'\nNo: 'N'\n")

  if question_screen == 'y':
    print("yes")
  elif question_screen == 'n':
    
    break
  else:
    print("invalid choice")

print("THANK YOU FOR USING THE ATM, HAVE A NICE DAY!")


