class Quiz_brain:
    def __init__(self, question_bank):
        self.que_list = question_bank
        self.que_num = 0
        self.score = 0

    def next_question(self):
        current_question = self.que_list[self.que_num]
        self.que_num += 1
        print("\n" + "-" * 50)
        user_ans = input(f"\033[96mQ.{self.que_num}: {current_question.text} (True/False): \033[0m").lower().strip()
        self.check_answer(user_ans, current_question.answer)

    def still_have_questions(self):
        return self.que_num < len(self.que_list)

    def check_answer(self, guess, correct_answer):
        if guess == correct_answer.lower():
            print("\033[92m✅ Correct! Great job!\033[0m")
            self.score += 1
        else:
            print(f"\033[91m❌ Wrong! The correct answer was: {correct_answer}\033[0m")
        print(f"\033[93m📊 Your Score: {self.score}/{self.que_num}\033[0m")
