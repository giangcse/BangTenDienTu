import subprocess
import time

subprocess.run(["python", "main.py"])
time.sleep(3)
subprocess.run(["taskkill", "/IM", "python.exe", "/F"])
