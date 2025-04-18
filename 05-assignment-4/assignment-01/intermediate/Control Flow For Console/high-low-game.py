import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    #  keep track of score
    your_score = 0

    #  Play multiple rounds
    for i in range(NUM_ROUNDS):
        print("Round", i + 1)
        #  Generate the random numbers and print them out
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print("Your number is", your_num)

        # Get user input for their choice
        choice = input("Do you think your number is higher or lower than the computer's?: ")

        #  Make sure the player inputs a valid choice (higher or lower)
        while choice != "higher" and choice != "lower":
            choice = input("Please enter either higher or lower: ")

        # Map out all the ways to win the round
        higher_and_correct = choice == "higher" and your_num > computer_num
        lower_and_correct = choice == "lower" and your_num < computer_num

        if higher_and_correct or lower_and_correct:
            print("You were right! The computer's number was", computer_num)
            # keep track of your score
            your_score += 1 
        else: 
            print("Aww, that's incorrect. The computer's number was", computer_num)

        # keep track of your score
        print("Your score is now", your_score)
        print()
    
    # Conditional ending messages based on performance
    print("Your final score is", your_score)

    if your_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif your_score > NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
