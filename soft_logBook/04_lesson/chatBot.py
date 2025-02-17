#!/usr/bin/env python3

import random

def random_question():
        """Reaction for empty question"""
        question = input("")
        print('')

def key_words():
                """Specific words"""

                while True:

                        try:
                                question = input("Waiting for question: ")
                                print()

                                if "Hello" in question:
                                    print(f"Hello {name}, how are you today? ")
                                elif "books" in question:
                                    print(f"{name}, you will find all the books in the library")
                                elif "bus" in question:
                                    print(f"{name}, you will find the bus stop near the university, left hand side of the building")
                                elif "thank you" in question:
                                    print(f"Your welcome {name}, I am here to help! ")
                        except ValueError:
                                print("The problem is not identified")

def exit_the_program():
        """exit the program"""
        question = input("Is there anything else can I help you with? ")
        print()

        if "exit" in question:
                print(f"I am happy I could help you {name}, bye")
                exit()
        elif "quit" in question:
                print(f"I am happy I could help you {name}, bye")
                exit()
        elif "bye" in question:
                print(f"I am happy I could help you {name}, bye")
                exit()



if __name__ == "__main__":

        print("Welcome to the chatbot")
        name = input("What is your name? ")
        random_agent_name = ["William","Mary","Jack", "Ester"]
        agent_name = random.choice(random_agent_name)

        print(f"Hi,{name}!\n My name is {agent_name},\n How can I help you today?")

        key_words()
        random_question()

        print("Thank you, good bye! ")
        exit()