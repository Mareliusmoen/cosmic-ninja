#All imports for the app
import welcome_text
import os
import chapter1
import chapter2
import chapter3

clear = lambda: os.system('clear') 

answer_a = ["a", "A"]
answer_b = ["b", "B"]
answer_yes = ["y", "Y", "YES", "yes"]
answer_no = ["n", "N", "NO", "no"]
new_line = '\n'
welcome_text.welcome_logo()
welcome_text.introduction()
name = input('ENTER YOUR NINJA NAME >> ')

clear()

welcome_text.start_message(name)
# game loop
while True:
    first_answer = input('Would you like to start your adventure? ENTER [yes / no]: >>')
    if first_answer in answer_yes:
        clear()
        chapter1.chapter1()
        chapter1.chapter1_option_a()
        chapter1.chapter1_option_b()
        print(new_line)
        chapter1_answer = input('What would you like to do? ENTER [a / b] >>')
        # loop for the choice in chapter 1
        while True:
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
                        break # exit the loop for chapter 2a
                    elif chapter2a_answer in answer_b:
                        clear()
                        chapter3.chapter3ab()
                        chapter3.chapter3ab_option_a()
                        chapter3.chapter3ab_option_b()
                        print(new_line)
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
                        break # exit the loop for chapter2b
                    elif chapter2b_answer in answer_b:
                        clear()
                        chapter3.chapter3bb()
                        chapter3.chapter3bb_option_a()
                        chapter3.chapter3bb_option_b()
                        print(new_line)
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
                print("""Uh-oh, it appears your ninja instincts are momentarily eclipsed by the cosmic chaos. 
                Take a deep breath, focus your energy, and try again with the precision of a laser ninja-star! Please enter 'a' or 'b'.""")
                chapter1_answer = input('What would you like to do? ENTER [a / b] >>')
        break
    elif first_answer in answer_no:
        print("Alright, maybe next time. Farewell, cosmic ninja!")
        break
    else:
        clear()
        chapter1.chapter1()
        chapter1.chapter1_option_a()
        chapter1.chapter1_option_b()
        print(new_line)
        print("""Oops! It seems like you've entered a cosmic hiccup in the space-time continuum. 
        Give it another shot and remember, even cosmic ninjas make mistakes now and then! 
        Please enter 'yes' or 'no'.""")