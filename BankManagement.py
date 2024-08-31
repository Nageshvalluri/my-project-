
class Account:
    def __init__(self):
        self.accNo = 0
        self.name = ""
        self.deposit = 0
        self.type = ""
        self.pin = 0

    def CreateAccount(self):
        while True:
            self.accNo = input("  Enter the account number (min 6 digits): ")
            if len(self.accNo) == 6 and self.accNo.isdigit():
                self.accNo = int(self.accNo)
                break
            else:
                print(" Invalid account number Please enter min 6 digits.")

        self.name = input(" Enter the account holder name: ")

        while True:
            self.pin = input(" Enter the 4-digit pin: ")
            if len(self.pin) == 4 and self.pin.isdigit():
                self.pin = int(self.pin)
                break
            else:
                print("Invalid PIN. Please enter 4 digits.")
                
        while True:
            self.type = input("Enter the type of account [C/S]: ").upper()
            if self.type in ['C', 'S']:
                break
            else:
                print("Invalid account type. Please enter 'C' for Current or 'S' for Savings.")

        while True:
            self.deposit = int(input("Enter the initial amount (>=500 for Savings and >=1000 for Current): "))
            if (self.type == 'S' and self.deposit >= 500) or (self.type == 'C' and self.deposit >= 1000):
                break
            else:
                print(" Invalid deposit Minimum requirements do not match ")

        print(" New Account Created Successfully....!")
        print(f"Note: Please remember your account number: {self.accNo}")

    def ShowAccount(self):
        print(f"Account Number: {self.accNo}")
        print(f"Account Holder Name: {self.name}")
        print(f"Account PIN: {self.pin}")
        print(f"Type of Account: {self.type}")
        print(f"Balance: {self.deposit}")

    def updateAccount(self):
        self.name = input(" update Account Holder Name: ")
        self.type = input(" update Type of Account [C/S]: ").upper()
        self.deposit = int(input(" update Balance: "))

    def depositAmount(self, amount):
        self.deposit += amount

    def withdrawAmount(self, amount):
        if amount <= self.deposit:
            self.deposit -= amount
        else:
            print(" Insufficient balance ")

    def report(self):
        print(f"{self.accNo}  {self.name}  {self.type}  {self.deposit}")

    def getAccountNo(self):
        return self.accNo

    def getAccountHolderName(self):
        return self.name

    def getAccountType(self):
        return self.type

    def getDeposit(self):
        return self.deposit


def intro():
    print("*******************************************")
    print("---- Welcome To Union Bank of India--------")
    print("*******************************************")
    input("--------  Press Enter to continue ---------")
    print()


def writeAccount(accounts):
    account = Account()
    account.CreateAccount()
    accounts.append(account)


def displayAll(accounts):
    if accounts:
        for account in accounts:
            account.report()
    else:
        print(" No records to display ")


def displaySp(accounts, num):
    found = False
    for account in accounts:
        if account.accNo == num:
            print(f"Your account balance is: {account.getDeposit()}")
            found = True
            break
    if not found:
        print("Error: Account number is wrong. Please try again.")


def depositAndWithdraw(accounts, num, option):
    account_found = False
    for account in accounts:
        if account.accNo == num:
            account_found = True
            if option == 1:
                amount = int(input("Enter the amount to deposit: "))
                account.depositAmount(amount)
                print("Amount deposited successfully!")
            elif option == 2:
                amount = int(input("Enter the amount to withdraw: "))
                account.withdrawAmount(amount)
                print("Amount withdrawn successfully!")
            break
    if not account_found:
        print("Error: Account number is wrong. Please try again.")


def deleteAccount(accounts, num):
    initial_length = len(accounts)
    accounts[:] = [account for account in accounts if account.accNo != num]
    if len(accounts) == initial_length:
        print("Error: Account number is wrong. Please try again.")
    else:
        print("Account deleted successfully!")


def updateAccount(accounts, num):
    account_found = False
    for account in accounts:
        if account.accNo == num:
            account_found = True
            account.updateAccount()
            break
    if not account_found:
        print("Error: Account number is wrong. Please try again.")


# Start of the program
accounts = []  # In-memory storage of accounts
intro()
while True:

    print("^^^^^^^^^  ---MAIN MENU----   ^^^^^^^")
    print()
    print("1.<--------- NEW ACCOUNT------------>")
    print("2.<--------- DEPOSIT AMOUNT--------->")
    print("3.<--------- WITHDRAW AMOUNT-------->")
    print("4.<--------- BALANCE ENQUIRY-------->")
    print("5.<-----ALL ACCOUNT HOLDER LIST----->")
    print("6.<--------- CLOSE AN ACCOUNT------->")
    print("7.<--------- MODIFY AN ACCOUNT------>")
    print("8.<------------- EXIT--------------->")
    print()
    print("******Select Your Option (1-8):******")

    ch = input()

    if ch.isdigit() and 1 <= int(ch) <= 8:
        ch = int(ch)
        if ch == 1:
            writeAccount(accounts)
        elif ch == 2:
            num = int(input(" Enter The account number: "))
            depositAndWithdraw(accounts, num, 1)
        elif ch == 3:
            num = int(input(" Enter The account number: "))
            depositAndWithdraw(accounts, num, 2)
        elif ch == 4:
            num = int(input(" Enter The account number: "))
            displaySp(accounts, num)
        elif ch == 5:
            displayAll(accounts)
        elif ch == 6:
            num = int(input(" Enter The account number: "))
            deleteAccount(accounts, num)
        elif ch == 7:
            num = int(input(" Enter The account number: "))
            modifyAccount(accounts, num)
        elif ch == 8:
            print(" Thanks for using the bank management system ")
            break
    else:
        print("Invalid choice. Please select a valid option (1 to 8).")
