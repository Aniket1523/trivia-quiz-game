class QuizBrain:

    def __init__(self, q_list):
        self.question_no = 0
        self.questions_list = q_list

    def still_has_questions(self):
        return self.question_no < len(self.questions_list)

    def next_question(self):
        ans = input(f"Q. {self.question_no + 1}: {self.questions_list[self.question_no].text} (True/False)?:")
        if ans.lower() == self.questions_list[self.question_no].answer.lower():
            self.question_no += 1
            return True
        else:
            return False
