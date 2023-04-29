import random
OUTPUT_FILE = "commit_bot.txt"
from os         import system
from datetime   import datetime 
from threading  import Thread
def create_commit():
    while True:
        system("git pull -X theirs")
        for _ in range(100):
            with open(OUTPUT_FILE, "w") as f:
                f.write(str(datetime.now()))
                
            system(f"git add {OUTPUT_FILE}")
            system(f"git commit -m \"Update {OUTPUT_FILE}\"")
            
        system("git pull -X theirs")
        system("git push")
create_commit()
