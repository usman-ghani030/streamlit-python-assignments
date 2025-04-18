import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Time's up!")


t = int(input("Enter the time in seconds: "))
countdown(t)
# This code implements a countdown timer in Python. It takes an input time in seconds and counts down to zero, displaying the time remaining in MM:SS format. When the countdown reaches zero, it prints "Time's up!".    
    