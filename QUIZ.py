import csv
import random

# Read questions and answers from file
def read_questions(filename):
    questions = []
    with open("quiz.csv", 'r') as file:
        reader = csv.reader(file)
        for column in reader:
            question = {
                    'text': column[0],
                    'options': column[1:5], 
                    'correct': column[5] 
                }
            questions.append(question)
    return questions

# Select 10 random questions
def select_questions(questions):
    return random.sample(questions, 10)

# Conduct the quiz
def conduct_quiz(questions):
    score = 0
    incorrect_questions = []
    for question in questions:
        print(question['text'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        answer = input("Enter your answer: ")
        if answer == question['correct']:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {question['correct']}.")
            incorrect_questions.append(question['text'])
    return score, incorrect_questions

# Display results
def display_results(score, incorrect_questions):
    if score >= 8:
        print("Congrats!")
    else:
        print("Thanks for taking this quiz. This is just an indicative result to assist you in revisiting these areas:")
        for question in incorrect_questions:
            print(question)

# Main program
def main():
    filename ="quiz.csv"
    questions = read_questions(filename)
    quiz_questions = select_questions(questions)
    score,incorrect_questions = conduct_quiz(quiz_questions)
    display_results(score,incorrect_questions)
p=input("Enter Start to play the quiz")
if(p=="Start"):
      main()
