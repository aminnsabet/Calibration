import random
import os
import time
from datetime import datetime

def random_char():
    return random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

def modify_file(filename):
    with open(filename, 'r+') as file:
        content = file.read()
        if content:
            random_position = random.randint(0, len(content) - 1)
            content = content[:random_position] + random_char() + content[random_position + 1:]
            file.seek(0)
            file.write(content)
            file.truncate()

def git_commit_and_push():
    os.system('git add README.md')
    os.system('git commit -m "Random change to README.md"')
    os.system('git push origin main')  # Change 'main' to your branch name if different

def should_run_today():
    today = datetime.today().weekday()  # Monday is 0 and Sunday is 6
    return today not in [5, 6]  # Not Saturday or Sunday

def is_within_time_range():
    current_hour = datetime.now().hour
    return 8 <= current_hour < 20  # Between 8 AM and 8 PM

def main():
    while True:
        if should_run_today() and is_within_time_range():
            modify_file('README.md')
            git_commit_and_push()
            print("README.md modified and pushed at", datetime.now())
        
        # Wait for a random amount of time (in minutes) before next run
        next_run_in = random.randint(1, 240)  # Change 60 to any max minutes
        print(f"Next run in {next_run_in} minutes")
        time.sleep(next_run_in * 60)

if __name__ == "__main__":
    main()

