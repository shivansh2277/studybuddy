from fastapi import FastAPI
from pydantic import BaseModel
from .agents.planner import generate_plan
from .agents.retriever import retrieve_resources
from .agents.quizmaster import generate_quiz
from .agents.grader import grade_mcq as grade_mcq_fn
from .memory.memory_bank import update_progress


app = FastAPI(title="StudyBuddy")


class PlanRequest(BaseModel):
user_id: str
goal: str
days: int = 7


@app.post("/plan")
def plan(req: PlanRequest):
plan = generate_plan(req.goal, req.days)
return {"plan": plan}


class QuizRequest(BaseModel):
user_id: str
topic: str
n: int = 5


@app.post("/quiz")
def quiz(req: QuizRequest):
quiz = generate_quiz(req.topic, req.n)
return {"quiz": quiz}


class GradeMCQRequest(BaseModel):
user_id: str
qid: int
answer: str
correct: str


@app.post("/grade_mcq")
def grade_mcq_endpoint(payload: GradeMCQRequest):
result = grade_mcq_fn(payload.answer, payload.correct)
update_progress(payload.user_id, {"type":"mcq", "qid": payload.qid, "result": result})
return result
