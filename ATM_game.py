############
# enter PIN
############
while True:
    enter_pin = input('\t###########################################\n\tWELCOME TO THIS ATM! PLEASE ENTER YOUR PIN:\n\t\t\t{PIN=1234}\n\t###########################################\n\n')

    if enter_pin == '1234':
        print('\n' * 30)
        print('PIN Accepted')
        print('\n' * 30)
        break
    else:
        print('\n' * 30)
        print('Sorry, that PIN is incorrect')
        continue


###################################################################
# define class for account, with attributes deposit and withdrawal
###################################################################
class Account():

    # define attributes
    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    # define methods
    def deposit(self, deposit_amt):
        self.balance += deposit_amt
        print('${} was deposited into your account'.format(deposit_amt))
        print('\n######################')
        print('Current balance: ${}'.format(myacct.balance))
        print('#######################\n')

    def withdrawal(self, withdrawal_amt):
        self.balance -= withdrawal_amt
        if self.balance < 0:
            print('Funds unavailable!')
            self.balance += withdrawal_amt
            print('\n######################')
            print('Current balance: ${}'.format(myacct.balance))
            print('#######################\n')
        else:
            print('${} was withdrawn from your account'.format(withdrawal_amt))
            print('\n######################')
            print('Current balance: ${}'.format(myacct.balance))
            print('#######################\n')

    def __str__(self):
        return f'Account owner: {self.owner} \nCurrent Balance: ${self.balance}'


myacct = Account('Ali G', 34)

####################
# selection screen
###################
welcome = True

while welcome == True:
    print('Welcome Back, ' + myacct.owner + '!\n')
    select_screen = input(
        "     PLEASE MAKE A SELECTION     \n\n\n\nVIEW BALANCE ---> 'B' \nMAKE DEPOSIT ---> 'D' \nWITHDRAWAL   ---> 'W'\n\n\n")
    ###############
    # view balance
    ###############
    if select_screen.lower() == 'b':
        print('\n' * 30)
        print('Account owner: ' + myacct.owner + '\n')
        print('#######################')
        print(f'Account balance: ${myacct.balance}')
        print('#######################\n')



    ################
    # make deposit
    ###############
    elif select_screen.lower() == 'd':
        print('\n' * 30)
        while True:
            try:
                print('Account owner: '+myacct.owner+'\n')
                print('#######################')
                print(f'Account balance: ${myacct.balance}')
                print('#######################\n')
                deposit_screen = int(input("HOW MUCH WOULD YOU LIKE TO DEPOSIT?\n\n\n"))
            except ValueError:
                print('\n' * 30)
                print("Invalid entry. Please enter an integer\n\n")
                continue
            else:
                print('\n' * 30)
                break
        myacct.deposit(deposit_screen)

    ##################
    # make withdrawal
    ##################
    elif select_screen.lower() == 'w':
        print('\n' * 30)
        while True:
            try:
                print('Account owner: ' + myacct.owner + '\n')
                print('#######################')
                print(f'Account balance: ${myacct.balance}')
                print('#######################\n')
                withdrawal_screen = int(input("HOW MUCH WOULD YOU LIKE TO WITHDRAWAL?\n\n\n"))
            except ValueError:
                print('\n' * 30)
                print("Invalid entry. Please enter an integer\n\n")
                continue
            else:
                print('\n' * 30)
                break
        myacct.withdrawal(withdrawal_screen)

    else:
        print('\n' * 30)
        print("Invalid entry. Please enter 'B', 'D', or 'W'")

    ###################################
    # ask to make another transaction
    ##################################
    while True:
        return_screen = input("WOULD YOU LIKE TO MAKE ANOTHER TRANSACTION? ENTER 'Yes' or 'No'\n\n\n")
        if return_screen.lower() == 'yes':
            print('\n' * 30)
            break
        elif return_screen.lower() == 'no':
            print('\n' * 30)
            print('Thank you for using this ATM. \n\nHave a nice day!')
            welcome = False
            break
        else:
            print('\n' * 30)
            print("Invalid entry. Please enter 'Yes' or 'No'")
            continue