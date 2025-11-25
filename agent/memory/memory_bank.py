import json, os
PATH = "app/memory/memory.json"




def load_memory():
if not os.path.exists(PATH):
return {}
with open(PATH, "r") as f:
return json.load(f)




def save_memory(data):
with open(PATH, "w") as f:
json.dump(data, f, indent=2)




def update_progress(user_id: str, record: dict):
m = load_memory()
user = m.setdefault(user_id, {"progress": []})
user["progress"].append(record)
save_memory(m)
