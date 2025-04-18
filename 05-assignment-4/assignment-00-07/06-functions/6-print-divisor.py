def print_divisors(num):
    # Loop from 1 to num (inclusive) to find divisors
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=' ')  # Print each divisor on the same line
    print()  # Print a newline after all divisors

def main():
    # Get user input
    num = int(input("Enter a number: "))
    print(f"Here are the divisors of {num}")
    print_divisors(num)

if __name__ == '__main__':
    main()