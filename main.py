from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
Score = 0
for question in question_data:
    new_q = Question(question['text'], question['answer'])
    question_bank.append(new_q)
print("True or False Tumult: Navigate the Maze of Facts and Fiction!")
qb = QuizBrain(question_bank)
while qb.still_has_questions():
    if qb.next_question():
        Score += 1
        print(f"That's correct... Your score is {Score}")
    else:
        print(f"That's incorrect... Your Final score is {Score}")
        break
