import art
import game_data
import random

print(art.logo)
flag=True

def clean(a):
    print("\n" * 30)
    print(a)


def check(guess,a_followers,b_followers):
    if a_followers>b_followers:
        return guess=="a"
    else:
        return guess=="b"

count = 0

while(flag):
    clean(art.logo)
    print(f"\033[1m🏆 Your Score: {count}\033[0m")  # Bold score display
    a=random.choice(game_data.data)
    b=random.choice(game_data.data)
    print("🔷Compare A:",a["name"], ", A" ,a["description"],", From ", a["country"])
    print(art.vs)
    print("🔶Against B:",b["name"], ", A" ,b["description"],", From ", b["country"])
    p=input("🤔Who has more followers \033[1m 'A' or 'B'\033[0m: ").lower()


    res=check(p,a["follower_count"],b["follower_count"])
    if res:
        count += 1
        print("🎉Correct! Your score increased.")
    else:
        flag = False
        clean(art.logo)
        print(art.lose)
        print(f"\033[1m💀 Game Over! Your final score is {count}.\033[0m")  # Bold game over message
        print("🔥 Thanks for playing! Try again? 😃")
