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
        chapter1_answer = input('What would you like to do? ENTER [a / b] >>')
        if chapter1_answer in answer_a:
            clear()
            chapter2.chapter2a()
            chapter2.chapter2a_option_a()
            chapter2.chapter2a_option_b()
        elif chapter1_answer in answer_b:
            clear()
            chapter2.chapter2b()
            chapter2.chapter2b_option_a()
            chapter2.chapter2b_option_b()
        else:
            print("Oops! It seems like you've entered an invalid choice. Please enter 'a' or 'b'.")
        
        break
    elif first_answer in answer_no:
        print("Alright, maybe next time. Farewell, cosmic ninja!")
        break
    else:
        print("""Oops! It seems like you've entered a cosmic hiccup in the space-time continuum. 
        Give it another shot and remember, even cosmic ninjas make mistakes now and then! 
        Please enter 'yes' or 'no'.""")