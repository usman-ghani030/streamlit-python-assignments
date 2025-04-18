import random

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

words = ( "alligator",  "ant",  "ape", "armadillo", "baboon", "bat", "bear",  "bee", "bison", "boar", "buffalo", "butterfly", "camel",  "cat", "caterpillar", "cattle", "cheetah", "chicken", "chimpanzee",  "cobra", "cockroach",  "crab", "crane", "crocodile", "crow",  "deer", "dinosaur", "dog", "dogfish", "dolphin", "donkey", "dragonfly", "duck","eagle",  "eel", "elephant",  "falcon",  "fish",  "fox", "frog", "giraffe", "goat", "goldfish", "gorilla", "grasshopper", "hawk",  "hippopotamus", "horse", "human", "hummingbird", "hyena", "jackal", "jaguar", "jellyfish", "kangaroo", "kingfisher", "koala", "leopard", "lion", "lobster",  "mongoose", "monkey", "mosquito", "mouse", "octopus", "ostrich",  "owl",  "panda", "panther", "parrot", "partridge", "penguin",  "pig", "pigeon", "polar-bear",  "quail", "rabbit", "raccoon", "rat", "red-deer", "reindeer", "rhinoceros", "salamander", "salmon", "sand-dollar", "sandpiper", "scorpion", "seahorse", "seal", "shark", "sheep",  "snail", "snake", "sparrow", "spider", "squid",   "tiger", "toad",  "turkey", "turtle", "viper", "whale", "wildcat", "wolf", "wolverine",  "worm",  "yak", "zebra")



def display_man(wrong_guesses):
    print("**********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False

if __name__ == "__main__":
    main()

