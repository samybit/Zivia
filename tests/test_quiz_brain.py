from src.zivia.quiz_brain import QuizBrain
from src.zivia.question_model import Question

def test_score_increments():
    # one question true
    qb = QuizBrain([Question("a", "True")])
    qb.next_question()
    qb.check_answer("True")
    assert qb.score == 1