#!/usr/bin/env python3

import random

secret_number = random.randint(1,10)



while True:
    secret_number = random.randint(1,10)
    print("/nAm thinking of a number between 1 and 10, can you guess?")


    guess = None
    guess_count = 0


    while guess != secret_number:
        try:
            guess = int(input("Enter your guess here: "))
            guess_count += 1

            match guess:
                case _ if  guess == secret_number:
                    print(f"Congratulations, you got it on count: {guess_count}")
                case _ if guess < secret_number:
                    print("The number you entered is lower, try again")
                case _ if guess > secret_number:
                    print("The number you entered is higher, try again")  

        except ValueError:
            print("Please input corect number in the range specified!")
            
    play_again = input("Do you want to play again(yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thank you for playing, Goodbye!")
        break
    else:
        secret_number = random.randint(1,10)




        
       
    




