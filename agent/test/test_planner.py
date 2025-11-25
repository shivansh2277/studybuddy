from app.agents.planner import generate_plan

def test_generate_plan_structure():
    plan = generate_plan("recursion", 3)
    assert "days" in plan
    assert len(plan["days"]) == 3
    assert plan["days"][0]["focus"].startswith("recursion")
