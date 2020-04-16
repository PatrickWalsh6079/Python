

'''
ATM GAME

1. welcome screen that prompts user for PIN  
2. take the PIN and decide whether it is correct
3. if it is correct, then display a main menu screen
4. enable ATM to ask the user repeatedly until PIN is correct

'''

print("\t\tWELCOME TO THE ATM. WOULD YOU LIKE SOME CASH???\n\n")

while True:

  ask_pin = input("PLEASE ENTER YOUR PIN:\n\n")
  if ask_pin == "444":
    print("CORRECT!")
    break
  else:
    print("WRONG! PLEASE TRY AGAIN!!!!")


'''
ATM GAME   

5. create a class called BankAccount()
6. give this class two attributes: owner and balance
7. give this class two methods: deposit and withdrawal

'''

class BankAccount():

  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance

  def deposit(self, deposit_amount):
    self.balance += deposit_amount
    print(self.balance)

  def withdrawal(self, withdrawal_amount):
    self.balance -= withdrawal_amount
    print(self.balance)

  # __str__ method to display message
  def __str__(self):
    return f"Account owner: {self.owner}\nBalance: ${self.balance}\n"

my_account = BankAccount("Delaney", 1000)

# print(my_account.owner)
# print(my_account.balance)
print(my_account)



