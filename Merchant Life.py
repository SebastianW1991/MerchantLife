totalMoney = float(40.30)
beerPriceX = float(0.05)
foodPriceX = float(0.15)
rentPriceX = float(1.00)
horseFoodX = float(2.00)
oldMulePriceX = float(5.00)
mulePrixeX = float(8.00)
strongMulePriceX = float(10.00)

print("Hello")
name = input("Please, insert your name ")
beginning = open('beginning.txt').read()
beginning = input("Hello " + name + beginning + "[a] Go to market,\n [b] Go to tavern, \n [c] Leave the city."
                  "\nChoose your option by choosing letters above ")
while beginning:

    if beginning == "a":
        marketX = open('marketX.txt').read()
        marketX = input(marketX)
        if marketX == "a":
            marketXa = open('marketXa.txt').read()
            marketXa = input('Welcome in Augias stable, please, take a look on our steeds' + marketXa + '')
        elif marketX == "b":
            marketXb = open('marketXb.txt')
            marketXb = input("Greetings, I see that you are not warrior, let me show you my crafts" + marketXb + '')
        elif marketX == "c":
            print("Here, take a look at the finest wines in Xarthas")
        elif marketX == "d":
            print("Welcome in the finest armory of this city")
        elif marketX == "e":
            print("Welcome in Jacobsen & Sons")
        elif marketX == "f":
            print("You set up your stool and wait for buyer of your stuff")
