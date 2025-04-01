from question_model import Question
from data import question_data as qd
from quiz_brain import Quiz_brain

# Colors for better UI
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

print(YELLOW + "\n🚀 Welcome to the Ultimate Tech Quiz! 🚀\n" + RESET)

question_bank = []
for question in qd:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

quiz = Quiz_brain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

print(GREEN + "\n🎉 Congratulations! You've completed the quiz! 🎉" + RESET)
print(CYAN + f"🏆 Your Final Score: {quiz.score}/{quiz.que_num} 🏆" + RESET)
