import os
import subprocess
from datetime import datetime, timedelta

# --- CONFIGURATION ---
# Your actual start date from the Pattern Tracker
start_date = datetime(2026, 2, 19, 12, 0, 0) 
total_days = 34 

def run_cmd(command, env=None):
    try:
        subprocess.run(command, shell=True, check=True, env=env)
    except subprocess.CalledProcessError as e:
        print(f"Error executing: {command}\n{e}")

# 1. Initialize git if you haven't already
if not os.path.exists(".git"):
    run_cmd("git init")
    print("Initialized empty Git repository.")

# 2. Iterate through each day to create backdated commits
for i in range(1, total_days + 1):
    folder_name = f"Day-{i:02d}"
    
    if os.path.exists(folder_name):
        # Calculate the historical date for this specific day
        current_date = start_date + timedelta(days=i-1)
        date_string = current_date.strftime('%Y-%m-%dT%H:%M:%S')
        
        # Stage the folder for this specific day
        run_cmd(f"git add {folder_name}")
        
        # Also stage the assets if they exist (to keep proof with the day)
        # Note: This assumes your assets are in an /assets folder
        run_cmd("git add assets/") 
        
        # Set Git environment variables for the historical timestamp
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_string
        env["GIT_COMMITTER_DATE"] = date_string
        
        # Commit with the specific day's message
        commit_msg = f"Day {i:02d}: GfG POTD Python Solution"
        run_cmd(f'git commit -m "{commit_msg}"', env=env)
        
        print(f"Day {i:02d} committed for date: {current_date.date()}")

# 3. Final commit for the main README and docs
run_cmd("git add README.md docs/")
run_cmd('git commit -m "Finalize repository documentation and tracker"')

print("\nAll 34 days are committed locally with backdated timestamps!")
print("Next step: Run 'git push origin main' to see your streak on GitHub.")