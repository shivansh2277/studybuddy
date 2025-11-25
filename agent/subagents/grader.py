from ..tools.code_runner import run_code




def grade_mcq(answer: str, correct: str) -> dict:
return {"correct": answer == correct}




def grade_code(submitted_code: str, test_code: str) -> dict:
"""
For demo: combine submitted code + test code and execute. Test code should raise an exception
or assert to indicate a failed test.
"""
wrapper = submitted_code + "\n\n" + test_code
res = run_code(wrapper)
passed = res.get("returncode", 1) == 0 and res.get("stderr", "") == ""
return {"passed": passed, "exec": res}
