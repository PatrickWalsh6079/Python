
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
print(my_account)


'''
1. set up a selection screen
2. allow user to either deposit or withdrawal money

'''

print("WHAT WOULD YOU LIKE TO DO?")


# selection screen to ask user what they want to do

while True:
  selection_screen = input("View balance: 'B'\nMake deposit: 'D'\nMake withdrawal: 'W'\n")

  if selection_screen == 'b':
    print("Current balance: ${}".format(my_account.balance))
    break

  elif selection_screen == 'd':
    deposit_screen = int(input("How much would you like to deposit?\n"))
    my_account.deposit(deposit_screen)
    print("New balance: $",my_account.balance)
    break

  elif selection_screen == 'w':
    withdrawal_screen = int(input("How much would you like to withdrawal?\n"))
    my_account.withdrawal(withdrawal_screen)
    print("New balance: $",my_account.balance)
    break

  else:
    print("That is not a valid selection.")



