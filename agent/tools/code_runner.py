import subprocess, tempfile, os, sys




def run_code(py_code: str, timeout: int = 3):
"""
Very simple toy sandbox for demo. DO NOT use in production for running untrusted code.
"""
fname = tempfile.mktemp(suffix=".py")
with open(fname, "w") as f:
f.write(py_code)
try:
proc = subprocess.run([sys.executable, fname], capture_output=True, text=True, timeout=timeout)
return {"stdout": proc.stdout, "stderr": proc.stderr, "returncode": proc.returncode}
except Exception as e:
return {"error": str(e)}
finally:
try: os.remove(fname)
except: pass
