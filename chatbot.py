import random

#intro text and intial request for user input
print("\nHello, I\'m a chat bot for Johnny!\nYou can tell me a video game genre and I\'ll tell you a game Johnny plays in that genre!\nType \'done\' to exit out")
user_input = input("Name a video game genre: \n")

#global variable to check if user response matches any lists
plays_Game = False

#lists of games based on genre
RPG = ["Fallout", "Skyrim, one of his favorites", "Dishonored"]

shooter = ["Arma", "Call Of Duty", "Halo, one of his favorites", "Battlefield", "Valorant"]

horror = ["Outlast", "Alien: Isolation, one of his favorites"]

strategy = ["Total War, one of his favorites ", "XCOM", "Leage Of Legends","Chess"]

cards = ["Poker, one of his favorites", "Solitare"]

arcade = ["Fall Guys", "Clone Drone in the Danger Zone, one of his favorites"]

#receives user input, checks to see if input matches any genres, and returns response based on input
def get_bot_response(user_response):
    global plays_Game
    user_response = user_response.lower()
    if user_response == "rpg":
        plays_Game = True
        return  random.choice(RPG)
    elif "shooter" == user_response or "fps" == user_response:
        plays_Game = True
        return random.choice(shooter)
    elif "horror" == user_response:
        plays_Game = True
        return random.choice(horror)
    elif "strategy" == user_response:
        plays_Game = True
        return random.choice(strategy)
    elif "cards" == user_response:
        plays_Game = True
        return random.choice(cards)
    elif "arcade" == user_response:
        plays_Game = True
        return  random.choice(arcade)
    elif plays_Game is False:
        print(f"\n* Johnny doesn't play {user_response} *\n")

#loop to repeatedly ask user for input and prints response from get_bot_response
while user_input.lower() != "done":
    game = get_bot_response(user_input)
    if plays_Game is True:
        print(f"\n* Johnny plays {game} *\n")
        plays_Game = False
    user_input = input("Type \'done\' to exit out\nName a video game genre: \n")

    