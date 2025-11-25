from typing import List




def generate_quiz(topic: str, n: int = 5):
"""
Generate a simple mix of MCQ and short code questions.
Replace with LLM-based question generation for better quality.
"""
quiz = []
for i in range(n):
quiz.append({
"id": i+1,
"type": "mcq" if i % 2 == 0 else "code",
"question": f"Sample {topic} question #{i+1}",
"choices": ["A", "B", "C", "D"] if i % 2 == 0 else None,
"expected_code": "def add(a,b):\n return a+b" if i % 2 == 1 else None
})
return quiz
