import random
def sumplayer():
    a=0
    for n in player:
        a+=n
    return a
def sumdealer():
    b=0
    for n in dealer:
        b+=n
    return b
condition=True
while condition:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    dealer = [(random.choice(cards)), (random.choice(cards))]
    player = [(random.choice(cards)), (random.choice(cards))]
    print(f"Dealer:{dealer[0]}")
    print(f"Player:{player}")

    while True:
        if sumplayer()<21:
            user_choice=input("Hit or Stand: ").lower()
            if user_choice=="hit":
                player.append(random.choice(cards))
                print(sumplayer())
                print(f"player:{player}")
            else:
                break
        else:
            break
    while True:
        if sumdealer()<17:
            dealer.append(random.choice(cards))
            #print(sumdealer())
            #print(f"dealer:{dealer}")
        else:
            break

    """RESULT"""

    if sumplayer()>21:
        print(f"{player}:{sumplayer()}\nplayer loose!\nPlayer went over ")
        print(f"{dealer}:{sumdealer()}\ndealer win! ")
    elif sumdealer()>21:
        print(f"{player}:{sumplayer()}\nplayer win! ")
        print(f"{dealer}:{sumdealer()}\ndealer loose! \nDealer went over ")
    elif sumdealer()==sumplayer():
        print(f"player:-{player}:{sumplayer()}\ndealer:-{dealer}:{sumdealer()}\nIt's a draw")
    elif sumplayer()>sumdealer():
        print(f"{player}:{sumplayer()}\nplayer win! ")
        print(f"{dealer}:{sumdealer()}\ndealer loose!\nScore is lesser then the player ")
    elif sumdealer()>sumplayer():
        print(f"{player}:{sumplayer()}\nplayer loose!\nScore is lesser then the dealer  ")
        print(f"{dealer}:{sumdealer()}\ndealer win! ")

    user_wish =input("Do you want to play? type 'Y' to play,type 'N' to stop:").lower()
    if user_wish=="n":
        condition=False
        break
    else:
        print("\n"*20)

