# Text Adventure Game Starter Code

# Example room map
rooms = {
    "start": {
        "description": "You are in a dark room. A door leads north.",
        "north": "forest"
    },
    "forest": {
        "description": "You are in a forest. A path leads south and there is a glowing key nearby.",
        "south": "start",
        "item": "key"
    }
}

player_inventory = []
current_room = "start"


def show_room():
    room = rooms[current_room]
    print(room["description"])


# TODO: Add commands for movement, inventory, and item collection
# TODO: Add a win condition when the player finds the key and reaches the exit
# TODO: Add a loop to keep the game running until the player wins or quits

show_room()
