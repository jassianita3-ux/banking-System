import fun

bankCredentials={}
#load balance from text file
balance = fun.load_balance()

def main():
    global balance

    while True:
        print("\n===Welcome to Scot Bank!====")
        print("1. Create an Account")
        print("2.Login")
        print("3.Exit")
        try:
            choice=int(input("Enter a choice:"))
            if choice==1:
                username=input("Enter username:")
                if username in bankCredentials:
                    print("Username already exists!")
                    continue

                password1=input("Enter password:")
                password2=input("Confirm password.")
                if password1==password2 and password1 !="":
                    bankCredentials[username]=password1
                    print("Account Created Successfully!")

                else:
                    print("Passwords do not match or are empty!")    

            elif choice==2:
                username=input("Enter username:")
                password=input("Enter password:")
                if username in bankCredentials and bankCredentials[username]==password:#check username is valid
                    print("\nLogin Successful!")
                    
                while True:

                        print("\n===Banking Menu=== ")
                        print("1.Deposit")
                        print("2.Withdraw")
                        print("3.Check Balance")
                        print("4.Logout")

                        choice2=input("Enter choice:")
                        if choice2=="1":
                            balance= fun.deposit(balance)
                            fun.save_balance(balance)
                            print(f"New Balance:Rs{balance}")

                        elif choice2=="2":
                            balance=fun.withdraw(balance)
                            fun.save_balance(balance)
                            print(f"New Balance:Rs{balance}")
                        elif choice2=="3":
                            print(f"Available Balance:Rs{balance}")
                        elif choice2=="4":
                            print("Logging out...")    
                            break   

                        else:
                            print("Invalid Choice")

                else:
                    print("Invalid username or Password!")
            elif choice== 3:
                print("Thank you for using Scot Bank!")
                break

            else:
                print("Invalid Choice! Choose 1,2 or 3.")
    
        except ValueError:
            print("Please enter a valid numeric choice.")
            

main()