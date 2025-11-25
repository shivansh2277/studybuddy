from app.agents.quizmaster import generate_quiz

def test_quiz_generation():
    quiz = generate_quiz("recursion", 4)
    assert len(quiz) == 4
    # expects alternating types: mcq, code, mcq, code...
    assert quiz[0]["type"] == "mcq"
    assert quiz[1]["type"] == "code"
