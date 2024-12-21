#!/usr/bin/env python3

#mad Lips generator

#code to prompt the user
adjective_weather = input("Enter an adjective to describe the weather: ")
adjective_animal1 = input("Enter another adjective to describe a monkey: ")
adjective_animal2 = input("Enter an adjective to describe the lion: ")
adjective_experience = input("Enter an adjective to describe the experience: ")


#conditional variation
animal_choice = input("Enter your favorite animal (e.g., monkey, tiger, elephant): ")

if animal_choice.lower() == "monkey":
    animal_description = "swinging from the trees"
elif animal_choice.lower() == "elephant":
    animal_description = "trumpeting loudly"
else:
    animal_description = "doing something unique"

# Buil the story
story = f"""
On a beautiful {adjective_weather} day, I went to the zoo. 
I saw a funny {adjective_animal1} monkey {animal_description} from the trees. 
Then, I spotted a majestic {adjective_animal2} lion lounging in the sun. 
What a wild and {adjective_experience} experience!
"""

#outputing the story based on response given
print("\nHere’s your Mad Libs Story:\n")
print(story)