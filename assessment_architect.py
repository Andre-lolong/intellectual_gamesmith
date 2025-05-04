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
    with open("Questionnaire.txt", "a") as file:
         while True:
            # ask the question
            question = input("Enter your desired question: ").capitalize()
            # ask four possible answers (a, b, c, d)
            choice_a = input("Enter choice letter a: ")
            choice_b = input("Enter choice letter b: ")
            choice_c = input("Enter choice letter c: ")
            choice_d = input("Enter choice letter d: ")
            # ask the correct answer
            correct = input("Which letter is correct among the choices a, b, c, and d?: ")
            # write the inputs to file
            file.write("Question: " + question + "\n")
            file.write("a.): " + choice_a + "\n")
            file.write("b.): " + choice_b + "\n")
            file.write("c.): " + choice_c + "\n")
            file.write("d.): " + choice_d + "\n")
            file.write("correct answer: " + correct + "\n")
            print(" ")

            continunity = input("Do you want to add another question? (y/n): ")
            if continunity.lower() != "y":
                break       
        
    print("Your question(s) and choice(s) as well as the right answer has been added to the file")
    print("Your questionnaire is now ready!")
        
quiz()