# All imports for the app
import welcome_text
import os
import chapter1
import chapter2
import chapter3
import chapter4

clear = lambda: os.system('clear') 
# to make sure that any way of writing your answer is accepted
answer_a = ["a", "A"]
answer_b = ["b", "B"]
answer_yes = ["y", "Y", "YES", "yes", "Yes", "YEs", "yES"]
answer_no = ["n", "N", "NO", "no", "No", "nO"]
# to style the console output
new_line = '\n'

# game start
welcome_text.welcome_logo()
welcome_text.introduction()
name = input('ENTER YOUR NINJA NAME >> ')
clear()
welcome_text.start_message(name)
print(new_line)
first_answer = input('Would you like to start your adventure? ENTER [yes / no]: >>')

# game loop
while True:
    if first_answer in answer_yes:
        clear()
        chapter1.chapter1()
        chapter1.chapter1_option_a()
        chapter1.chapter1_option_b()
        print(new_line)
        chapter1_answer = input('What would you like to do? ENTER [a / b] >>')
        while True: # loop for the choice in chapter 1
            if chapter1_answer in answer_a:
                clear()
                chapter2.chapter2a()
                chapter2.chapter2a_option_a()
                chapter2.chapter2a_option_b()
                print(new_line)
                chapter2a_answer = input('What would you like to do? ENTER [a / b] >>')
                while True: # loop for chapter 2a
                    if chapter2a_answer in answer_a:
                        clear()
                        chapter3.chapter3aa()
                        chapter3.chapter3aa_option_a()
                        chapter3.chapter3aa_option_b()
                        print(new_line)
                        chapter3aa_answer = input('What would you like to do? ENTER [a / b] >>')
                        while True: # loop for chapter 3aa
                            if chapter3aa_answer in answer_a:
                                clear()
                                chapter4.chapter4aaa()
                                chapter4.chapter4aaa_option_a()
                                chapter4.chapter4aaa_option_b()
                                print(new_line)
                                chapter4aaa_answer = input('What would you like to do? ENTER [a / b] >>')
                                break #exit the loop for chapter 3aa
                            elif chapter3aa_answer in answer_b:
                                clear()
                                chapter4.chapter4aab()
                                chapter4.chapter4aab_option_a()
                                chapter4.chapter4aab_option_b()
                                print(new_line)
                                chapter4aab_answer = input('What would you like to do? ENTER [a / b] >>')
                                break #exit the loop for chapter 3aa
                            else:
                                clear()
                                chapter3.chapter3aa()
                                chapter3.chapter3aa_option_a()
                                chapter3.chapter3aa_option_b()
                                print(new_line)
                                print("""Looks like you've entered the intergalactic labyrinth of choices. Don't worry, even cosmic ninjas sometimes take detours. Try your cosmic navigation skills again!""")
                                chapter3aa_answer = input('What would you like to do? ENTER [a / b] >>')
                        break # exit the loop for chapter 2a
                    elif chapter2a_answer in answer_b:
                        clear()
                        chapter3.chapter3ab()
                        chapter3.chapter3ab_option_a()
                        chapter3.chapter3ab_option_b()
                        print(new_line)
                        chapter3ab_answer = input('What would you like to do? ENTER [a / b] >>')
                        while True: # loop for chapter 3ab
                            if chapter3aa_answer in answer_a:
                                clear()
                                chapter4.chapter4aba()
                                chapter4.chapter4aba_option_a()
                                chapter4.chapter4aba_option_b()
                                print(new_line)
                                chapter4aba_answer = input('What would you like to do? ENTER [a / b] >>')
                                break #exit the loop for chapter 3ab
                            elif chapter3aa_answer in answer_b:
                                clear()
                                chapter4.chapter4abb()
                                chapter4.chapter4abb_option_a()
                                chapter4.chapter4abb_option_b()
                                print(new_line)
                                chapter4abb_answer = input('What would you like to do? ENTER [a / b] >>')
                                break #exit the loop for chapter 3ab
                            else:
                                clear()
                                chapter3.chapter3ab()
                                chapter3.chapter3ab_option_a()
                                chapter3.chapter3ab_option_b()
                                print(new_line)
                                print("""Looks like you've entered the intergalactic labyrinth of choices. Don't worry, even cosmic ninjas sometimes take detours. Try your cosmic navigation skills again!""")
                                chapter3ab_answer = input('What would you like to do? ENTER [a / b] >>')
                        break # exit the loop for chapter 2a
                    else:
                        clear()
                        chapter2.chapter2a()
                        chapter2.chapter2a_option_a()
                        chapter2.chapter2a_option_b()
                        print(new_line)
                        print("""Epic cosmic blunder! It happens to the best of us. Go ahead, rewrite your cosmic destiny with a keystroke!""")
                        chapter2a_answer = input('What would you like to do? ENTER [a / b] >>')
                break # exit the loop for chapter1 
            elif chapter1_answer in answer_b:
                clear()
                chapter2.chapter2b()
                chapter2.chapter2b_option_a()
                chapter2.chapter2b_option_b()
                print(new_line)
                chapter2b_answer = input('What would you like to do? ENTER [a / b] >>')
                while True: # loop for chapter 2b
                    if chapter2b_answer in answer_a:
                        clear()
                        chapter3.chapter3ba()
                        chapter3.chapter3ba_option_a()
                        chapter3.chapter3ba_option_b()
                        print(new_line)
                        chapter3ba_answer = input('What would you like to do? ENTER [a / b] >>')
                        while True: # loop for chapter 3ba
                            if chapter3ba_answer in answer_a:
                                clear()
                                chapter4.chapter4baa()
                                chapter4.chapter4baa_option_a()
                                chapter4.chapter4baa_option_b()
                                print(new_line)
                                chapter4baa_answer = input('What would you like to do? ENTER [a / b] >>')
                                break #exit the loop for chapter 3ba
                            elif chapter3ba_answer in answer_b:
                                clear()
                                chapter4.chapter4bab()
                                chapter4.chapter4bab_option_a()
                                chapter4.chapter4bab_option_b()
                                print(new_line)
                                chapter4bab_answer = input('What would you like to do? ENTER [a / b] >>')
                                break #exit the loop for chapter 3ba
                            else:
                                clear()
                                chapter3.chapter3ba()
                                chapter3.chapter3ba_option_a()
                                chapter3.chapter3ba_option_b()
                                print(new_line)
                                print("""Looks like you've entered the intergalactic labyrinth of choices. Don't worry, even cosmic ninjas sometimes take detours. Try your cosmic navigation skills again!""")
                                chapter3ba_answer = input('What would you like to do? ENTER [a / b] >>')
                        break # exit the loop for chapter2b
                    elif chapter2b_answer in answer_b:
                        clear()
                        chapter3.chapter3bb()
                        chapter3.chapter3bb_option_a()
                        chapter3.chapter3bb_option_b()
                        print(new_line)
                        chapter3bb_answer = input('What would you like to do? ENTER [a / b] >>')
                        while True: # loop for chapter 3bb
                            if chapter3bb_answer in answer_a:
                                clear()
                                chapter4.chapter4bba()
                                chapter4.chapter4bba_option_a()
                                chapter4.chapter4bba_option_b()
                                print(new_line)
                                chapter4bba_answer = input('What would you like to do? ENTER [a / b] >>')
                                break #exit the loop for chapter 3bb
                            elif chapter3bb_answer in answer_b:
                                clear()
                                chapter4.chapter4bbb()
                                chapter4.chapter4bbb_option_a()
                                chapter4.chapter4bbb_option_b()
                                print(new_line)
                                chapter4bbb_answer = input('What would you like to do? ENTER [a / b] >>')
                                break #exit the loop for chapter 3bb
                            else:
                                clear()
                                chapter3.chapter3bb()
                                chapter3.chapter3bb_option_a()
                                chapter3.chapter3bb_option_b()
                                print(new_line)
                                print("""Hold on a moment, it appears your cosmic ninja keyboard skills need a calibration. Try anew and aim for the accuracy of a laser-guided shuriken!""")
                                chapter3bb_answer = input('What would you like to do? ENTER [a / b] >>')
                        break # exit the loop for chapter2b
                    else:
                        clear()
                        chapter2.chapter2b()
                        chapter2.chapter2b_option_a()
                        chapter2.chapter2b_option_b()
                        print(new_line)
                        print("""Hold on a moment, it appears your cosmic ninja keyboard skills need a calibration. 
                        Try anew and aim for the accuracy of a laser-guided shuriken!""")
                        chapter2b_answer = input('What would you like to do? ENTER [a / b] >>')
                break # exit the loop for chapter1
            else:
                clear()
                chapter1.chapter1()
                chapter1.chapter1_option_a()
                chapter1.chapter1_option_b()
                print(new_line)
                print("""Uh-oh, it appears your ninja instincts are momentarily eclipsed by the cosmic chaos. 
                Take a deep breath, focus your energy, and try again with the precision of a laser ninja-star! Please enter 'a' or 'b'.""")
                chapter1_answer = input('What would you like to do? ENTER [a / b] >>')
        break
    elif first_answer in answer_no:
        print("Alright, maybe next time. Farewell, cosmic ninja!")
        break
    else:
        clear()
        welcome_text.start_message(name)
        print(new_line)
        print("""Oops! It seems like you've entered a cosmic hiccup in the space-time continuum. 
        Give it another shot and remember, even cosmic ninjas make mistakes now and then! 
        Please enter 'yes' or 'no'.""")
        first_answer = input('Would you like to start your adventure? ENTER [yes / no]: >>')