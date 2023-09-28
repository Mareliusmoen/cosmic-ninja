def start_y_or_n():
    """
    Ask player if they're ready to play, and adds input.

    This function prints the question to start the game and gives the player
    the different options they can input. Theres an input field and it returns
    the value to be used by the rest of the code.

    """
    return input(
        """Would you like to start your adventure? ENTER [yes / no]: >>  """)


def a_or_b():
    """
    Ask player if they would like to choose option 'a' or 'b', and adds input.

    This function prints the question of which option the player wants to go
    for and explains to the player the different options they can input.
    Theres an input field and it returnsthe value to be used by the rest
    of the code.
    """
    return input('What would you like to do? ENTER [a / b] >>  ')
    