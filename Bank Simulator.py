import random
import datetime
import time
import colorama


def create_account():
    print(colorama.Fore.BLUE + colorama.Style.BRIGHT + "Welcome to Our Banking System" + colorama.Style.RESET_ALL)
    new_user = input("Enter Your Name: ")
    print(
        colorama.Fore.YELLOW + colorama.Style.BRIGHT + "Hello " + new_user + ", your 4 digit PIN Number will be generated shortly. Please provide some more details." + colorama.Style.RESET_ALL)
    print(
        "Please provide us with some more information like the Date of Birth to check if you are eligible to open an account or not.")
    dob = datetime.datetime(int(input("Enter Year: ")), int(input("Enter Month: ")), int(input("Enter Day: ")))
    dt_today = datetime.datetime.today()
    age = (dt_today - dob).days
    if age < 6575:
        print(colorama.Fore.RED+colorama.Style.BRIGHT)
        print("Minimum age requirements didn't fulfilled. In order to open a bank account you must be 18+....")
        time.sleep(1.5)
        print("Please Contact with our Representative for further details....")
        print(colorama.Style.RESET_ALL)
        exit()
    else:
        while True:
            check_pin = random.randint(1000, 9999)
            if check_pin not in credentials.values():
                new_pin = str(check_pin)
                print(
                    "Congratulations! You've Successfully Created a new account. Your PIN is {}. Pls don't share it with anyone !".format(new_pin))
                credentials[new_user] = new_pin
            break
        return


def acc_verification():
    global username, pin
    trial = 3
    print(colorama.Style.RESET_ALL)
    if username in credentials.keys() and pin == credentials[username]:
        print(colorama.Fore.BLUE+colorama.Style.BRIGHT+"You've successfully logged in...."+colorama.Style.RESET_ALL)
        return
    else:
        for i in range(trial, 0, -1):
            print(colorama.Fore.RED+colorama.Style.BRIGHT+"Incorrect Username or Password. Pls try again. You've {} trials left".format(i)+colorama.Style.RESET_ALL)
            username = input("Enter your name: ")
            pin = input("Enter your PIN: ")
            if username in credentials.keys() and pin == credentials[username]:
                print(colorama.Fore.BLUE+colorama.Style.BRIGHT+"You've successfully logged in...."+colorama.Style.RESET_ALL)
                return
        print(colorama.Fore.RED+colorama.Style.BRIGHT+"Sorry. This account has been locked for security issues. Pls contact with our representative"+colorama.Style.RESET_ALL)
        exit()


def deposit():
    current_balance = balance[username]
    money_deposit = int(input("Enter the amount to be deposited: "))
    updated_balance = current_balance + money_deposit
    balance[username] = updated_balance
    print(colorama.Fore.CYAN+colorama.Style.BRIGHT+"The money has been added to your account. Your new balance is $%d" % updated_balance + colorama.Style.RESET_ALL)
    return


def withdraw():
    current_balance = balance[username]
    money_withdraw = int(input("Enter the amount to be withdrawn: "))
    updated_balance = current_balance - money_withdraw
    balance[username] = updated_balance
    print(colorama.Fore.CYAN+colorama.Style.BRIGHT+"The money has been withdrawn from your account. Your new balance is $%d" % updated_balance + colorama.Style.RESET_ALL)
    return


def check_balance():
    print(colorama.Fore.CYAN+colorama.Style.BRIGHT)
    print("Your Current balance is $%d" % (balance[username]))
    print(colorama.Style.RESET_ALL)
    return


if __name__ == "__main__":

    # System Initialization
    credentials = {'Rafi': '1234'}
    balance = {'Rafi': 500}
    greet = "...Welcome to the Virtual Bank..."
    print(colorama.Fore.CYAN + colorama.Style.BRIGHT + greet)
    for i in range(len(greet)): print("_", end="")
    print()
    print(colorama.Style.RESET_ALL)
    time.sleep(2)

    print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "System: " + colorama.Style.RESET_ALL)
    print("Type 'Yes' if you are a new user")
    print("Type 'No' if you are not a new user")
    print(colorama.Fore.YELLOW+colorama.Style.BRIGHT)
    action = input("User: ")
    print(colorama.Style.RESET_ALL)
    action = action.lower()
    if action == 'yes':
        create_account()
    else:
        username = input("Enter your name: ")
        pin = input("Enter your PIN: ")
        acc_verification()
        print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "System:" + colorama.Style.RESET_ALL)

        print("Press '1' to check Current Balance")
        print("Press '2' to Withdraw money")
        print("Press '3' to Deposit money")
        print("Press Any other key to Exit")
        while True:
            print(colorama.Fore.YELLOW + colorama.Style.BRIGHT)
            action = input("User: ")
            print(colorama.Style.RESET_ALL)
            if action == '1':
                check_balance()
            elif action == '2':
                withdraw()
            elif action == '3':
                deposit()
            else:
                print("Logging out of the Session...")
                exit()

