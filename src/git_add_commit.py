#!/usr/bin/env python3
import subprocess
import sys

def git_add_commit(message):
    try:
        # Run `git add .`
        subprocess.run(["git", "add", "."], check=True)
        print("Staged all changes.")

        # Run `git commit -m "message"`
        subprocess.run(["git", "commit", "-m", message], check=True)
        print(f"Committed with message: {message}")

    except subprocess.CalledProcessError as e:
        print(f"Error during git operation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: gac 'Your commit message'")
        sys.exit(1)

    commit_message = sys.argv[1]
    git_add_commit(commit_message)