import subprocess


def run_cmd(cmd):

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())

    return result.stdout


def get_diff(commit_range):

    cmd = f"git diff {commit_range}"
    return run_cmd(cmd)
