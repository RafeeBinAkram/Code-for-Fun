import random

def play():
    target = random.randint(1, 100)
    
    while True:
        inp = int(input("Enter your number: "))
        difference = inp-target
        
        if difference>0:
            print("😂 Your guess is greater than target!")
        elif difference<0:
            print("😁 Your guess is smaller than target!")
        
        if abs(difference)>10:
            print("🎃 It's too far...")
        
        if difference==0:
            print("🎉🎉🎉 Congratulations !! You've found it...")
            break
        print()
        
if __name__=="__main__":
    print("🎈🎈🎈Number Guessing Game🎈🎈🎈")
    print("\nRule: If the difference between your guess and the magic number is more than 10, computer will prompt It's too far..\n\n ***Game Starts***\n")
    play()
    
    
    
    
    
    
    
    
    
    
    
