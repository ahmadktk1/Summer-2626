# Now all the project for the first time the functional version
accounts = {}
AccountAuth = {} # IBAN : PIN

# create user account function
def create_account(accounts = accounts,AccountAuthorization= AccountAuth):
    newUser = []
    name = input("Name: ")
    age = int(input("Age: "))
    account_type = input(r"Current \ Saving ")
    address = input("Address: ")
    branchno = int(input("Branch Number: "))
    balance = 0

    

    # when account created ask user to set ATM PIN
    
    newUser.append(name)
    newUser.append(age)
    newUser.append(account_type)
    newUser.append(address)
    newUser.append(balance)

    # IBAN format "PK10 AKML 1929 0023 1911 3842"
    while True:
        import random 
        accno = random.randint(1111111111,9999999999)
        if accno in accounts.keys():
            pass
        else:
            IBAN = "PK10"+"AKML"+str(branchno)+ "00"+str(accno)
            break
    
    # creating the account
    accounts[IBAN] = newUser
    

    # creating ATM PIN
    PIN = input("Set PIN : ")
    assert len(PIN) == 4

    
    AccountAuth[IBAN] = PIN
    print("Account Successfully Created! ")
    print(f"User Account Details \n {IBAN} {name} {age} {address} {account_type}")
    
# add balance to account function
def add_balance(accounts = accounts,Auth = AccountAuth):
    # we have to see 2 things is the accounts Number in the accountsno 
    IBAN = input("Enter IBAN: ")
    if IBAN in accounts.keys():
        while True:
            PIN = input("Enter Account PIN : ")
            if len(PIN) != 4:
                print("PIN is 4 digits ")
            elif len(PIN) == 4 and PIN == AccountAuth[IBAN]: 
                Balance = int(input("Enter Amount: "))
                accounts[IBAN][4] = Balance
                print(f"Successfully Added {Balance} to your account")
                break
            elif len(PIN) == 4 and PIN != AccountAuth[IBAN]:
                print("Incorrect PIN Enter Again")
    else:
        print("Account no found")

# now the function of checking balance
def check_balance(accounts = accounts):
    IBAN = input("Enter IBAN : ")
    if IBAN in accounts:
        print(f"Balance : {accounts[IBAN][4]}")
    else:
        print(f"Account not found")


# withdraw amount function
def withdraw_amount(accounts= accounts,Auth = AccountAuth):
    IBAN = input("Enter IBAN : ")
    if IBAN in accounts:
        PIN = input("Enter Account PIN: ")
        while True:
            if len(PIN) != 4:
                print("PIN is 4 digits")
            elif len(PIN) ==4 and PIN ==  AccountAuth[IBAN]:
                amount = int(input("Withdrawal Amount : "))
                accounts[IBAN][4] = accounts[IBAN][4] - amount
                print(f"Withdrawal successful remaining amount {accounts[IBAN][4]}")
                break
            elif len(PIN) == 4 and PIN != AccountAuth[IBAN]:
                print("Incorrect PIN")
    else:
        print(f"Account Not Found")
 
# creating main 
if __name__ == "__main__":
    
    while True:
        print("_-"* 20 ,"Welcome to AKM Banks","_-"*20)
        print("Select your choice")
        print("1. Create New Account")
        print("2. Check Balance")
        print("3. Add Balance")
        print("4. Withdraw Amount")
        print("5. Cancel")
        print("_-"* 25 ,"-_"*25)
        choice = int(input("Selection: "))
        if choice == 1:
            create_account()
        elif choice == 2:
            check_balance()
        elif choice ==3:
            add_balance()
        elif choice == 4:
            withdraw_amount()
        elif choice == 5:
            break




        
