import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user=[]
comp=[]
user_score=0
comp_score=0

def calculate_score(cards):
    if sum(cards)==21 and cards==2:
        return -1
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "You Lose,Opponent has Blackjack 😱"
    elif u_score == 0:
        return "Congratulations!! You Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_the_game():
    for i in range(2):
        user.append(random.choice(cards))
        comp.append(random.choice(cards))

    flag=True
    while(flag):
        user_score=calculate_score(user)
        comp_score=calculate_score(comp)
        print(f"Your cards:{user} ,Your score:{user_score}")
        print(f"computer first card:{comp[0]}")
        if user_score==-1 or comp_score==-1 or user_score>21:
            flag=False
        else:
            user_choice=input("Do You want to pick a card.'Y' for yes 'N' for no").lower()
            if user_choice=="y":
                user.append(random.choice(cards))
            else:
                flag=False

    while comp_score<17 and comp_score!=-1:
        comp.append(random.choice(cards))
        comp_score=calculate_score(comp)

    print(f"Your Final deck of cards:{user}, Your score:{user_score}")
    print(f"Computer Final deck of cards:{comp}, Computer score:{comp_score}")
    print(compare(user_score,comp_score))


mood=input("""Do You want to start the Amazing BlackJack Game.
Type "Y" For yes "N" For no :""").lower()
if mood=='y':
    print("\n"*25)
    print(art.logo)
    play_the_game()