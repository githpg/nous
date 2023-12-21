death_squares = [()]


def right_turn(current_orient):
    if current_orient == "N":
        current_orient = "E"
    elif current_orient == "E":
        current_orient == "S"
    elif current_orient == "S":
        current_orient == "W"
    elif current_orient == "W":
        current_orient = "N"

    return current_orient


def left_turn(current_orient):
    if current_orient == "N":
        current_orient = "W"
    elif current_orient == "E":
        current_orient == "N"
    elif current_orient == "S":
        current_orient == "E"
    elif current_orient == "W":
        current_orient = "S"

    return current_orient


def move_forward_1(current_orient, bot_position_x, bot_position_y):
    if current_orient == "N":
        new_bot_position_y = bot_position_y + 1
        new_bot_position_x = bot_position_x
    elif current_orient == "S":
        new_bot_position_y = bot_position_y - 1
        new_bot_position_x = bot_position_x
    elif current_orient == "E":
        new_bot_position_x = bot_position_x + 1
        new_bot_position_y = bot_position_y
    elif current_orient == "W":
        new_bot_position_x = bot_position_x - 1
        new_bot_position_y = bot_position_y

    return new_bot_position_x, new_bot_position_y


def move_forward(current_orient, bot_position_x, bot_position_y):
    if current_orient == "N":
        bot_position_y = bot_position_y + 1
    elif current_orient == "S":
        bot_position_y = bot_position_y - 1
    elif current_orient == "E":
        bot_position_x = bot_position_x + 1
    elif current_orient == "W":
        bot_position_x = bot_position_x - 1

    return bot_position_x, bot_position_y


def move_bot(bot_instructions, current_orient, bot_position_x, bot_position_y):
    for move in bot_instructions:
        if move == "R":
            print("move right")
            right_turn(current_orient)
        elif move == "L":
            print("move left")
            left_turn(current_orient)
        elif move == "F":
            print("move forward")
            move_forward(current_orient, bot_position_x, bot_position_y)

    return bot_position_x, bot_position_y, current_orient


def bot_info_input(bot_number, max_x, max_y):
    if bot_number == 1:
        first_or_next = "first"
    elif bot_number >= 2:
        first_or_next = "next"

    print(f"Enter the start coordinates of your {first_or_next} bot")

    (
        start_position_x,
        start_position_y,
        start_position_orient,
    ) = input().split()  # splits string into l==t

    print("what are your instructions?")
    bot_instructions = input().strip()  # removes leading + trailing white space

    current_orient = start_position_orient
    bot_position_x = int(start_position_x)
    bot_position_y = int(start_position_y)

    current_orient, bot_position_x, bot_position_y = move_bot(
        bot_instructions, current_orient, bot_position_x, bot_position_y
    )

    print(bot_position_x, bot_position_y, current_orient)


def main():
    print("Enter the size of your planet")
    max_x, max_y = map(int, input().split())

    print(max_x, max_y)

    bot_number = 1

    bot_info_input(bot_number, max_x, max_y)

    print("Do you have another bot? Y/N")
    more_bots = input().upper()
    if more_bots == "Y":
        bot_number + 1
        bot_info_input(bot_number, max_x, max_y)
    elif more_bots == "N":
        print("Thanks for playing")


if __name__ == "__main__":
    main()
