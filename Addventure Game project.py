import time
import random

def adv_game():
    def print_pause(*messages):
        for message in messages:
            print(message)
            time.sleep(2)

    def road_block(total_score):
        # code for loss
        print_pause("You have killed the wicked fairy")
        total_score += 15
        print_pause("Your current score is:", total_score)
        return total_score

    def knock_on_door(total_score):
        # code for knocking on the door
        print_pause("You knock on the door.")
        print_pause("The wicked fairy steps out")
        print_pause("Your current score is:", total_score)

        while True:
            choice = input("Do you want to cast a spell (2) or run away (1): ")
            if choice == "2":
                total_score = road_block(total_score)
                break
            elif choice == "1":
                print_pause("You have turned into a frog")
                total_score -= 10
                print("Your current score is:", total_score)
                break
            else:
                print("Invalid input! Please enter (1) or (2)")          

        return total_score

    def enter_cave(total_score):
        # code for entering the cave
        print_pause("You have entered the cave.")
        print_pause("Your current score is:", total_score)
        # add random rewards
        rewards = ["a health potion", "10 gold bars", "The wand of ogorth"]
        reward = random.choice(rewards)
        print_pause(f"You have found {reward}!")
        total_score += 15
        print("Your current score is:", total_score)
        print_pause("You returned to the field")
        return total_score

    print_pause("You find yourself standing in an open field, filled with grass",
                "and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairy is somewhere around here,",
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand, you hold your trusty (but not very effective)",
                "magic wand.")
    total_score = 0

    while True:
        choice = input("Do you want to knock on the door (1) or enter the cave (2): ")
        if choice == "1":
            total_score = knock_on_door(total_score)
            break
        elif choice == "2":
            total_score = enter_cave(total_score)
            break
        else:
            print("Invalid input! Please enter (1) or (2)")

    if total_score >= 10:
        print("Congrats! You have won the game")
    elif total_score < 0:
        print("Game over! You have lost")

    while True:
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y":
            adv_game()
            break
        elif play_again == "n":
            print("Thank you for playing DECI Adventure game!")
            break
        else:
            print("Invalid input! Please enter (y) or (n)")

adv_game()