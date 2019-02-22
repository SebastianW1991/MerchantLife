totalMoney = float(40.30)
beerPriceX = float(0.05)
foodPriceX = float(0.15)
rentPriceX = float(1.00)
horseFoodX = float(2.00)
print("Hello")
name = input("Please, insert your name ")
beginning = input("Hello " + name + ", after long time spent on foreign university, your uncle sent "
                  "you a letter with horrible news"
                  "\ndue to recent disease your father and mother deceased. What is worse, after their death, "
                  "your home was caught by fire \nAll what remained is pair of old horses, "
                  "old cart  and 50 feet of linen cloth for sale and 40 guldens and 30 talars."
                  "\nFinally you reclaimed what you possess. What will you do?"
                  " You are next to your old home and you feel saddened. "
                  "You can:\n[a] Go to market,\n[b] Go to tavern, "
                  "\n[c]Leave the city.""Choose your option by choosing letters ")
while beginning:

    if beginning == "a":
        marketX = input("Welcome on the market of Xarthas, what you plan to do? \n[a] Go to horse merchant,\n"
                        "[b] Go to armor merchant,\n[c] Go to wine merchant,\n[d] Go to weapon merchant "
                        "\n[e] Go to wheat merchant \n[f] Try to sell your goods")
        if marketX == "a":
            print("Greetings, are you looking for new steed?")
        elif marketX == "b":
            print("Greetings, I see that you are not warrior, please let me show you my best crafts")
        elif marketX == "c":
            print("Here, take a look at the finest wines in Xarthas")
        elif marketX == "d":
            print("Welcome in the finest armory of this city")
        elif marketX == "e":
            print("Welcome in Jacobsen & Sons")
        elif marketX == "f":
            print("You set up your stool and wait for buyer of your stuff")
    elif beginning == "b":
        tavernX = input("Welcome in Hanging Bear. You can: \n [a] buy a beer for 5 talars. \n "
                        "[b] buy food for you for 15 talars .\n "
                        "[c] rent a room for 1 gulden. \n [d] buy food for your horses for 2 guldens. \n "
                        "[e] leave tavern.")

        if tavernX == "a":
            totalMoney = totalMoney - beerPriceX
            tavernXa = input("You feel happier, yet your pocket is lighter. You have " + str(totalMoney) + " total"
                             " Do you wish to do anything else? You can:\n [a] buy food for you for 15 talars. \n "
                             "[b] rent a room for 1 gulden. \n [c] buy food for your horses for 2 guldens. \n "
                             "[d] leave tavern.")
            if tavernXa == "a":
                totalMoney = totalMoney - foodPriceX
                tavernXaA = input(" You feel healthier, but your money bag contains only " + str(totalMoney) + " now. "
                                  "You can either:\n [a]rent a room for 1 gulden. \n "
                                  "[b] buy food for your horses for 2 guldens."
                                  "\n [c] leave tavern. ")
                if tavernXaA == "a":
                    totalMoney = totalMoney - rentPriceX
                    tavernXaAa = input("Yaawn, that was good night Now you posses only a mere " + str(totalMoney) + ""
                                       " guldens. You can: \n [a] feed your horses for 2 guldens.\n [b] leave the "
                                       "tavern.")
                    if tavernXaAa == "a":
                        totalMoney = totalMoney - horseFoodX
                        tavernXaAaA = input("Now you have " + str(totalMoney) + " guldens and your horses "
                                            "are well feed."
                                            "Having none activities here, you decided to leave tavern. Now you can :\n"
                                            "[a] go to market. \n[b] leave the city.")
                        if tavernXaAaA == "a":
                            tavernXaAaA = (marketX == "a")
                        else:
                            tavernXaAaA = (outskirtsX == "c")
            elif tavernXa == "b":
                totalMoney = totalMoney - rentPriceX
                tavernXaA = input("Yaawn, that was good night Now you posses only a mere " + str(totalMoney) +
                                  " guldens. Now you can:"
                                  "\n [a] buy food for your horses for 2 guldens \n [b] leave the tavern")
            elif tavernXa == "c":
                totalMoney = totalMoney - horseFoodX
                print("Now you have only " + str(totalMoney) + " guldens, but at least your horses are well feed")
            else:
                print("You left tavern, What do you plan to do?")

        if tavernX == "b":
            totalMoney = totalMoney - foodPriceX
            print("Your stomach is full and you are ready for upcoming events. You have " + str(totalMoney) + " left")
        elif tavernX == "c":
            totalMoney = totalMoney - rentPriceX
            print("You got some rest. But your pocket contains now " + str(totalMoney) + " coins")
        elif tavernX == "d":
            totalMoney = totalMoney - horseFoodX
            print("Your horses are well feed now and healthier. You have now " + str(totalMoney))
    elif beginning == "c":
        outskirtsX = input("You are at outskirts of the city")
    else:
        beginning = input("Choose your option by choosing letters : a or b or c")