#tawerna
    elif beginning == "b":
        tavernX = open('tavernX.txt').read()
        tavernX = input(tavernX)
        if tavernX == "a":
            # tavern beer
            totalMoney = totalMoney - beerPriceX
            tavernXa = open('tavernXa.txt').read()
            tavernXa = input("You feel happier, yet your pocket is lighter. You have " + str(totalMoney) + " total"
                             + tavernXa + "")
            if tavernXa == "a":
                totalMoney = totalMoney - foodPriceX  # tavern beer and food
                tavernXaA = open('tavernXaA.txt').read()
                tavernXaA = input(" You feel healthier, but your money bag contains only " + str(totalMoney) + " now. "
                                  + tavernXaA + "")
                if tavernXaA == "a":
                    totalMoney = totalMoney - rentPriceX  # tavern beer and food and rent
                    tavernXaAa = open('tavernXaAa.txt').read()
                    tavernXaAa = input("Yaawn, that was good night Now you posses only a mere " + str(totalMoney) +
                                       " guldens." + tavernXaAa + "")
                    if tavernXaAa == "a":
                        totalMoney = totalMoney - horseFoodX  # tavern beer and food and rent and horse food
                        tavernXaAaA = open('tavernXaAaA.txt').read()
                        tavernXaAaA = input("Now you have " + str(totalMoney) + " and your horses are well feed. "
                                            + tavernXaAaA + "")
                        if tavernXaAaA == "a":
                            beginning = "a"
                        elif tavernXaAaA == "b":
                            beginning = "c"
                        else:
                            print('error, choose again')
                            tavernXaAaA = open('tavernXaAaA.txt').read()
                            tavernXaAaA = input("Now you have " + str(totalMoney) + " and your horses are well feed. "
                                                + tavernXaAaA + "")
                            if tavernXaAaA == "a":
                                beginning = "a"
                            elif tavernXaAaA == "b":
                                beginning = "c"
                    elif tavernXaAa == "b":
                        tavernXaAaB = input("You left the tavern. You can :\n[a] go to market. \n[b] leave the city.")
                        if tavernXaAaB == "a":
                            beginning = "a"
                        else:
                            beginning = "c"
            elif tavernXa == "b":
                totalMoney = totalMoney - foodPriceX
                tavernXaB = open('tavernXaB.txt').read()
                tavernXaB = input("You feel healthier now. Now you posses only a mere " + str(totalMoney) + ""
                                  + tavernXaB + "")
            elif tavernXa == "c":
                totalMoney = totalMoney - rentPriceX
                tavernXaC = input("Yaawn, that was good night Now you posses only a mere " + str(totalMoney) +
                                  " guldens. Now you can:"
                                  "\n[a] buy food for your horses for 2 guldens \n[b] leave the tavern")
            elif tavernXa == "d":
                totalMoney = totalMoney - horseFoodX
                print("Now you have only " + str(totalMoney) + " guldens, but at least your horses are well feed")
            else:

                tavernXaE = open('tavernXe').read()
                input("You left tavern, What do you plan to do?" + tavernXe + " ")
                if tavernXaE == "a":
                    beginning = "a"
                elif tavernXaE == "b":
                    beginning = "c"
                else:
                    tavernX = "a"

        elif tavernX == "b":
            totalMoney = totalMoney - foodPriceX
            tavernXb = open('tavernXb.txt').read()
            tavernXb = input("Your stomach is full and you are ready for upcoming events. You have " + str(totalMoney) +
                             " left." + tavernXb + "")
            if tavernXb == "a":
                totalMoney = totalMoney - beerPriceX
                tavernXbA = open('tavernXbA.txt').read()
                tavernXbA = input("You feel happier, yet your pocket is lighter. You have " + str(totalMoney) + " total"
                                  + tavernXbA + "")
            elif tavernXb == "b":
                totalMoney = totalMoney - rentPriceX
                tavernXbB = open('tavernXbB.txt').read()
                tavernXbB = input("Yaawn, that was good night Now you posses only a mere " + str(totalMoney) + "" +
                                  tavernXbB + " ")
            elif tavernXb == "c":
                totalMoney = totalMoney - horseFoodX
                tavernXbC = open('tavernXbC.txt').read()
                tavernXbC = input("Your horses are well feed now and healthier. You have now " + str(totalMoney) + "" +
                                  tavernXbC + " ")
            else:
                tavernXbD = input("You left the tavern. You can :\n[a] go to market. \n[b] leave the city.\n"
                                  "[c] return to tavern")
                if tavernXbD == "a":
                    beginning = "a"
                elif tavernXbD == "b":
                    beginning = "c"
                else:
                    tavernX = "b"
        elif tavernX == "c":
            totalMoney = totalMoney - rentPriceX
            tavernXc = open('tavernXc.txt').read()
            tavernXc = input("You got some rest. But your pocket contains now " + str(totalMoney) + " coins "
                             + tavernXc + " ")
            if tavernXc == "a":
                totalMoney = totalMoney - beerPriceX
                tavernXcA = open('tavernXcA.txt').read()
                tavernXcA = input("You feel happier, yet your pocket is lighter. You have " + str(totalMoney) + " total"
                                  " Do you wish to do anything else?" + tavernXcA + " ")
            elif tavernXc == "b":
                totalMoney = totalMoney - foodPriceX
                tavernXcB = open('tavernXcB.txt').read()
                tavernXcB = input("Your stomach is full and you are ready for upcoming events. "
                                  "You have " + str(totalMoney) + " left." + tavernXcB + " ")
            elif tavernXc == "c":
                totalMoney = totalMoney - horseFoodX
                tavernXcC = input("Your horses are well feed now and healthier. You have now " + str(totalMoney) + ""
                                  "You still can:\n [a] buy a beer for 5 talars. \n "
                                  "[b] buy food for you for 15 talars. \n[c] leave tavern.")
            elif tavernXc == "d":
                tavernXcD = input("You left the tavern. You can :\n[a] go to market. \n[b] leave the city.\n"
                                  "[c] return to tavern")
                if tavernXcD == "a":
                    beginning = "a"
                elif tavernXcD == "b":
                    beginning = "c"
                else:
                    tavernX = "b"
        elif tavernX == "d":
            totalMoney = totalMoney - horseFoodX
            tavernXd = input("Your horses are well feed now and healthier. You have now " + str(totalMoney) + ""
                             "You still can:\n [a] buy a beer for 5 talars. \n "
                             "[b] buy food for you for 15 talars. \n[c] rent a room for 1 gulden. \n "
                             "[d] leave tavern.")
            if tavernXd == "a":
                totalMoney = totalMoney - beerPriceX
                tavernXdA = input("You feel happier, yet your pocket is lighter. You have " + str(totalMoney) + " total"
                                  " Do you wish to do anything else? You can:\n "
                                  "[a] buy food for you for 15 talars.\n [b] buy food for your horses for 2 guldens.\n "
                                  "[c] leave tavern.")
                if tavernXdA == "a":
                    totalMoney = totalMoney - foodPriceX
                elif tavernXdA == "b":
                    totalMoney = totalMoney - horseFoodX


            elif tavernXd == "b":
                totalMoney = totalMoney - foodPriceX
            elif tavernXd == "c":
                totalMoney = totalMoney - rentPriceX
            elif tavernXd == "d":
                tavernXdD = input("You left the tavern. You can :\n[a] go to market. \n[b] leave the city.\n"
                                  "[c] return to tavern")
                if tavernXdD == "a":
                    beginning = "a"
                elif tavernXdD == "b":
                    beginning = "c"
                else:
                    tavernX = "b"
        else:
            tavernXe = input("You left the tavern. You can :\n[a] go to market. \n[b] leave the city.\n"
                             "[c] return to tavern")
    elif beginning == "c":
        outskirtsX = open('outskirtsX.txt').read()
        outskirtsX = input(outskirtsX)
    else:
        beginning = input("Choose your option by choosing letters : a or b or c")
