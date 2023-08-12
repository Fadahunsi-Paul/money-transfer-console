#Building Default Portal
import random



amount_db = [] 
user_files = []

select_opt = [

    {"option":"Transfer Money"},
    {"option":"Balance"}, 
    {"option":"Airtime & Bundles"},
    {"option":"My Wallet"},
    {"option":"Deposit"}
]

#Query functions
def create_user(pin,phone_no):
    for files in user_files:
        if phone_no == files["phone_no"]:
            return None

    new_user = {"pin":pin, "phone_no":phone_no}
    user_files.append(new_user)
    return new_user


def input_pin(pin):
    for files in user_files:
        if files['pin'] == pin:
            return files
    return None

# create login queries
def user_login(pin,phone_no):
    for files in user_files:
        if files["pin"] == pin and files["phone_no"] == phone_no:
            return files
        return False
    
#Transfering money Command

def transfer_money():
    if not amount_db:
        print('Your Balance is Low')
        files()
 
        print("The Recipient Type ")
        print("1. Momo User")
        print("2. Non-Momo User")

        insert = input(": ")

        if insert == "1":
            first_num = int(input("Enter Recipient Mobile number: "))
            sec_num = int(input("Confirm Recipient Number: "))
            reference = input('Enter Reference: ')
            
            if first_num != sec_num: 
                print("Numbers not Match")
                return

            # checking for sufficiency of wallet
            amt = int(input("Enter Amount: "))    
            if amt > amount_db[0]:
                print("Your Balance is low You cannot make the Transfer")
                return

             # Update the amount_db list with the new balance
            bal_amt = amount_db[0] - amt   
            amount_db[0] = bal_amt 

            print(f'Transfer to {sec_num} for {amt}GH with Reference: {reference}. Fee is GHS 0.00, Tax amount is 0.00. Total Amount is GHS -------# for next')
            next = input(': ')

            if next == "#":
                pin = int(input(f'{amt}. Enter MM PIN: '))
                user = input_pin(pin)

                if not user:
                    print("Invalid Pin")
                    return

                print(f'Payment made for GHS {amt} to {sec_num}. Available Balance is {bal_amt}GHS with Reference:{reference}')
                files()
        else:
            print("Invalid Option")
            

#Balance Check
def balance():
    print("==========================")
    print('Check Balance Fee Charged if 0.00. Enter Pin')
    pin = int(input('Enter Pin: '))
    user = input_pin(pin)

    if not user:
        print('Invalid Pin')
        return

    if not amount_db:   
        print('Your Balance is 0.00gh')
        files()
        return

    # adding of total deposits as balance
    bal = sum(amount_db)
    print(f"Your Balance is {bal}gh")
    files()

# Depositing Money into Wallet
def deposit():
    print("==========================")
    print("DEPOSIT PAGE")
    print("==========================")
    dep_amt = int(input("Enter Amount You want to Deposit: "))
    amount_db.append(dep_amt)
    pin = int(input('Enter Pin: '))
    password =input_pin(pin)

    # adding of new deposit to an existing one
    total_balance = sum(amount_db)

    if not password:
        print("Invalid Pin")
        return

    if password:
        print(f'''You Have Successfully Deposited an Amount of {dep_amt}GH total Balance is {total_balance}GH
        ''')
        files()
    print('====================================================================')


# Selection Page
def files():
    while True:
        # print items
        print("==========================")
        for nums,opts in enumerate(select_opt):
            print(nums+1,opts["option"])
    
        option = input(": ")
        print("-----------")
        if option == "1":
            transfer_money() 
        elif option == "5":
            deposit()
        elif option == "2":
            balance()
        else:
                print("Invalid Option. Please try again.")
                continue
        break

# First Dial Command
def dial_1():
    cash = [{"amount":["0.5","1","2","3","4","5","10"]}]
    extra = [{"amount":["0.5","1","2","3","4","5","10"]}]

    ans = random.randint(0, len(cash[0]["amount"])-1)
    ext = random.randint(0, len(extra[0]["amount"])-1)
    reply = ("Your a/c is GHC"+(str(ans)) + " " + "Xtra-time:"+(str(ext)) + "GH") 
    print(reply)


# Login Authentication
def login():
    print("""LOGIN PAGE
    """)
    Pin = int(input("Enter Pin: "))
    Phone_no = int(input("Enter Phone Number: "))

    if user_login(Pin, Phone_no):
        files()
    
    else:
        print("""Invalid Inputs  
        """)
        intro()

# Register Authentication
def register():
    
    print("REGISTER BELOW")
    print("""""")

    Pin = int(input("Enter Pin: "))
    Phone_no = int(input("Enter Number: ")) 
    print("""""")
    select = ("SELECT FROM THE OPTIONS BELOW")
    print(select)
    if create_user(Pin, Phone_no):
        files()

    else:
        print("Invalid input")
    print('========================')
    files()


# Default Page
def intro():
    print("=================================================")
    print("""YOUR PORTAL
            1.REGISTER          2.LOGIN
    """)
    print("=================================================")
   
    dial = input("     ")
    if dial == "1": 
        register()       
    elif dial == "2":
        login()   
    else:
        print("oooPs!! Wrong Input!")

def console():
    intro() 

# running app
console() 