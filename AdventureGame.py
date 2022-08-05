# Viola Dube
# Places of Adventure Text game

print("Hello, Where would you like to go to the beach(b) or to the mountains(m)?")
place = input("What do you choose?:")
if place.lower() == 'b':
    print("Do you want to go for a swim? y or n")
    answer = input("What do you choose?:")
    if answer.lower() == 'y':
        print("You got stung by a jellyfish. You lose!")        
    else:
        print("Would you like to build a sandcastle (c), look for shells (s) or lay in the sun (l)")
        choice = input("What do you choose?:")
        if choice.lower() == 'c':
            print("You won a sandcastle contest and  you won the game!")
        elif choice.lower() == 's':
            print("It is high tide. No shells to be found. You lose!")
        else:
            print("You forgot sunscreen and got a sunburn. You lose!")
            
else:
    # mountains
    print("Do you want to go for a hike? y or n")
    response = input("What is your answer?:")
    if response.lower() == 'y':
        print("You forgot to bring a map and got lost. You lose!")
    else:
        print("Do you want to play a game? y or n")
        playGame = input("What is your answer?:")
        if playGame.lower() == 'y':
            print("Pick a color: blue, brown, or green")
            color = input("Type in your color choice:")
            if color.lower() == "blue":
                print("I spy something blue. Can you guess what it is?")
                guess = input("What is your guess?:")
                if guess.lower() == "sky":
                    print("You guessed corectly. You win!")
                else:
                    print("Wrong answer. I was thinking of the sky. You lose.")
            elif color.lower() == "green":
                print("I spy something green. Can you guess what it is?")
                guess = input("What is your guess?:")
                if guess.lower() == "grass":
                    print("You guessed correctly. You win!")
                else:
                    print("Wrong answer. I was thinking of grass. You lose.")
            else:
                print("I see a brown bear ready to attack. You lose!")
        else:
            print("You are bored and lost the game.")

print("Thanks for playing!")
