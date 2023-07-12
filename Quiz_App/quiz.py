import random
import json

class QuizGame:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
    
    def set_questions(self,questions):
        self.questions = questions
    
    def start(self):
        random.shuffle(self.questions)
        print("Welcome To Quiz! if you want to quit the game press 'q'.")
        for question in self.questions:
            print(question["question"])
            user_answer = input("Give your answer: ")
            if user_answer.lower() == question["answer"].lower():
                print("Correct Answer!")
                self.score += 1
            elif user_answer.lower() == 'q':
                print("Game Over!")
                break
            else:
                print(f"Wrong Answer! Correct answer is: {question['answer']}")
        print(f"Game Over! Your score: {self.score} / {len(self.questions)}")
def read_questions_from_file(file_path):
    questions=[]
    
    with open(file_path,'r') as file:
        questions = json.load(file)
    return questions
questions = read_questions_from_file("Python_Mini_Projects//Quiz_App//questions.json")

quiz = QuizGame(questions)
quiz.start()
    