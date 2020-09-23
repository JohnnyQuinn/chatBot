import random

print("\nHello, I\'m a chat bot for Johnny!\nYou can tell me a video game genre and I\'ll tell you a game Johnny plays in that genre!\nType \'done\' to exit out")
user_input = input("Name a video game genre: \n")

plays_Game = False

#lists of games based on genre
RPG = ["Fallout", "Skyrim", "Dishonored"]

shooter = ["Arma", "Call Of Duty", "Halo", "Battlefield", "Valorant"]

horror = ["Outlast", "Alien: Isolation"]

strategy = ["Total War (my fav)", "XCOM", "Leage Of Legends"]

cards = ["Poker, I absolutely love poker!", "Solitare"]

arcade = ["Fall Guys", "Clone Drone in the Danger Zone"]

def get_bot_response(user_response):
    global plays_Game
    if user_response == "RPG":
        plays_Game = True
        return  random.choice(RPG)
    elif "shooter" == user_response or "FPS" == user_response:
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
        print(f"Johnny doesn't play {user_response}")

while user_input != "done":
    game = get_bot_response(user_input)
    if plays_Game is True:
        print(f"Johnny plays {game}")
        plays_Game = False
    user_input = input("Name a video game genre: \n")

    