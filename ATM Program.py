import time


print("""
***********************
Welcome to ATM ...

Operations :
(1) - Balance Inquiry

(2) - Deposit Money


(3) - Withdraw Money
 

Press 'Q' to End Transactions.


***********************
""")

balance = 13500

sys_password = 1903

right_of_entry = 3


def transactions(balance):
    while True:

        transaction = input("Select Transaction.")

        if (transaction  == "Q"):
           try:
                print("We wish you a nice day.")
                print("ATM will be activated soon.")
                time.sleep(5)
                break
           except ValueError:
               print("The value you entered does not match our format, please try again.")
           except Exception as error:
               print(f"Error message: {error}")

        elif (transaction == "1"):
             try:
                print("Your new balance is {} TL.".format(balance))
             except ValueError:
                 print("The value you entered does not match our format, please try again.")
             except Exception as error:
                 print(f"Error message: {error}")
        elif (transaction == "2"):
            try:
                amount = int(input("Enter the amount you want to deposit."))
                balance += 	amount
                print("Your new balance is {} TL.".format(balance))
            except ValueError:
                print("The value you entered does not match our format, please try again.")
            except Exception as error:
                print(f"Error message: {error}")

        elif (transaction== "3"):
            try:
                amount = int(input("Enter the amount to be withdrawn."))
                if (balance - 	amount< 0):
                    print("Insufficient Balance!!!")
                else:
                    balance -= 	amount
                    print("Your new balance is {} TL.".format(balance))
            except ValueError:
                print("The value you entered does not match our format, please try again.")
            except Exception as error:
                print(f"Error message: {error}")

while right_of_entry > 0:
    password = int(input("Enter Your Password."))

    if (password != sys_password):
        print("Your Password is Incorrect!")
        right_of_entry-= 1

    elif (password == sys_password):
        print("Welcome to Muratcan Acar.")
        transactions(balance)

    if (right_of_entry == 1):
        print("You Have One Login Right If You Enter Your Password Wrong, Your Card Will Be Blocked!")

    elif(right_of_entry == 0):
        print("Your Card Has Been Blocked You Can Open It By Going To Our Nearest Branch.")
        break
