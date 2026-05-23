import random
import sys
import time


points = 100
streak = 0
multiplier = 1
current_range = 100

ability_1 = int(0)
ability_2 = int(0)
ability_3 = int(0)
ability_4 = int(0)
ability_4_active = False
ability_5 = int(0)
ability_5_active = False
    
ability_1_costs = [50, 100, 150, 200]
ability_2_costs = [50, 100, 150, 200, 250]
ability_3_costs = [50, 100, 150, 200]
ability_4_costs = 500
ability_5_costs = 1000
while True:
    
    effective_range = int(current_range * (1 - ability_2 * 0.05))
    secret = random.randint(1, effective_range)
    ability_5_active = False
        
    eliminated = []
    while len(eliminated) < ability_3 * 5:
        num = random.randint(1, current_range)
        if num != secret and num not in eliminated:
            eliminated.append(num)
    print(f"Eliminated numbers: {sorted(eliminated)}")

# Ability 5 code
    while True:
        ans = input("type 5 if you want to use active ability 5\nType 0 to proceed\n program will auot proceed if no skill points available")
        if ans == "5" and ability_5 > 0:
            if secret > current_range//2:
                ability_5_active = True
                print(f"Numbers from 0 to {current_range//2} are elimiated!")
                break
            
            else:
                ability_5_active = True
                print(f"Numbers from {current_range//2} to {current_range} are eliminated!")
                break
        
        elif ability_5 == 0:
            print("No skill points available...\n")
            break

        else:
            print("proceeding...\n")
            break

    if ability_5_active:
        effective_range = current_range // 2
    else:
        effective_range = effective_range
    
#Pregame, asking question, wager, etc.
    print(f"I'm thinking of a number between 1 and {effective_range}!")
    attempts = 0
    your_guess = int(input("How many attempts do you think it would take you to guess it?\nAttempts:"))
    
    while True:
        wager_input = (input("How many points do you wanna wager on this next game? \n Points wagered: "))
        if wager_input == "ALL IN":
            wager = points
        else:
            wager = int(wager_input)
        if wager <= points:
            break
        elif wager == "ALL IN":
            wager = points
        else:
            wager > points
            print("Cant wager more than you got, try again!")

# THe main game loop, contains ability 4
    while True:
        guess_input = input("Your Guess:")
        if guess_input == "A4" :
            if ability_4 > 0 :
                if attempts <= your_guess//2 :
                    wager = wager * 2
                    ability_4_active = True
                else:
                    print("Cant use the ability, too late!")
            else:
                print("You dont have the ability!")
            continue
        guess = int(guess_input)
        attempts += 1
        
        if guess < secret:
             print("Too low!")

        elif guess > secret:
             print("Too high!")

        else: 
             print(f"You got it in {attempts} attempts!") 
             break
        
        if attempts > your_guess:
            print("Thats one too many attempts!")
            break
         
# Game Result, points given/taken, multiplier, etc.
    if attempts == your_guess:
        multiplier = 1 + (0.5*streak)
        points += int(2 * wager * (1 + ability_1 * 0.05) * multiplier)
        streak += 1
        current_range += 100
        print(f"Jackpot streak: {streak} | Multiplier: {multiplier} | Next Range: {current_range}")

        print ("JACKPOTTT, you guessed it perfectly dawg"f"\n Your current points are: {points}")

    elif attempts == your_guess - 1:

        multiplier = 1
        current_range = 100
        print ("So close!"f"\n Your Current points are: {points}")
        print(f"Jackpot streak: {streak} | Multiplier: {multiplier} | Next Range: {current_range}")


    else:
        points -= wager
        streak = 0
        multiplier = 1
        current_range = 100
        if points == 0:
            print ("YA LOST DUMMY")
            time.sleep(2)
            sys.exit()
        else:
            print("Dumbass, "f"Your currents points are {points}")
            print(f"Jackpot streak: {streak} | Multiplier: {multiplier} | Next Range: {current_range}")

        
    if streak == 10:
        print("YOU WIN THE GAME!")
        # ending sequence here
        break

# SHOP SYSTEM (BIG CODE)
    if points > 0:
        while True:

            print(f"Shop's Open! \n You have {points} points \nAbilites: \nAbility 1: {ability_1} (${ability_1_costs[ability_1] if ability_1 <= 3 else "MAX"}) \nAbility 2: {ability_2} (${ability_2_costs[ability_2] if ability_2 <= 4 else "MAX"}) \nAbility 3: {ability_3} (${ability_3_costs[ability_3] if ability_3 <= 3 else "MAX"}) \nAbility 4: {ability_4} (${ability_4_costs if ability_4 == 0 else "MAX"}) \nAbility 5: {ability_5} (${ability_5_costs if ability_5 == 0 else "MAX"})")
            choice = int(input("WHat do you want to do? \n type ""ability number"" (1 ,2, 3 or 4) to buy skill point \n type ""0"" to exit the shop: \n"))
            if choice == 1:

                if ability_1_costs[ability_1]>points:
                    print("Cant afford it yet!")
                elif ability_1 >= 4:
                    print("Skill points are maxxed out for this ability!")
                else:
                    #Viable to buy
                    points = points - ability_1_costs[ability_1]
                    ability_1 += 1

            elif choice == 2:
                if ability_2_costs[ability_2]>points:
                    print("Cant afford it yet!")
                elif ability_2 >= 5:
                    print("Skill points are maxxed out for this ability!")
                else:
                    #Viable to buy
                    points = points - ability_2_costs[ability_2]
                    ability_2 += 1

            elif choice == 3:
                if ability_3_costs[ability_3]>points:
                    print("Cant afford it yet!")
                elif ability_3 >= 4:
                    print("Skill points are maxxed out for this ability!")
                else:
                    #Viable to buy
                    points = points - ability_3_costs[ability_3]
                    ability_3 += 1

            elif choice == 4:
                if ability_4_costs > points:
                    print("Can't afford this yet!")
                elif ability_4 > 0:
                    print("Cant store more than 1 Skill point")
                else:
                    points = points - ability_4_costs
                    ability_4 += 1

            elif choice == 5:
                if ability_5_costs > points:
                    print("Can't afford this yet!")
                elif ability_5 > 0:
                    print("Cant store more than 1 Skill point")
                else:
                    points = points - ability_5_costs
                    ability_5 += 1

            else:
                break
        
    else:
        print("Game Over")
        break
    
            