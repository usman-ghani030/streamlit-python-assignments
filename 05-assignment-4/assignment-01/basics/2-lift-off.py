# def main():
#     for i in range(10, 0, -1): 
#         print(i, end=" ")  
    
#     print("Liftoff!")

# if __name__ == '__main__':
#     main()



import time

def main():   
    for i in range(10, 0, -1): 
        print(i, end=" ", flush=True)  
        time.sleep(1)  # 1 second gap
    
    print("Liftoff!")

if __name__ == '__main__':
    main()

# flush =True forces the output to be printed immediately, without buffering. It means print every value after every one second.
# else it will print all the values at once all together after 10 seconds. 
