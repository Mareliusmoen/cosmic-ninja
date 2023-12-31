"""
    This file containes the code that will run the game in the output
    terminal.

    This file contains all the imports from other libraries and files, as well
    as base functions and variables to be used in all the base code, and
    off course the base code for the game itself.

"""
# All imports for the app
import os
import platform
import welcome_text
import chapter1
import chapter2
import chapter3
import chapter4
import chapter5
import wrong_input
import queries


# make sure it clears on all operating systems
def clear():
    """
    Clear the terminal.

    This function provides a cross-platform
    way to clear the screen based on the operating system. On Windows,
    it uses the correct 'cls', while on any other systems, it uses 'clear'.

    Note:
    I have imported the 'os and 'platform library that this function need.

    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


# to make sure that any way of writing your answer is accepted
ANSWER_A = ["a", "A"]
ANSWER_B = ["b", "B"]
ANSWER_YES = ["y", "Y", "YES", "yes", "Yes", "YEs", "yES"]
ANSWER_NO = ["n", "N", "NO", "no", "No", "nO"]
# to style the console output
NEW_LINE = '\n'


def main():
    """
    Defines the function that contains the entire game.

    This function runs the whole game and calls the correct chapter based
    on the players choice.

    Note:
    For this function function to work properly, all chapters and text strings.
    needs to be import from the different .py files.
    """
    # game start
    welcome_text.welcome_logo()
    print(NEW_LINE)
    welcome_answer = \
        input("""
    If you want the full immersive ninja-life experience, hit play above this
    terminal to play a absolute classic ninja-fighter-theme-song.
    HAAIIIYYYYAA!!!

    Would you like to read more about why I made this app ENTER [a]
    Would you instead become the lethal ninja living deep inside you ENTER [b]
    >>  """)
    while True:  # welcome page with logo
        if welcome_answer in ANSWER_A:
            clear()
            welcome_text.backstory()
            print(NEW_LINE)
            backstory_answer = \
                input('Are you ready to play the game? ENTER [y]')
            while True:  # backstory loop
                if backstory_answer in ANSWER_YES:
                    break  # exit backstory loop
                else:
                    wrong_input.wrng_input2()
                    backstory_answer = input(
                        'Are you ready to play the game? ENTER [y]')
            break  # exit welcome page/logo loop
        elif welcome_answer in ANSWER_B:
            clear()
            break  # exit welcome page/logo loop
        else:
            wrong_input.wrng_input1()
            welcome_answer = input("""
    Would you like to read more about why I made this app ENTER [a],
    would you instead become the lethal ninja living deep inside you ENTER [b]
    >>  """)
    clear()
    welcome_text.introduction()
    while True:  # name-input loop
        name = input('ENTER YOUR NINJA NAME >>  ')
        if name.strip():
            break  # exit name-input loop
        else:
            wrong_input.wrng_name()
    clear()
    welcome_text.start_message(name)
    print(NEW_LINE)
    first_answer = queries.start_y_or_n()

    # game loop
    while True:
        if first_answer in ANSWER_YES:
            clear()
            chapter1.chapter1()
            chapter1.chapter1_option_a()
            chapter1.chapter1_option_b()
            print(NEW_LINE)
            chapter1_answer = queries.a_or_b()
            while True:  # loop for the choice in chapter 1
                if chapter1_answer in ANSWER_A:
                    clear()
                    chapter2.chapter2a()
                    chapter2.chapter2a_option_a()
                    chapter2.chapter2a_option_b()
                    print(NEW_LINE)
                    chapter2a_answer = queries.a_or_b()
                    while True:  # loop for chapter 2a
                        if chapter2a_answer in ANSWER_A:
                            clear()
                            chapter3.chapter3aa()
                            chapter3.chapter3aa_option_a()
                            chapter3.chapter3aa_option_b()
                            print(NEW_LINE)
                            chapter3aa_answer = queries.a_or_b()
                            while True:  # loop for chapter 3aa
                                if chapter3aa_answer in ANSWER_A:
                                    clear()
                                    chapter4.chapter4aaa()
                                    chapter4.chapter4aaa_option_a()
                                    chapter4.chapter4aaa_option_b()
                                    print(NEW_LINE)
                                    chapter4aaa_answer = queries.a_or_b()
                                    while True:  # loop for chapter 4aaa
                                        if chapter4aaa_answer in ANSWER_A:
                                            clear()
                                            chapter5.chapter5aaaa()
                                            print(NEW_LINE)
                                            # exit the loop for chapter 4aaa
                                            break
                                        elif chapter4aaa_answer in ANSWER_B:
                                            clear()
                                            chapter5.chapter5aaab()
                                            print(NEW_LINE)
                                            # exit the loop for chapter 4aaa
                                            break
                                        else:
                                            clear()
                                            chapter4.chapter4aaa()
                                            chapter4.chapter4aaa_option_a()
                                            chapter4.chapter4aaa_option_b()
                                            print(NEW_LINE)
                                            wrong_input.wrng_input5()
                                            chapter4aaa_answer = \
                                                queries.a_or_b()

                                    break  # exit the loop for chapter 3aa
                                elif chapter3aa_answer in ANSWER_B:
                                    clear()
                                    chapter4.chapter4aab()
                                    chapter4.chapter4aab_option_a()
                                    chapter4.chapter4aab_option_b()
                                    print(NEW_LINE)
                                    chapter4aab_answer = queries.a_or_b()
                                    while True:  # loop for chapter 4aab
                                        if chapter4aab_answer in ANSWER_A:
                                            clear()
                                            chapter5.chapter5aaba()
                                            print(NEW_LINE)
                                            # exit the loop for chapter 4aab
                                            break
                                        elif chapter4aab_answer in ANSWER_B:
                                            clear()
                                            chapter5.chapter5aabb()
                                            print(NEW_LINE)
                                            # exit the loop for chapter 4aab
                                            break
                                        else:
                                            clear()
                                            chapter4.chapter4aab()
                                            chapter4.chapter4aab_option_a()
                                            chapter4.chapter4aab_option_b()
                                            print(NEW_LINE)
                                            wrong_input.wrng_input3()
                                            chapter4aab_answer = \
                                                queries.a_or_b()

                                    break  # exit the loop for chapter 3aa
                                else:
                                    clear()
                                    chapter3.chapter3aa()
                                    chapter3.chapter3aa_option_a()
                                    chapter3.chapter3aa_option_b()
                                    print(NEW_LINE)
                                    wrong_input.wrng_input4()
                                    chapter3aa_answer = queries.a_or_b()
                            break  # exit the loop for chapter 2a
                        elif chapter2a_answer in ANSWER_B:
                            clear()
                            chapter3.chapter3ab()
                            chapter3.chapter3ab_option_a()
                            chapter3.chapter3ab_option_b()
                            print(NEW_LINE)
                            chapter3ab_answer = queries.a_or_b()
                            while True:  # loop for chapter 3ab
                                if chapter3ab_answer in ANSWER_A:
                                    clear()
                                    chapter4.chapter4aba()
                                    chapter4.chapter4aba_option_a()
                                    chapter4.chapter4aba_option_b()
                                    print(NEW_LINE)
                                    chapter4aba_answer = queries.a_or_b()
                                    while True:  # loop for chapter 4aba
                                        if chapter4aba_answer in ANSWER_A:
                                            clear()
                                            chapter5.chapter5abaa()
                                            print(NEW_LINE)
                                            # exit the loop for chapter 4aba
                                            break
                                        elif chapter4aba_answer in ANSWER_B:
                                            clear()
                                            chapter5.chapter5abab()
                                            print(NEW_LINE)
                                            # exit the loop for chapter 4aba
                                            break
                                        else:
                                            clear()
                                            chapter4.chapter4aba()
                                            chapter4.chapter4aba_option_a()
                                            chapter4.chapter4aba_option_b()
                                            print(NEW_LINE)
                                            wrong_input.wrng_input2()
                                            chapter4aba_answer = \
                                                queries.a_or_b()
                                    break  # exit the loop for chapter 3ab
                                elif chapter3ab_answer in ANSWER_B:
                                    clear()
                                    chapter4.chapter4abb()
                                    chapter4.chapter4abb_option_a()
                                    chapter4.chapter4abb_option_b()
                                    print(NEW_LINE)
                                    chapter4abb_answer = queries.a_or_b()
                                    while True:  # loop for chapter 4abb
                                        if chapter4abb_answer in ANSWER_A:
                                            clear()
                                            chapter5.chapter5abba()
                                            print(NEW_LINE)
                                            # exit the loop for chapter 4abb
                                            break
                                        elif chapter4abb_answer in ANSWER_B:
                                            clear()
                                            chapter5.chapter5abbb()
                                            print(NEW_LINE)
                                            # exit the loop for chapter 4abb
                                            break
                                        else:
                                            clear()
                                            chapter4.chapter4abb()
                                            chapter4.chapter4abb_option_a()
                                            chapter4.chapter4abb_option_b()
                                            print(NEW_LINE)
                                            wrong_input.wrng_input1()
                                            chapter4abb_answer = \
                                                queries.a_or_b()
                                    break  # exit the loop for chapter 3ab
                                else:
                                    clear()
                                    chapter3.chapter3ab()
                                    chapter3.chapter3ab_option_a()
                                    chapter3.chapter3ab_option_b()
                                    print(NEW_LINE)
                                    wrong_input.wrng_input3()
                                    chapter3ab_answer = queries.a_or_b()
                            break  # exit the loop for chapter 2a
                        else:
                            clear()
                            chapter2.chapter2a()
                            chapter2.chapter2a_option_a()
                            chapter2.chapter2a_option_b()
                            print(NEW_LINE)
                            wrong_input.wrng_input2()
                            chapter2a_answer = queries.a_or_b()
                    break  # exit the loop for chapter1
                elif chapter1_answer in ANSWER_B:
                    clear()
                    chapter2.chapter2b()
                    chapter2.chapter2b_option_a()
                    chapter2.chapter2b_option_b()
                    print(NEW_LINE)
                    chapter2b_answer = queries.a_or_b()
                    while True:  # loop for chapter 2b
                        if chapter2b_answer in ANSWER_A:
                            clear()
                            chapter3.chapter3ba()
                            chapter3.chapter3ba_option_a()
                            chapter3.chapter3ba_option_b()
                            print(NEW_LINE)
                            chapter3ba_answer = queries.a_or_b()
                            while True:  # loop for chapter 3ba
                                if chapter3ba_answer in ANSWER_A:
                                    clear()
                                    chapter4.chapter4baa()
                                    chapter4.chapter4baa_option_a()
                                    chapter4.chapter4baa_option_b()
                                    print(NEW_LINE)
                                    chapter4baa_answer = queries.a_or_b()
                                    while True:  # loop for chapter 4baa
                                        if chapter4baa_answer in ANSWER_A:
                                            clear()
                                            chapter5.chapter5baaa()
                                            print(NEW_LINE)
                                            # exit the loop for chapter 4baa
                                            break
                                        elif chapter4baa_answer in ANSWER_B:
                                            clear()
                                            chapter5.chapter5baab()
                                            print(NEW_LINE)
                                            # exit the loop for chapter 4baa
                                            break
                                        else:
                                            clear()
                                            chapter4.chapter4baa()
                                            chapter4.chapter4baa_option_a()
                                            chapter4.chapter4baa_option_b()
                                            print(NEW_LINE)
                                            wrong_input.wrng_input2()
                                            chapter4baa_answer = \
                                                queries.a_or_b()
                                    break  # exit the loop for chapter 3ba
                                elif chapter3ba_answer in ANSWER_B:
                                    clear()
                                    chapter4.chapter4bab()
                                    chapter4.chapter4bab_option_a()
                                    chapter4.chapter4bab_option_b()
                                    print(NEW_LINE)
                                    chapter4bab_answer = queries.a_or_b()
                                    while True:  # loop for chapter 4bab
                                        if chapter4bab_answer in ANSWER_A:
                                            clear()
                                            chapter5.chapter5baba()
                                            print(NEW_LINE)
                                            # exit the loop for chapter 4bab
                                            break
                                        elif chapter4bab_answer in ANSWER_B:
                                            clear()
                                            chapter5.chapter5babb()
                                            print(NEW_LINE)
                                            # exit the loop for chapter 4bab
                                            break
                                        else:
                                            clear()
                                            chapter4.chapter4bab()
                                            chapter4.chapter4bab_option_a()
                                            chapter4.chapter4bab_option_b()
                                            print(NEW_LINE)
                                            wrong_input.wrng_input1()
                                            chapter4bab_answer = \
                                                queries.a_or_b()
                                    break  # exit the loop for chapter 3ba
                                else:
                                    clear()
                                    chapter3.chapter3ba()
                                    chapter3.chapter3ba_option_a()
                                    chapter3.chapter3ba_option_b()
                                    print(NEW_LINE)
                                    wrong_input.wrng_input3()
                                    chapter3ba_answer = queries.a_or_b()
                            break  # exit the loop for chapter2b
                        elif chapter2b_answer in ANSWER_B:
                            clear()
                            chapter3.chapter3bb()
                            chapter3.chapter3bb_option_a()
                            chapter3.chapter3bb_option_b()
                            print(NEW_LINE)
                            chapter3bb_answer = queries.a_or_b()
                            while True:  # loop for chapter 3bb
                                if chapter3bb_answer in ANSWER_A:
                                    clear()
                                    chapter4.chapter4bba()
                                    chapter4.chapter4bba_option_a()
                                    chapter4.chapter4bba_option_b()
                                    print(NEW_LINE)
                                    chapter4bba_answer = queries.a_or_b()
                                    while True:  # loop for chapter 4bba
                                        if chapter4bba_answer in ANSWER_A:
                                            clear()
                                            chapter5.chapter5bbaa()
                                            print(NEW_LINE)
                                            # exit the loop for chapter 4bba
                                            break
                                        elif chapter4bba_answer in ANSWER_B:
                                            clear()
                                            chapter5.chapter5bbab()
                                            print(NEW_LINE)
                                            # exit the loop for chapter 4bba
                                            break
                                        else:
                                            clear()
                                            chapter4.chapter4bba()
                                            chapter4.chapter4bba_option_a()
                                            chapter4.chapter4bba_option_b()
                                            print(NEW_LINE)
                                            wrong_input.wrng_input5()
                                            chapter4bba_answer = \
                                                queries.a_or_b()
                                    break  # exit the loop for chapter 3bb
                                elif chapter3bb_answer in ANSWER_B:
                                    clear()
                                    chapter4.chapter4bbb()
                                    chapter4.chapter4bbb_option_a()
                                    chapter4.chapter4bbb_option_b()
                                    print(NEW_LINE)
                                    chapter4bbb_answer = queries.a_or_b()
                                    while True:  # loop for chapter 4bbb
                                        if chapter4bbb_answer in ANSWER_A:
                                            clear()
                                            chapter5.chapter5bbba()
                                            print(NEW_LINE)
                                            # exit the loop for chapter 4bbb
                                            break
                                        elif chapter4bbb_answer in ANSWER_B:
                                            clear()
                                            chapter5.chapter5bbbb()
                                            print(NEW_LINE)
                                            # exit the loop for chapter 4bbb
                                            break
                                        else:
                                            clear()
                                            chapter4.chapter4bbb()
                                            chapter4.chapter4bbb_option_a()
                                            chapter4.chapter4bbb_option_b()
                                            print(NEW_LINE)
                                            wrong_input.wrng_input2()
                                            chapter4bbb_answer = \
                                                queries.a_or_b()
                                    break  # exit the loop for chapter 3bb
                                else:
                                    clear()
                                    chapter3.chapter3bb()
                                    chapter3.chapter3bb_option_a()
                                    chapter3.chapter3bb_option_b()
                                    print(NEW_LINE)
                                    wrong_input.wrng_input4()
                                    chapter3bb_answer = queries.a_or_b()
                            break  # exit the loop for chapter2b
                        else:
                            clear()
                            chapter2.chapter2b()
                            chapter2.chapter2b_option_a()
                            chapter2.chapter2b_option_b()
                            print(NEW_LINE)
                            wrong_input.wrng_input3()
                            chapter2b_answer = queries.a_or_b()
                    break  # exit the loop for chapter1
                else:
                    clear()
                    chapter1.chapter1()
                    chapter1.chapter1_option_a()
                    chapter1.chapter1_option_b()
                    print(NEW_LINE)
                    wrong_input.wrng_input4()
                    chapter1_answer = queries.a_or_b()
            break
        elif first_answer in ANSWER_NO:
            print(NEW_LINE)
            print("Alright, maybe next time. Farewell, cosmic ninja!")
            break
        else:
            clear()
            welcome_text.start_message(name)
            print(NEW_LINE)
            wrong_input.wrng_input5()
            first_answer = queries.start_y_or_n()
    while True:
        if first_answer in ANSWER_NO:
            print("We'll miss you!")
            break
        else:
            play_again = input(f"""
{name}, do you want to play again? (yes/no): """).strip().lower()
            if play_again in ANSWER_YES:
                # Reset the game
                clear()
                main()  # restart the game
            elif play_again in ANSWER_NO:
                clear()
                welcome_text.goodbye_text(name)
                break
            else:
                wrong_input.wrng_input2()


if __name__ == "__main__":
    main()
