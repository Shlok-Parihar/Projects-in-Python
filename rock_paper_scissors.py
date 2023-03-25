import random

user_win = 0
lap_win = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("TYPE rock, paper, scissor TO PLAY. TO QUIT = q.").lower()
    if user_input == "q":
        break


    if user_input not in options:
        print("Type any choice.")
        continue

    random_number = random.randint(0,2)
    lap_pik = options[random_number]
    print("Laptop Picked",lap_pik+".")

    if user_input == lap_pik:
        print("DRAW.!")

    elif user_input == "rock" and lap_pik == "scissor":
        print("You won!")
        user_win += 1
        continue

    elif user_input == "paper" and lap_pik == "rock":
        print("You won!")
        user_win += 1
        continue

    elif user_input == "scissor" and lap_pik == "paper":
        print("You won!")
        user_win += 1
        continue
    
    else:
        print("laptop wins")
        lap_win += 1 
    continue

print("You won",user_win,"times.")
print("Lappy won",lap_win,"times.")

print("GOODBYE.")
    
