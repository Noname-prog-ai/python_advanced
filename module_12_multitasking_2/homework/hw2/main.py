import subprocess

def process_count(username: str) -> int:
    cmd = f"ps -u {username} -o pid= | wc -l"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    return int(result.stdout)

def total_memory_usage(root_pid: int) -> float:
    cmd = f"ps -e -o pid,ppid,pmem | grep -E '^\s*{root_pid}|^\s*PID' | awk '{{sum += $3}} END {{print sum}}'"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    return float(result.stdout.strip())

username = "your_username"
root_pid = 1
print(process_count(username))
print(total_memory_usage(root_pid))