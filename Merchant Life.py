totalMoney = float(40.30)
beerPriceX = float(0.05)
foodPriceX = float(0.15)
rentPriceX = float(1.00)
horseFoodX = float(2.00)
print("Hello")
name = input("Please, insert your name ")
print("Hello " + name +" after long time spent on foreign university, your uncle sent you a letter with horrible news\n"
 "due to recent epidemy your father and mother deceased. What is worse, after their death, your home was caught by fire\n"
"All what remained is pair of old horses, old cart  and 50 feet of linen cloth for sale and 40 guldens and 30 talars. Finally you reclaimed what you \n"
"posess. What will you do? You are next to your old home and you feel saddened.You can:[a] Go to market,[b] Go to tavern, [c]Leave the city.")
beginning = input("Choose your option by choosing letters ")
if beginning == "a":
    print("Welcome on the market of Xarthas, what you plan to do? \n [a] Go to horse merchant,\n [b] Go to armor merchant,\n"
          "[c]Go to wine merchant,\n [d]Go to weapon merchant \n[e] Go to wheat merchant \n[f] Try to sell your goods")
    marketx = input("Choose your option")
    if marketx == "a":
        print("Greetings, are you looking for new steed?")
    elif marketx == "b":
        print("Greetings, I see that you are not warrior, please let me show you my best crafts")
    elif marketx == "c":
        print("Here, take a look at the finest wines in Xarthas")
    elif marketx == "d":
        print("Welcome in the finest armory of this city")
    elif marketx == "e":
        print("Welcome in Jacobsen & Sons")
    elif marketx == "f":
        print("You set up your stool and wait for buyer of your stuff")
elif beginning == "b":
    print("Welcome in Hanging Bear. You can: \n [a] buy a beer for 5 talars \n [b] buy food for you for 15 talars \n [c] rent a room for 1 gulden \n [d] buy food for your horses for 2 guldens \n [e] leave tavern")
    tavernX = input("Choose your option: ")
    if tavernX == "a":
        totalMoney = totalMoney - beerPriceX

        print("You feel happier, yet your pocket is lighter. You have " + str(totalMoney) + " total")
    tavernXa = input("Do you wish to do anything else? You can:\n [a] buy food for you for 15 talars \n [b] rent a room for 1 gulden \n [c] buy food for your horses for 2 guldens \n [d] leave tavern")
    if tavernXa == "a":
        totalMoney = totalMoney - foodPriceX
        print(" You feel healthier, but your money bag contains only " + str(totalMoney) + " now")

    elif tavernX == "b":
        totalMoney = totalMoney - foodPriceX
        print("Your stomach is full and you are ready for upcoming events. You have " + str(totalMoney) + " left")
    elif tavernX == "c":
        totalMoney = totalMoney - rentPriceX
        print("You got some rest. But your pocket contains now " + str(totalMoney) + " coins")
    elif tavernX == "d":
        totalMoney = totalMoney - horseFoodX
        print("Your horses are well feed now and healthier.You have now " + str(totalMoney))


elif beginning == "c":
    print("You are at outskirts of the city")
else:
    beginning = input("Choose your option by choosing letters ")
