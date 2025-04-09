import html

class Quiz_brain:
    def __init__(self, question_bank):
        self.que_list = question_bank
        self.que_num = 0
        self.score = 0

    def next_question(self):
        self.current_question = self.que_list[self.que_num]
        self.que_num += 1
        print("\n" + "-" * 50)
        q_text=html.unescape(self.current_question.text)
        # user_ans = input(f"\033[96mQ.{self.que_num}: {q_text} (True/False): \033[0m").lower().strip()
        # self.check_answer(user_ans, current_question.answer)
        return f"{self.que_num}: {q_text}"

    def still_have_questions(self):
        return self.que_num < len(self.que_list)

    def check_answer(self, guess):
        correct_answer=self.current_question.answer
        if guess.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False


        #     print("\033[92m✅ Correct! Great job!\033[0m")
        #     self.score += 1
        # else:
        #     print(f"\033[91m❌ Wrong! The correct answer was: {correct_answer}\033[0m")
        # print(f"\033[93m📊 Your Score: {self.score}/{self.que_num}\033[0m")
