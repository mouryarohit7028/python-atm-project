print(" WELCOME TO ABC BANK !!  \n Please Insert your card \n ")
pin=1212
chances=3
balance=5

while chances !=0:
    user_pin=int(input("please enter your four digit pin :"))

    if user_pin != pin:
        chances -=1
        print("Wrong pin number")
        print(f"you have {chances} chance left")

    else:
        user_choice=input(" B : balance ,D : deposit ,W : withdraw \n ")
        if user_choice == "B":
            print(f" Your total balance is RS.{balance} ")

            print("=========================================================")
            print("=========================================================")


        if user_choice == "D":
            deposit_user=int(input("Enter a amount you would like to deposit : "))

            print("=========================================================")
            print("=========================================================")

            total_balance=balance +deposit_user

            print(f"you have deposited RS.{deposit_user}")

            print("=========================================================")
            print("=========================================================")
            print(f"Your updated balance is RS.{total_balance}")

            print("=========================================================")
            print("=========================================================")

        
        if user_choice =="W" :
            withdraw_user=int(input("Enter the amount you want to withdraw : "))

            print("=========================================================")
            print("=========================================================")

            total_balance=total_balance-withdraw_user

            print(f"You have withdrawn RS.{withdraw_user}")

            print("=========================================================")
            print("=========================================================")

            print(f"your updated balance is RS.{total_balance}")

            print("=========================================================")
            print("=========================================================")

    user_exit=input("would you like to exit ? Yes/No \n ")
    if user_exit =="Yes":
        print("Thankyou for using ABC bank !!")
        break
    else:
        continue

