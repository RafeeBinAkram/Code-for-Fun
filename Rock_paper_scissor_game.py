import random

def play(player_name):
    choices = ['r', 'p', 's']
    status = True
    count = 0
    while status:
        count+=1
        player = input(player_name.capitalize()+': ')
        computer = random.choice(choices)
        print("Computer: %s\n" %(computer))
        if player == computer:
            print("\n😂😂 You are busted !")
            print("🏆🏆 Your Score: %d" %(count))
            status = False
            
            
if __name__=="__main__":
    print("_________Rock, Paper and Scissor Game_____________\n")
    print("Rule: Rock = r, Paper = p, Scissor = s\n")
    plr_name = input("Enter your name: ")
    print()
    play(plr_name)
    
    
