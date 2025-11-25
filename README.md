# StudyBuddy — Multi-Agent Personalized Exam Prep Assistant


**Author:** Shivansh Shukla


## What this project is
StudyBuddy is a multi-agent system designed to help students prepare for exams. It generates study plans, retrieves concise resources, creates adaptive quizzes (including short code questions), auto-grades answers, and stores progress using a simple memory bank.


This repo is a submission-ready capstone skeleton for the Agents Intensive course. It includes an offline/simulated search tool and a toy code runner for demo purposes. Replace the LLM and web search stubs with real APIs for a production-ready project.


## Quick start
1. `python -m venv venv` (optional)
2. `pip install -r requirements.txt`
3. `uvicorn app.main:app --reload --port 8000`
4. Visit `http://localhost:8000/docs` for interactive API docs.


## File overview
See the `app/` folder for agent code, tools, and memory. Also included: `writeup.md` and `demo_video_script.md` for submission.

## Notes
- This demo uses a simple `subprocess` code runner — this is NOT secure for untrusted code. For judging, it is acceptable as a toy runner; for production use containerized sandboxes.
- Replace `app/utils/llm_client.py` with your LLM client (OpenAI, Anthropic, or internal) and update `app/tools/web_search.py` to call a real search API (SerpAPI/Bing) or the course MCP tool.
