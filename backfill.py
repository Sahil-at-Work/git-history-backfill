import os
import random
import subprocess
from datetime import datetime, timedelta

current_year = datetime.now().year
previous_year = current_year - 1

start_date = datetime(previous_year, 1, 1)
end_date = datetime(previous_year, 12, 31)

data_file = "history_log.txt"

current_date = start_date
while current_date <= end_date:
    num_commits = random.randint(3, 10)

    for i in range(num_commits):
        hour = random.randint(8, 22)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        commit_dt = current_date.replace(
            hour=hour, minute=minute, second=second
        )
        date_str = commit_dt.strftime("%Y-%m-%dT%H:%M:%S")

        with open(data_file, "a") as f:
            f.write(f"Record logged at {date_str} (entry {i + 1})\n")

        subprocess.run(["git", "add", data_file], check=True)

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str

        commit_message = f"Update log for {date_str}"
        subprocess.run(
            ["git", "commit", "-m", commit_message], env=env, check=True
        )

    current_date += timedelta(days=1)