#All imports for the app
import welcome_text
import os
clear = lambda: os.system('clear') 

answer_a = ["a", "A"]
answer_b = ["b", "B"]


welcome_text.welcome_logo()
welcome_text.introduction()
name = input('ENTER YOUR NINJA NAME >> ')

clear()

welcome_text.start_message(name)

