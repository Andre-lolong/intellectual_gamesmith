# Create a program that ask the user for a question, it will also ask for 4 possible answers (a, b, c, d) and the correct answer
# Write the collected data to a text file
# Ask another question until the user chose to exit

# Create a function for the program, that can be called or reused later
# Set and open file named 'questionnaire' and and a mode in which file is opened
# Use while loop to ask the user repetitively for questions and answers that will break if the user wants to stop
# Ask the user to input: question, possible answers (a, b, c, d) and a correct answer
# Write the string answers from the previous input to the file 
# Ask if the user wants to add more
# if True, then repeat the loop to ask more questions, possible answers and correct answer
# if False, then break the loop

# Close the file
# Tell the user that the multiple-choice questionnaire has been made  

def quiz():
    file = open("Questionnaire", "a")

    while True:
        # ask the question
        question = input("Enter your desired quesiton: ")
        # ask four possible answers (a, b, c, d)
        a = input("Enter choice letter a: ")
        b = input("Enter choice letter b: ")
        c = input("Enter choice letter c: ")
        d = input("Enter choice letter d:")
        # ask the correct answer
        correct = input("Which letter is correct among the choices a, b, c, and d?: ")