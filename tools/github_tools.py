import subprocess


def fetch_issue(number):

    cmd = f"gh issue view {number} --json title,body"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        return ""

    return result.stdout
