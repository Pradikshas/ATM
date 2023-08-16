try:
    print("Welcome to Indian Overseas bank:")
    a = input("Insert your Card: ")
    j = 10000
    pin = 1234

    def bank_transaction():
        global j

        if a:
            print("Select 1 - withdraw\n2 - bank balance\n3 - pin number change")
            k = int(input())

            if k == 1:
                print("Enter withdrawal amount:")
                am = int(input())
                print("Enter PIN:")
                pinned = int(input())
                if pin == pinned:
                    if am > j:
                        print("Your requested amount is higher than your bank balance")
                        bank_transaction()
                    else:
                        print("Please collect your cash")
                        j -= am
                        print("Updated bank balance:", j)
                        bank_transaction()
                else:
                    print("Incorrect PIN")
                    bank_transaction()

            elif k == 2:
                print("View bank balance")
                print("Your bank balance for your account is", j)
                bank_transaction()

            elif k == 3:
                print("Enter your current PIN number")
                current = int(input())
                if current == pin:
                    newpin = int(input("Enter your new PIN number: "))
                    print("Your old PIN", current, "Changed to", newpin)
                    bank_transaction()
                else:
                    print("Incorrect PIN")
                    bank_transaction()

            else:
                print("Enter 1, 2, or 3 only")
                bank_transaction()

    if a:
        bank_transaction()

    else:
        print("Please enter your card")

except Exception as e:
    print("An error occurred:", e)
finally:
    print("Thank you for using our ATM.")
