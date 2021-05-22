import json
import time
from datetime import datetime

def load_file(json_path):
  with open(json_path, 'r') as file:
    return json.load(file)

def rotary_animation(rotation_time):
  animation = "|/-\\"
  idx = 0
  start_time = datetime.now()
  diff = 0
  while diff < rotation_time:
      diff = (start_time - datetime.now()).total_seconds()
      print(animation[idx % len(animation)], end="\r")
      idx += 1
      time.sleep(0.1)

def any_key_input():
  input("\n\nPress any key to go back.")
