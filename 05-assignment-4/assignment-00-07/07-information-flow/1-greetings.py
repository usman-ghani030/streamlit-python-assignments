def greet(name):
    """Prints a greeting with the given name."""
    print(f"Greetings {name}!")

def main():  
    name = input("What's your name? ")
    
    greet(name)

if __name__ == '__main__':
    main()