from termcolor import colored
from utils import choices_to_str

activities = ["Attend class", "Pick your wand",
              "Chat with fellow peers", "Meet Prof. Dumbledore", "Use the washroom", "Go to dorm room"]
houses = ["serpent", "lion",
          "badger", "eagle"]
suspects = ["Adris", "Peter", "Luna", "Sylvia"]
inventory = []

print(colored(
    "Welcome to Hogwarts! Let's get you settled down... ", "light_cyan"))
print(colored("Fellow Wizard, what is your name?", "light_cyan"))
mname = input()
print(colored("Oh that is rather muggle-blood sounding... choose something more wizardy: ", "light_cyan"))
name = input()
print(colored("Lovely to meet you, "+name.title() +
      ". My name is Adris, Head Boy [click enter to cont.]", "light_cyan"))
input()
print(colored(
    "We have quite the itinerary today...classes, dorms, OH! And your house! Let's take you to the sorting hat, shall we? [click enter to cont.]", "light_cyan"))
input()
print(colored("Hello my dear, I am the Sorting Hat. Now, can you please think of an animal?", "light_magenta"))

done = False
while not done:
    prompt = choices_to_str(houses)
    action = input(prompt + " >>> ")
    if action == "serpent":
        inventory.append("serpent")
        print(colored("HOUSE OF SLYTHERIN! [click enter to cont.]", "green"))
    if action == "eagle":
        inventory.append("eagle")
        print(colored("HOUSE OF RAVENCLAW! [click enter to cont.]", "blue"))
    if action == "lion":
        inventory.append("lion")
        print(colored("HOUSE OF GRYFFINDOR! [click enter to cont.]", "red"))
    if action == "badger":
        inventory.append("badger")
        print(colored("HOUSE OF HUFFLEPUFF! [click enter to cont.]", "yellow"))
    if action == "lion" or "serpent" or "badger" or "eagle" in inventory:
        input()
        print(colored("You will do well in your house, "+name.title() +
              " but take caution, there is something uncertain about your partner there... \nGood luck! [click enter to cont.]", "magenta"))
        done = True
input()
print(colored(
    "Hey first-year! Congrats on your choice. I have to take something to Prof. Moody, but follow this map and you will be in safe hands! Later! [click enter to open map]", "light_cyan"))
input()

done = False
while not done:
    prompt = choices_to_str(activities)
    action = input(prompt + " >>> ")
    if action == "Pick your wand":
        inventory.append("Pick your wand")
        print(colored(
            "Wand 303: Holly wood with a dragon scale should do it for you! [click enter to cont.]", "green"))
        input()
    if action == "Attend class":
        inventory.append("Attend class")
        print(colored("Professor! The 'pebble' as you wish", "light_green"))
        print(colored("Shush boy! I smell someone is listening to us...", "red"))
        print(colored("[click enter to leave!]", "white"))
        input()
    if action == "Chat with fellow peers":
        inventory.append("Chat with fellow peers")
        print(colored("Hi there! My name is Luna", "light_blue"))
        print(colored("Nice to meet you! I'm Sylvia", "yellow"))
        print(colored(
            "And my name is Peter. I'm not sure if you heard, but someone has stolen the philospher's stone! I heard Prof. McGonagall whispering to herself about being moody and petty... [click enter to keep chatting]", "light_green"))
        input()
        print(colored("That's horrible! Who would do such a thing? I wonder what being moody and petty means...", "yellow"))
        print(colored(
            "I know right! Um, Peter, what is that white dust on your hair?", "light_blue"))
        print(colored(
            "Huh? Oh, I must have bumped into one of Prof. Moody's cupboards this morning. Speaking of which, I'm supposed to meet him now! I'll see you two later! [click enter to cont.]", "light_green"))
        input()
    if action == "Meet Prof. Dumbledore":
        inventory.append("Meet Prof. Dumbledore")
        print(colored("Ahhh, "+name.title() +
              " I have been waiting for you. Someone has stolen something very important of mine, I trust you to find out who it is and let me know...[click enter to cont.]", "blue"))
        input()
    if action == "Use the washroom":
        inventory.append("Use the washroom")
        print(
            colored("HELPPP! HERE! [click enter to open stall door] ", "light_cyan"))
        input()
        print(colored(
            "Oh thank goodness you found me! I'm Adris. Someone locked me in here this morning! And I can't believe I'm saying this, but he looked like my twin! [click enter to cont.]", "light_cyan"))
        input()
    if action == "Go to dorm room":
        inventory.append("Go to dorm room")
        print(colored(
            "Book of potions: Ch 6 Polyjuice Potion -- \n Recipe: Crushed unicorn horns, rat skulls, diamond pearls [click enter to cont.]", "red"))
        input()
        # print(inventory)
    if action == "Pick your wand" and "Chat with fellow peers" and "Meet Prof. Dumbledore" and "Attend class" and "Use the washroom" and "Go to dorm room" in inventory:
        print(colored("We meet again "+name.title() +
              ". Can you please let me know who stole the philospher's stone?", "blue"))
        done = True

done = False
while not done:
    prompt = choices_to_str(suspects)
    action = input(prompt + " >>> ")
    if action == "Peter":
        print(colored("Well done, "+name.title() +
                      " I trust that Hogwarts will be safe during your time here... Until next time!", "blue"))
        done = True
    else:
        print(colored(
            "I'm afraid you have been mistaken. The thief is still on the loose...", "blue"))
        done = True
