def move_bot(bot_instructions):
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
