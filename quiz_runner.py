#Importing libraries
import random
import tkinter as tk
from tkinter import filedialog
from rich.console import Console
from rich.prompt import Prompt
from rich import box
from rich.table import Table
import time

console = Console() #Sets up the styled output system so we can print colorful, formatted messages throughout the quiz

#Adding welcome message with typing effect
#Asking the user to choose the question file
#Load questions from the text file
    #Open the files in read mode
    #Read all lines from the file
    #Initialize an empty list to store the questions
    #Loop thru the lines in the file
        #Add the question to the question list
#Create a function that will display the questions, as well as the choices
#Create a function that will ask user to input their answer to the question
#Create a function that will start the quiz
    #Initialize score as zero
    #Shuffle the list of all loaded questions
    #If user entered Q, print quit message and break the loop
    #Otherwise, check if the user's answer is correct 
#Define function: main()
    #Show welcome message
    #Call choose_file() to get file path
    #If no file chosen, show error and exit
    #Call load_questions_from_text()
    #If questions loaded, call start_quiz()
#Call main() to begin execution