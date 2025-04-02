from termcolor import colored
from utils import choices_to_str

choices = ["sleep", "cheer", "dowork", "brush teeth"]
inventory = []

# The `colored` function prints out text in the color provided!
print(colored("Hello! Welcome to a boring adventure!", "green"))
print(colored("You are in a dark room. Choose one of the following:", "blue"))

# done is a "boolean variable" (i.e., either True or False)
# We use it to control when the `while` loop should end!
done = False
while not done:
    # `choices_to_str` is a function we wrote to turn a choices
    # list into a string where each choice is underlined.  If you
    # want to check it out, it's in `utils.py` on the left!
    prompt = choices_to_str(choices)
    action = input(prompt + " >>> ")
    if action == "sleep" and "work" and "brush teeth" in inventory:
        print(colored("ZZZZ...zzzz", "blue"))
        done = True
    elif action == "sleep":
        print(colored(
            "You still have work to do! plus, your breath is kinda stinky...", "red"))
    elif action == "dowork":
        inventory.append("work")
        print(colored("You're done with your work now! Get ready for bed", "green"))
    elif action == "cheer":
        print("Hip hip hooray!! You're still tired!")
    elif action == "brush teeth":
        inventory.append("brush teeth") #make sure to append brush teeth to inventory
        print("Nice job hygiene boss! Time for bed")

print(colored("The adventure is over!", "green"))
