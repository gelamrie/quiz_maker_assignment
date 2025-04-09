#Initialize the libraries that will be needed 
from colorama import init, Fore, Style
import time, sys 

init(autoreset=True)

#Create a typing effect for the welcome screen 
def typing_effect_centered(text, width=60, delay=0.04, color=Fore.RED + Style.BRIGHT):
    centered_text = text.center(width)
    for char in centered_text:

#Create a function for the welcome screen 
    #Add border design to enhance the appearance 
    #Display a welcome message with the typing effect
#Create a function that will ask the user for the category, questions, choices and correct answer
    #After asking for the choices, store it in a disctionary
    #After entering the correct answer, validate if it is one of the choices
    #If valid, return
#Create a function for the main program and create the logic
    #Call the welcome screen
    #Ask the user for the file name for saving the quiz
    #Create an empty list to store all questions for the session
    #Open the text file
        #Start a loop to repeatedly ask user to add questions
        #Write the question to the file
        #Add the question to the list for the preview later
        #Ask the user if they still want to input another question
    #After exiting the loop, print a success message that will indicate that all questions were saved to the file 
    #Print the preview of all questions from the session
#Run the program 



