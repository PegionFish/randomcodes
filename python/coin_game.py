from random import randrange

coin_user, coin_bot = 10, 10
rounds_of_game = 0

def bet(dice, wager):
    if dice == 7:

        print(f"The dice is {dice};\nDRAW!\n")
        return 0

    elif dice < 7:

        if wager == "s":
            print(f"The dice is {dice};\nYOU WIN!\n")
            return 1

        else:
            print(f"The dice is {dice};\nYOU LOST!\n")
            return -1

    elif dice > 7:

        if wager == "s":
            print(f"The dice is {dice};\nYOU LOST!\n")
            return 1

        else:
            print(f"The dice is {dice};\nYOU WIN!\n")
            return -1

while True:

    print(f"You:{coin_user}\t Bot:{coin_bot}")
    dice = randrange(2, 13)

    wager = input("What is your bet?")

    if wager == "q":
        break
    elif wager in "bs":
        result = bet(dice, wager)
        coin_user += result
        coin_bot -= result
        rounds_of_game += 1
    if coin_user == 0:
        print("Woops, you've LOST ALL, and GG")
        break
    elif coin_bot == 0:
        print("Woops, you've won all, and GG")
        break

print(f"You've played {rounds_of_game} rounds.\n")
print(f"You have {coin_user} coins now.Bye\n")