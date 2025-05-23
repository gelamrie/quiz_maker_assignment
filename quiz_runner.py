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
def type_writer(message, delay=0.04):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # new line

#Asking the user to choose the question file
def choose_file():
    root = tk.Tk()
    root.withdraw() # Hide the main tkinter window
    file_path = filedialog.askopenfilename(
        title="Select Quiz Bank File",
        filetypes=[("Text files", "*.txt")]
    )
    return file_path

#Load questions from the text file
def load_questions_from_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file: #Open the files in read mode
        raw_lines = [line.strip() for line in file.readlines()] #Read all lines from the file

    question_list = [] #Initialize an empty list to store the questions
    line_index = 0

    
    while line_index + 7 < len(raw_lines): #Loop thru the lines in the file
        if raw_lines[line_index] == "":
            line_index += 1
            continue
         
        try:
            category_line = raw_lines[line_index]
            question_line = raw_lines[line_index + 1]
            choice_lines = raw_lines[line_index + 2:line_index + 6]
            answer_line = raw_lines[line_index + 6]

            category = category_line.split(":", 1)[1].strip()
            question_text = question_line
            choices = [line[3:].strip() for line in choice_lines]    
        
            correct_letter = answer_line.split(":", 1)[1].strip().upper()
            correct_index = ord(correct_letter) - ord('A')
            correct_choice = choices[correct_index]

            question_list.append({ #Add the question to the question list
                "category": category,
                "question": question_text,
                "choices": choices,
                "answer": correct_choice
            }) 
        
        except Exception as error:
            console.print(f"[bold red]⚠ Malformed block at line {line_index + 1}: {error}[/bold red]")
    
        line_index += 8   

    return question_list
     
#Create a function that will display the questions, as well as the choices
def display_question(question_data, question_number):
    console.print(f"\n[bold blue]Question {question_number + 1}:[/bold blue] {question_data['question']}")

    choices_table = Table(box=box.SIMPLE)
    choices_table.add_column("Letter", justify="center")
    choices_table.add_column("Option", justify="left")

    choice_letters = ["A", "B", "C", "D"]
    for index, choice_text in enumerate(question_data["choices"]):
        choices_table.add_row(choice_letters[index], choice_text)

    console.print(choices_table)

#Create a function that will ask user to input their answer to the question
def prompt_user_for_answer():
    valid_letters = ['A', 'B', 'C', 'D', 'Q'] 
    while True:
        user_input = Prompt.ask("[bold yellow]Your answer (A-D or Q to quit)[/bold yellow]").strip().upper()
        if user_input in valid_letters:
            return user_input
        console.print("[bold red]❗ Invalid input. Choose A, B, C, D, or Q to quit.[/bold red]")

#Create a function that will start the quiz
def start_quiz(questions):
    score = 0  #Initialize score as zero
    random.shuffle(questions) #Shuffle the list of all loaded questions

    for question_number, question_data in enumerate(questions):
        display_question(question_data, question_number)
        user_letter = prompt_user_for_answer()

        if user_letter == "Q": #If user entered Q, print quit message and break the loop
            console.print("[bold cyan]👋 You chose to quit the quiz early.[/bold cyan]\n")
            break

        user_choice_index = ord(user_letter) - ord('A')
        user_choice = question_data["choices"][user_choice_index]
        correct_choice = question_data["answer"]

    #Otherwise, check if the user's answer is correct 
        if user_choice == correct_choice:
            console.print("[bold green]✅ Correct! Good job![/bold green]\n")
            score += 1
        else:
            correct_index = question_data["choices"].index(correct_choice)
            correct_letter = chr(correct_index + ord('A'))
            console.print(f"[bold red]❌ Wrong! Correct Answer: {correct_letter}. {correct_choice}[/bold red]\n")

    answered = question_number + 1 if user_letter != "Q" else question_number
    console.rule("[bold cyan]Quiz Finished![/bold cyan]")
    console.print(f"[bold magenta]🔥 Final Score: {score}/{answered}[/bold magenta]")

def main(): #Define function: main()
    type_writer("\n🎉 Welcome to the Quiz Game! Test your knowledge and have fun!\n", delay=0.05) #Show welcome message
   
    file_path = choose_file() #Call choose_file() to get file path
    if not file_path:
        console.print("[bold red]❌ No file selected. Exiting.[/bold red]")    #If no file chosen, show error and exit
        return 
    console.print(f"[bold cyan]📂 Loading file:[/bold cyan] {file_path}")
    
    try:
        questions = load_questions_from_text(file_path) #Call load_questions_from_text()
        console.print(f"[bold green]📚 {len(questions)} questions loaded. Let's go![/bold green]\n")
        start_quiz(questions) #If questions loaded, call start_quiz()
    
    except Exception as error:
        console.print(f"[bold red]❌ Error: {error}[/bold red]")
   

if __name__ == "__main__":
    main() #Call main() to begin execution