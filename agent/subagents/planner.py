from typing import Dict


def generate_plan(user_goal: str, days: int = 7) -> Dict:
"""
Create a naive day-wise study plan by splitting the goal into subtopics.
Replace with LLM-assisted syllabus parsing for a richer planner.
"""
plan = {"days": []}
for i in range(1, days+1):
plan["days"].append({"day": i, "focus": f"{user_goal} - subtopic {i}"})
return plan
