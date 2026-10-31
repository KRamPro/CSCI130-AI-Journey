# Name: K
# Date: October 30, 2026
# A tiny reflex agent: it uses fixed rules, not learning or reasoning.

from datetime import datetime


def main():
    hour = datetime.now().hour

    if hour < 12:
        time_of_day = "morning"
    elif hour < 18:
        time_of_day = "afternoon"
    else:
        time_of_day = "evening"

    print(f"Hello! It is {time_of_day}.")
    message = input("How are you feeling today? ").lower()

    if "happy" in message:
        print("I'm glad you're feeling happy!")
    elif "sad" in message:
        print("I'm sorry you're feeling sad. I hope your day gets better.")
    elif "excited" in message:
        print("That's exciting! I hope it goes well.")
    else:
        print("Thanks for telling me.")

    print("I hope these Interesting AI facts make you smile!")
    print("AI fact: AI systems can recognize patterns in data.")
    print("AI fact: Some AI systems can understand or generate language.")
    print("AI fact: A reflex agent follows rules based on what it observes.")


if __name__ == "__main__":
    main()
