#All imports for the app
import welcome_text
import os
import chapter1
import chapter2
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
while True:
    first_answer = input('Would you like to start your adventure? ENTER [yes / no]: >>')
    if first_answer in answer_yes:
        clear()
        chapter1.chapter1()
        chapter1.chapter1_option_a()
        chapter1.chapter1_option_b()
        print(new_line)
        chapter1_answer = input('What would you like to do? ENTER [a / b] >>')
        if chapter1_answer in answer_a:
            clear()
            chapter2.chapter2a()
            chapter2.chapter2a_option_a()
            chapter2.chapter2a_option_b()
            print(new_line)
            chapter2a_answer = input('What would you like to do? ENTER [a / b] >>')
                if chapter2a_answer in answer_a:
                clear()
                chapter3.chapter3aa()
                chapter3.chapter3aa_option_a()
                chapter3.chapter3aa_option_b()
                print(new_line)
                chapter3aa_answer = input('What would you like to do? ENTER [a / b] >>')
                elif chapter2a_answer in answer_b:
                clear()
                chapter3.chapter3ab()
                chapter3.chapter3ab_option_a()
                chapter3.chapter3ab_option_b()
                print(new_line)
                chapter3ab_answer = input('What would you like to do? ENTER [a / b] >>')
        elif chapter1_answer in answer_b:
            clear()
            chapter2.chapter2b()
            chapter2.chapter2b_option_a()
            chapter2.chapter2b_option_b()
            print(new_line)
            chapter2b_answer = input('What would you like to do? ENTER [a / b] >>')
                if chapter2b_answer in answer_a:
                clear()
                chapter3.chapter3ba()
                chapter3.chapter3ba_option_a()
                chapter3.chapter3ba_option_b()
                print(new_line)
                chapter3ba_answer = input('What would you like to do? ENTER [a / b] >>')
                elif chapter2b_answer in answer_b:
                clear()
                chapter3.chapter3bb()
                chapter3.chapter3bb_option_a()
                chapter3.chapter3bb_option_b()
                print(new_line)
                chapter3bb_answer = input('What would you like to do? ENTER [a / b] >>')
        else:
            print("""Uh-oh, it appears your ninja instincts are momentarily eclipsed by the cosmic chaos. 
            Take a deep breath, focus your energy, and try again with the precision of a laser ninja-star! Please enter 'a' or 'b'.""")
        
        break
    elif first_answer in answer_no:
        print("Alright, maybe next time. Farewell, cosmic ninja!")
        break
    else:
        print("""Oops! It seems like you've entered a cosmic hiccup in the space-time continuum. 
        Give it another shot and remember, even cosmic ninjas make mistakes now and then! 
        Please enter 'yes' or 'no'.""")