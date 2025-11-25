# Simple in-memory session store for the running FastAPI process.
SESSIONS = {}


def create_session(user_id: str):
SESSIONS[user_id] = {"current_topic": None}
return SESSIONS[user_id]


def get_session(user_id: str):
return SESSIONS.get(user_id)
