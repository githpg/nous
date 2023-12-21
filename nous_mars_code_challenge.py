def oreientation():
    N = bot_position_y + 1
    S = bot_position_y - 1
    E = bot_position_x + 1
    W = bot_position_x - 1


def left_turn(current_orient):
    if current_orient is "N":
        new_orient = "W"
    elif current_orient is "E":
        new_orient is "N"
    elif current_orient is "S":
        new_orient is "E"
    elif current_orient is "W":
        new_orient = "S"

    return new_orient


def right_turn(current_orient):
    if current_orient is "N":
        new_orient = "E"
    elif current_orient is "E":
        new_orient is "S"
    elif current_orient is "S":
        new_orient is "W"
    elif current_orient is "W":
        new_orient = "N"

    return new_orient


def move_forward(current_orient, bot_position_x, bot_position_y):
    if current_orient is "N":
        new_bot_position_y = bot_position_y + 1
    elif current_orient is "S":
        new_bot_position_y = bot_position_y - 1
    elif current_orient is "E":
        new_bot_position_x = bot_position_x + 1
    elif current_orient is "W":
        new_bot_position_x = bot_position_x - 1

    return new_bot_position_x, new_bot_position_y


def move_bot(bot_instructions, oriuentation, bot_position_x, bot_position_y):
    for move in bot_instructions:
        if move == "R":
            print("turning right")
        elif move == "L":
            print("turning left")
        elif move == "F":
            print("move forward")


def main():
    print("Enter the size of your planet")
    max_x, max_y = map(int, input().split())

    print(max_x, max_y)

    number_bot = "next"
    print(f"Enter the start coordinates of your {number_bot} bot")

    (
        bot_start_position_x,
        bot_start_position_y,
        bot_start_position_orient,
    ) = input().split()  # splits string into list

    print(bot_start_position_x, bot_start_position_y, bot_start_position_orient)

    print("what are your instructions?")
    bot_instructions = input().strip()  # removes leading + trailing white space

    print(bot_instructions)

    move_bot(bot_instructions)


if __name__ == "__main__":
    main()
