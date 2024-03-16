print("Welcome to the vending machine change maker program")
print("Change maker initialized.")

nickels = 25#26
dimes = 25
quarters = 25
ones = 0
fives = 0

total_cents = (nickels * 5) + (dimes * 10) + (quarters * 25) + (ones * 100) + (fives * 500)

print("Stock contains:")
print(f"     {nickels} nickels")
print(f"     {dimes} dimes")
print(f"     {quarters} quarters")
print(f"     {ones} ones")
print(f"     {fives} fives")
print()

bool = True




while bool == True:
    user_input = input("Enter the purchase price (xx.xx) or `q' to quit: ")
    if user_input == "q":

        total_cents = (nickels * 5) + (dimes * 10) + (quarters * 25) + (ones * 100) + (fives * 500)
        print(f"Total: {total_cents // 100} dollars and {total_cents % 100} cents")
        bool = False

    else:
        user_cents = float(user_input) * 100 #1.95 * 100 = 195.00
        x = user_cents % 5 # this will zero
        if x != 0: #like 1.96
            print("Illegal price: Must be a non-negative multiple of 5 cents.")
            print()
        else :
            print()
            print("Menu for deposits:")
            print("'n' - deposit a nickel")
            print("'d' - deposit a dime")
            print("'q' - deposit a quarter")
            print("'o' - deposit a one dollar bill")
            print("'f' - deposit a five dollar bill")
            print("'c' - cancel the purchase")
            print()
            print(f"Payment due: {user_cents // 100:.0f} dollars and {user_cents % 100:.0f} cents")
            i = 0

            while i < user_cents:
                vald = True
                while vald == True:
                    z = input("Indicate your deposit: ")
                    if z == "n":
                        user_cents -= 5
                        nickels += 1

                        if user_cents < 0:
                            positive = abs(user_cents)
                            list = [25, 10, 5]
                            print("Please take the change below.")
                            for coin in list:
                                fi = 0
                                on = 0
                                qa = 0
                                di = 0
                                ni = 0
                                while positive >= coin:
                                    positive = positive - coin
                                    if coin == 500:

                                        fives -= 1
                                        fi += 1
                                    elif coin == 100:

                                        ones -= 1
                                        on += 1
                                    elif coin == 25:

                                        quarters -= 1
                                        qa += 1

                                    elif coin == 10:

                                        dimes -= 1
                                        di += 1
                                    elif coin == 5:

                                        nickels -= 1
                                        ni += 1
                                if di > 0:
                                    print(f"{di} dime")
                                elif on > 0:
                                    print(f"{on} dollar")
                                elif ni > 0:
                                    print(f"{ni} nickel")
                                elif fi > 0:
                                    print(f"{fi} five")
                                elif qa > 0:
                                    print(f"{qa} quarter")
                            break
                        elif user_cents == 0:
                            print("No Change due")
                            break
                        print(f"Payment due: {user_cents // 100:.0f} dollars and {user_cents % 100:.0f} cents")
                    elif z == "d":
                        user_cents -= 10
                        dimes += 1
                        if user_cents < 0:
                            positive = abs(user_cents)
                            list = [25, 10, 5]
                            print("Please take the change below.")
                            for coin in list:
                                fi = 0
                                on = 0
                                qa = 0
                                di = 0
                                ni = 0
                                while positive >= coin:
                                    positive = positive - coin
                                    if coin == 500:
                                        # print("five dollar")
                                        fives -= 1
                                        fi += 1
                                    elif coin == 100:
                                        # print("one dollar")
                                        ones -= 1
                                        on += 1
                                    elif coin == 25:
                                        # print("1 quarter")
                                        quarters -= 1
                                        qa += 1
                                    elif coin == 10:
                                        # print("1 dime")
                                        dimes -= 1
                                        di += 1
                                    elif coin == 5:
                                        # print("1 nickel")
                                        nickels -= 1
                                        ni += 1
                                if di > 0:
                                    print(f"{di} dime")
                                elif on > 0:
                                    print(f"{on} dollar")
                                elif ni > 0:
                                    print(f"{ni} nickel")
                                elif fi > 0:
                                    print(f"{fi} five")
                                elif qa > 0:
                                    print(f"{qa} quarter")
                            break
                        elif user_cents == 0:
                            print("No Change due")


                            break
                        print(f"Payment due: {user_cents // 100:.0f} dollars and {user_cents % 100:.0f} cents")
                    elif z == "q":
                        user_cents -= 25
                        quarters += 1
                        if user_cents < 0:
                            positive = abs(user_cents)
                            list = [25, 10, 5]
                            print("Please take the change below.")
                            for coin in list:
                                fi = 0
                                on = 0
                                qa = 0
                                di = 0
                                ni = 0
                                while positive >= coin:
                                    positive = positive - coin
                                    if coin == 500:
                                        # print("five dollar")
                                        fives -= 1
                                        fi += 1
                                    elif coin == 100:
                                        # print("one dollar")
                                        ones -= 1
                                        on += 1
                                    elif coin == 25:
                                        # print("1 quarter")
                                        quarters -= 1
                                        qa += 1
                                    elif coin == 10:
                                        # print("1 dime")
                                        dimes -= 1
                                        di += 1
                                    elif coin == 5:
                                        # print("1 nickel")
                                        nickels -= 1
                                        ni += 1
                                if di > 0:
                                    print(f"{di} dime")
                                elif on > 0:
                                    print(f"{on} dollar")
                                elif ni > 0:
                                    print(f"{ni} nickel")
                                elif fi > 0:
                                    print(f"{fi} five")
                                elif qa > 0:
                                    print(f"{qa} quarter")
                            break
                        elif user_cents == 0:
                            print("No Change due")
                            break
                        print(f"Payment due: {user_cents // 100:.0f} dollars and {user_cents % 100:.0f} cents")
                    elif z == "o":
                        user_cents -= 100

                        ones += 1
                        if user_cents < 0:
                            positive = abs(user_cents)
                            list = [25, 10, 5]
                            print("Please take the change below.")
                            for coin in list:
                                fi = 0
                                on = 0
                                qa = 0
                                di = 0
                                ni = 0
                                while positive >= coin:
                                    positive = positive - coin
                                    if coin == 500:
                                        # print("five dollar")
                                        fives -= 1
                                        fi += 1
                                    elif coin == 100:
                                        # print("one dollar")
                                        ones -= 1
                                        on += 1
                                    elif coin == 25:
                                        # print("1 quarter")
                                        quarters -= 1
                                        qa += 1
                                    elif coin == 10:
                                        # print("1 dime")
                                        dimes -= 1
                                        di += 1
                                    elif coin == 5:
                                        # print("1 nickel")
                                        nickels -= 1
                                        ni += 1

                                if di > 0:
                                    print(f"{di} dime")
                                elif on > 0:
                                    print(f"{on} dollar")
                                elif ni > 0:
                                    print(f"{ni} nickel")
                                elif fi > 0:
                                    print(f"{fi} five")
                                elif qa > 0:
                                    print(f"{qa} quarter")
                            break
                        elif user_cents == 0:
                            print("No Change due")

                            break
                        print(f"Payment due: {user_cents // 100:.0f} dollars and {user_cents % 100:.0f} cents")
                    elif z == "f":
                        user_cents -= 500
                        fives += 1
                        if user_cents < 0:
                            positive = abs(user_cents)
                            list = [25, 10, 5]
                            print("Please take the change below.")
                            for coin in list:
                                fi = 0
                                on = 0
                                qa = 0
                                di = 0
                                ni = 0
                                while positive >= coin:
                                    positive = positive - coin
                                    if coin == 500:
                                        # print("five dollar")
                                        fives -= 1
                                        fi += 1
                                    elif coin == 100:
                                        # print("one dollar")
                                        ones -= 1
                                        on += 1

                                    elif coin == 25:
                                        # print("1 quarterxxxx")
                                        quarters -= 1
                                        qa += 1
                                    elif coin == 10:
                                        # print("1 dime")
                                        dimes -= 1
                                        di += 1
                                    elif coin == 5:
                                        # print("1 nickel")
                                        nickels -= 1
                                        ni += 1
                                if di > 0:
                                    print(f"{di} dime")
                                elif on > 0:
                                    print(f"{on} dollar")
                                elif ni > 0:
                                    print(f"{ni} nickel")
                                elif fi > 0:
                                    print(f"{fi} five")
                                elif qa > 0:
                                    print(f"{qa} quarter")
                            break
                        elif user_cents == 0:
                            print("No Change due")

                            break
                        print(f"Payment due: {user_cents // 100:.0f} dollars and {user_cents % 100:.0f} cents")

                    elif z == "c":
                        vald = False
                        i = 10000000
                        # print(user_cents, user_input)
                        positive = (float(user_input)*100) - user_cents
                        # print(positive)
                        list = [25, 10, 5]
                        print("Please take the change below.")
                        for coin in list:
                            fi = 0
                            on = 0
                            qa = 0
                            di = 0
                            ni = 0
                            while positive >= coin:
                                positive = positive - coin
                                if coin == 500:
                                    # print("five dollar")
                                    fives -= 1
                                    fi += 1
                                elif coin == 100:
                                    # print("one dollar")
                                    ones -= 1
                                    on += 1
                                elif coin == 25:
                                    # print("1 quarter")
                                    quarters -= 1
                                    qa += 1
                                elif coin == 10:
                                    # print("1 dime")
                                    dimes -= 1
                                    di += 1
                                elif coin == 5:
                                    # print("1 nickel")
                                    nickels -= 1
                                    ni += 1
                            if di > 0:
                                print(f"{di} dime")
                            elif on > 0:
                                print(f"{on} dollar")
                            elif ni > 0:
                                print(f"{ni} nickel")
                            elif fi > 0:
                                print(f"{fi} five")
                            elif qa > 0:
                                print(f"{qa} quarter")
                    else:
                        print("Illegal selection:",z)
                 


                if nickels < 0:
                    print("Machine is out of nickel.")
                    print("See store manager for remaining refund.")
                    print(f"Amount due is {(abs(ni)*5)/100} Dollar")
                    nickels = nickels + abs(nickels)
                elif dimes < 0:
                    print("Machine is out of dimes.")
                    print("See store manager for remaining refund.")
                    print(f"Amount due is {abs(dimes)*10/100} Dollar")
                    dimes = dimes + abs(dimes)
                elif quarters < 0:
                    print("Machine is out of quarters.")
                    print("See store manager for remaining refund.")
                    print(f"Amount due is {(abs(quarters) * 25)/100} Dollar")
                    quarters = quarters + abs(quarters)
                elif ones < 0:
                    print("Machine is out of ones.")
                    print("See store manager for remaining refund.")
                    print(f"Amount due is {(abs(ones)*1)/100} Dollar")
                    ones = ones + abs(ones)

                elif fives < 0:
                    print("Machine is out of fives.")
                    print("See store manager for remaining refund.")
                    print(f"Amount due is {(abs(fives)*5)/100} Dollar")
                    fives = fives + abs(fives)
                print()
                print("Stock contains:")
                print(f"     {nickels} nickels")
                print(f"     {dimes} dimes")
                print(f"     {quarters} quarters")
                print(f"     {ones} dollars")
                print(f"     {fives} five dollars")
                print()