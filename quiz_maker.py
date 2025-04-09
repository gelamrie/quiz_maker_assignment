#Initialize the libraries that will be needed 
from colorama import init, Fore, Style
import time, sys 

init(autoreset=True)

#Create a typing effect for the welcome screen 
def typing_effect_centered(text, width=60, delay=0.04, color=Fore.RED + Style.BRIGHT):
    centered_text = text.center(width)
    for char in centered_text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

#Create a function for the welcome screen 
def welcome_screen():
    border_design = (" ★ " + " ♡ ") * 10 #Add border design to enhance the appearance 
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT + border_design)
    typing_effect_centered(" Welcome to the Quiz Creator! ", width=len(border_design)) #Display a welcome message with the typing effect
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT + border_design + "\n")

#Create a function that will ask the user for the category, questions, choices and correct answer
def get_question_block(): 
    print(Fore.CYAN + "\n=== New Question ===")

    category = input(Fore.LIGHTMAGENTA_EX + "Enter a category (e.g., Math, History, Science): ")
    question = input(Fore.YELLOW + "Enter the question: ")

    #After asking for the choices, store it in a disctionary
    choices_dictionary = {}
    for letter in ['a', 'b', 'c', 'd']:
        choices_dictionary[letter] = input(Fore.BLUE + f"Choice ({letter}): ")

    #After entering the correct answer, validate if it is one of the choices
    while True: 
        correct_answer = input(Fore.GREEN + "Which one is the correct answer? (a/b/c/d): ")
        if correct_answer in choices_dictionary:
            break 
        print(Fore.RED + "❌ Invalid input. Please choose from a, b, c, or d.")
    
    #If valid, return
    return (f"Category: {category}\n"
        f"Question: {question_text}\n"
        + ''.join(f"{option}) {choices_dictionary[option]}\n" for option in ['a', 'b', 'c', 'd'])
        + f"Answer: {correct_answer}\n\n")

#Create a function for the main program and create the logic
def main():
    welcome_screen() #Call the welcome screen
   
    file_name = input(Fore.LIGHTCYAN_EX + "Enter the file name to save your quiz (e.g., myquiz.txt): ").strip() #Ask the user for the file name for saving the quiz
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    #Create an empty list to store all questions for the session
    all_questions_this_session = []
    
    #Open the text file
        #Start a loop to repeatedly ask user to add questions
        #Write the question to the file
        #Add the question to the list for the preview later
        #Ask the user if they still want to input another question
    #After exiting the loop, print a success message that will indicate that all questions were saved to the file 
    #Print the preview of all questions from the session
#Run the program 



