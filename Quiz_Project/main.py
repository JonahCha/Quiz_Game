from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(text=question_text,answer=question_answer)
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

    if quiz.still_has_question() == False:
        print(f"You Have Completed The Quiz\nYour Score is:{quiz.score}/{quiz.question_no}")
