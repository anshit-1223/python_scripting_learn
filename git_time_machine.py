# ####NEW CODE

# import subprocess
# import time
# from datetime import datetime, timedelta
# import os
# import random
# import sys

# def git_commit_for_each_day(start_date_str, file_to_change):
#     try:
#         start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
#     except ValueError:
#         print("❌ Invalid date format. Use YYYY-MM-DD.")
#         return

#     today = datetime.today().date()

#     # 🔒 Prevent future dates
#     if start_date > today:
#         print("❌ Start date cannot be in the future.")
#         return

#     current_date = start_date

#     while current_date <= today:
#         date_str = current_date.strftime("%Y-%m-%d 12:00:00")

#         env = os.environ.copy()
#         env["GIT_AUTHOR_DATE"] = date_str
#         env["GIT_COMMITTER_DATE"] = date_str

#         # 🔥 just append one blank line per commit
#         try:
#             with open(file_to_change, "a") as f:
#                 f.write("\n")  # <-- only new line
#         except OSError as e:
#             print(f"❌ File write failed: {e}")
#             return

#         # stage file
#         subprocess.run(["git", "add", file_to_change], check=True)

#         # commit
#         commit = subprocess.run(
#             ["git", "commit", "-m", f"Commit for {current_date}"],
#             env=env,
#             stdout=subprocess.DEVNULL,
#             stderr=subprocess.PIPE
#         )

#         if commit.returncode != 0:
#             print("❌ Git commit failed:")
#             print(commit.stderr.decode())
#             print("Stopping to avoid repository corruption.")
#             sys.exit(1)

#         # 🕒 delay to avoid Git race
#         time.sleep(random.randint(2, 4))

#         # push only on today
#         if current_date == today:
#             subprocess.run(["git", "push"], check=True)

#         current_date += timedelta(days=1)


# # ---------- usage ----------
# start_date = input("Enter start date (YYYY-MM-DD): ")
# file_name = input("Enter file name to modify (e.g. notes.txt, README.md): ")

# git_commit_for_each_day(start_date, file_name)





##Clean added lines at last code
import subprocess
import time
from datetime import datetime, timedelta
import os
import random
import sys

def git_commit_for_each_day(start_date_str, file_to_change):
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD.")
        return

    today = datetime.today().date()

    # 🔒 Prevent future dates
    if start_date > today:
        print("❌ Start date cannot be in the future.")
        return

    current_date = start_date
    total_lines_added = 0  # Track total added lines

    while current_date <= today:
        date_str = current_date.strftime("%Y-%m-%d 12:00:00")
        print(date_str)
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str

        # 🔥 Random number of blank lines per day (1-3 for example)
        lines_today = random.randint(1, 3)
        total_lines_added += lines_today

        # Append blank lines
        try:
            with open(file_to_change, "a") as f:
                for _ in range(lines_today):
                    f.write("\n")
        except OSError as e:
            print(f"❌ File write failed: {e}")
            return

        # stage file
        subprocess.run(["git", "add", file_to_change], check=True)

        # commit
        commit = subprocess.run(
            ["git", "commit", "-m", f"Commit for {current_date}"],
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE
        )

        if commit.returncode != 0:
            print("❌ Git commit failed:")
            print(commit.stderr.decode())
            print("Stopping to avoid repository corruption.")
            sys.exit(1)

        # 🕒 delay to avoid Git race
        time.sleep(random.randint(1, 2))

        # push only on today
        if current_date == today:
            subprocess.run(["git", "push"], check=True)

        current_date += timedelta(days=1)

    # 🔄 Cleanup: remove added blank lines
    try:
        with open(file_to_change, "r") as f:
            lines = f.readlines()
        if total_lines_added > 0:
            lines = lines[:-total_lines_added]  # Remove last N lines
        with open(file_to_change, "w") as f:
            f.writelines(lines)
        print(f"✅ Cleanup done: removed {total_lines_added} blank lines")
    except OSError as e:
        print(f"❌ Cleanup failed: {e}")

    # stage file
    subprocess.run(["git", "add", file_to_change], check=True)

    # commit
    commit = subprocess.run(
        ["git", "commit", "-m", f"Commit for {current_date}"],
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE
    )

# ---------- usage ----------
start_date = input("Enter start date (YYYY-MM-DD): ")
file_name = input("Enter file name to modify (e.g. notes.txt, README.md): ")

git_commit_for_each_day(start_date, file_name)
