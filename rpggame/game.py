#!/usr/bin/python3

from pipeop import pipes
import sys

INSTRUCTIONS = {"commands": ["go [direction]", "get item"], "title": "RPG Game"}
STATUS = {
    "lines": "---------------------------",
    "room_update": "You are in the",
    "inventory_update": "Inventory:",
    "see_update": "You see a",
}
ROOMS = {
    "Hall": {"south": "Kitchen", "east": "Dining Room", "item": "key"},
    "Kitchen": {
        "north": "Hall",
        "item": "monster",
    },
    "Dining Room": {"west": "Hall", "south": "Garden", "item": "potion"},
    "Garden": {"north": "Dining Room"},
}

END_ROOM = "Garden"
END_ITEM = "potion"
VALID_MOVES = ["get item", "go north", "go east", "go south", "go west", "quit"]


@pipes
def start(play_data):
    if play_data.get("current_room") == END_ROOM and END_ITEM in play_data.get(
        "inventory"
    ):
        print(
            "You escaped the house with the ultra rare key and magic potion... YOU WIN!"
        )
    else:
        round_data = play_pipeline(play_data)
        start(round_data)


@pipes
def play_pipeline(play_data):
    return (
        play_data
        >> show_status
        >> get_move
        >> go_checker
        >> get_checker
        >> monster_checker
        >> print_round_data_for_go
        >> print_round_data_for_get
    )


def show_instructions():
    title = INSTRUCTIONS.get("title")
    command_direction = INSTRUCTIONS.get("commands")[0]
    command_item = INSTRUCTIONS.get("commands")[1]
    instructions_to_print = """
            {0}
            ========
            Commands:
        {1}
        {2}
        'quit' to exit
            """
    print(instructions_to_print.format(title, command_direction, command_item))


def show_status(play_data):
    STATUS_to_print = f"""
        {STATUS.get("lines")}
        {STATUS.get("room_update")} {play_data.get('current_room')}
        {STATUS.get("inventory_update")} {str(play_data.get('inventory'))}
        """
    if "item" in play_data:
        STATUS_to_print += f"""{STATUS.get("see_update")} {play_data.get('item')}
      """

    STATUS_to_print += f"""{STATUS.get("lines")}"""
    print(STATUS_to_print)
    return play_data


def get_move(play_data):
    move = ""
    while move not in VALID_MOVES:
        move = input("What is your move? ")
        move = move.lower()
    play_data["move"] = move.split(" ", 1)
    if move == "quit":
        sys.exit("Exiting game.")
    return play_data


def go_checker(play_data):
    command = play_data.get("move")[0]
    intention = play_data.get("move")[1]
    current_room = play_data.get("current_room")
    if command == "go":
        if intention in ROOMS.get(current_room):
            play_data["current_room"] = ROOMS.get(current_room).get(intention)
            play_data["room_move"] = True
        else:
            play_data["room_move"] = False
    return play_data


def get_checker(play_data):
    command = play_data.get("move")[0]
    current_room = play_data.get("current_room")
    if command == "get":
        if "item" in ROOMS.get(current_room):
            play_data.get("inventory").append(ROOMS.get(current_room).get("item"))
            del ROOMS[current_room]["item"]
            play_data["attain_item"] = True
        else:
            play_data["attain_item"] = False
    return play_data


def monster_checker(play_data):
    if play_data.get("attain_item"):
        last_item = play_data.get("inventory")[-1]
        if last_item == "monster":
            sys.exit("A monster has got you... GAME OVER!")
    return play_data


def print_round_data_for_go(play_data):
    if play_data.get("move")[0] == "go":
        current_room = play_data.get("current_room")
        if play_data.get("room_move"):
            print(f"You moved to {current_room}")
        else:
            print(f"You can't go that way!")
    return play_data


def print_round_data_for_get(play_data):
    if play_data.get("move")[0] == "get":
        last_item = play_data.get("inventory")[-1]
        if play_data.get("attain_item"):
            print(f"You obtained the item: {last_item}")
        else:
            print(f"You can't get {last_item}")

    return play_data


def debug(play_data):
    print(play_data)
    return play_data


def main():
    START_ROOM = "Hall"
    START_INVENTORY = []
    show_instructions()
    start({"current_room": START_ROOM, "inventory": START_INVENTORY})


if __name__ == "__main__":
    main()

