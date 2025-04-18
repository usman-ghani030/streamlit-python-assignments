def is_leap_year(year):
                                   # Check if the year is divisible by 4
    if year % 4 == 0:
                                   # If year is divisible by 100, it must also be divisible by 400 to be a leap year
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


try:
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")
except ValueError:
    print("Please enter a valid integer year.")
