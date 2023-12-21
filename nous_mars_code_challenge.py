def right_turn(current_orient):
    if current_orient == "N":
        new_orient = "E"
    elif current_orient == "E":
        new_orient = "S"
    elif current_orient == "S":
        new_orient = "W"
    elif current_orient == "W":
        new_orient = "N"

    return new_orient


def left_turn(current_orient):
    if current_orient == "N":
        new_orient = "W"
    elif current_orient == "E":
        new_orient = "N"
    elif current_orient == "S":
        new_orient = "E"
    elif current_orient == "W":
        new_orient = "S"

    return new_orient


def where_is_move_forward(current_orient, bot_position_x, bot_position_y):
    new_bot_position_x = bot_position_x
    new_bot_position_y = bot_position_y

    if current_orient == "N":
        new_bot_position_y = bot_position_y + 1
    elif current_orient == "S":
        new_bot_position_y = bot_position_y - 1
    elif current_orient == "E":
        new_bot_position_x = bot_position_x + 1
    elif current_orient == "W":
        new_bot_position_x = bot_position_x - 1

    return new_bot_position_x, new_bot_position_y


def move_forward(current_orient, bot_position_x, bot_position_y, max_x, max_y):
    new_bot_position_x, new_bot_position_y = where_is_move_forward(
        current_orient, bot_position_x, bot_position_y
    )

    if (
        new_bot_position_x > max_x
        or bot_position_x < 0
        or new_bot_position_y > max_y
        or bot_position_y < 0
    ):
        bot_lost = True
        bot_position_x = bot_position_x
        bot_position_y = bot_position_y

    else:
        bot_lost = False
        bot_position_x = new_bot_position_x
        bot_position_y = new_bot_position_y

    return bot_position_x, bot_position_y, bot_lost


def move_bot(
    bot_instructions,
    current_orient,
    bot_position_x,
    bot_position_y,
    max_x,
    max_y,
    death_coordinates,
):
    for move in bot_instructions:
        print(
            f"current positions: x = {bot_position_x} and  y = {bot_position_y} and orientation = {current_orient}"
        )
        if move == "R":
            print("turn right")
            current_orient = right_turn(current_orient)
        elif move == "L":
            print("turn left")
            current_orient = left_turn(current_orient)
        elif move == "F":
            print("move forward")
            bot_position_x, bot_position_y, bot_lost = move_forward(
                current_orient,
                bot_position_x,
                bot_position_y,
                max_x,
                max_y,
            )
            if bot_lost == True:
                print(bot_position_x, bot_position_y)
                if (bot_position_x, bot_position_y) in death_coordinates:
                    continue

                elif (bot_position_x, bot_position_y) not in death_coordinates:
                    print("bot lost")

                    new_death_coordinates = (bot_position_x, bot_position_y)

                    death_coordinates.append(new_death_coordinates)

                    print(f"new death coordinates are: {death_coordinates}")

                    break

    return bot_position_x, bot_position_y, current_orient, bot_lost


def bot_info_input(bot_number, max_x, max_y, death_coordinates):
    if bot_number == 1:
        first_or_next = "first"
    elif bot_number >= 2:
        first_or_next = "next"

    print(f"Enter the start coordinates of your {first_or_next} bot")

    (
        start_position_x,
        start_position_y,
        start_position_orient,
    ) = input().split()  # splits string into

    start_position_x = int(start_position_x)
    start_position_y = int(start_position_y)

    if (
        start_position_x > max_x
        or start_position_x < 0
        or start_position_y > max_y
        or start_position_y < 0
    ):
        bot_lost = True
    else:
        bot_lost = False

    print("what are your instructions?")
    bot_instructions = input().strip()  # removes leading + trailing white space

    current_orient = start_position_orient
    bot_position_x = int(start_position_x)
    bot_position_y = int(start_position_y)
    bot_position_x, bot_position_y, current_orient, bot_lost = move_bot(
        bot_instructions,
        current_orient,
        bot_position_x,
        bot_position_y,
        max_x,
        max_y,
        death_coordinates,
    )

    if bot_lost:
        bot_lost = "LOST"
    else:
        bot_lost = ""

    print(bot_position_x, bot_position_y, current_orient, bot_lost)


def main():
    death_coordinates = []
    print("Enter the size of your planet")
    max_x, max_y = map(int, input().split())

    print(max_x, max_y)

    bot_number = 1

    bot_info_input(bot_number, max_x, max_y, death_coordinates)

    while True:
        print("Do you have another bot? Y/N")
        more_bots = input().upper()
        if more_bots == "Y":
            bot_number += 1
            bot_info_input(bot_number, max_x, max_y, death_coordinates)
        elif more_bots == "N":
            print("Thanks for playing")
            break


if __name__ == "__main__":
    main()
