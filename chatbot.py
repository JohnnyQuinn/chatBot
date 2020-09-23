import random

print("\nHello, I\'m a chat bot for Johnny!\nYou can tell me a video game genre and I\'ll return a game Johnny plays in that genre!\nType \'done\' to exit out")
user_input = input("Name a video game genre: ")

#lists of games based on genre
RPG = ["Fallout", "Skyrim", "Dishonored"]

shooter = ["Arma", "Call Of Duty", "Halo", "Battlefield", "Valorant"]

horror = ["Outlast", "Alien: Isolation"]

strategy = ["Total War (my fav)", "XCOM", "Leage Of Legends"]

cards = ["Poker, I absolutely love poker!", "Solitare"]

arcade = ["Fall Guys", "Clone Drone in the Danger Zone"]

def get_bot_response(user_response):
    if "RPG" in user_response:
        rpg_Response = random.choice(RPG)
        return rpg_Response
    if "shooter" or "FPS" in user_response:
        return random.choice(shooter)

while user_input != "done":
    print(get_bot_response(user_input))
    user_input = input("Name a video game genre: ")
    