import os
import time

def do_busy_work(time_in_seconds: int) -> float:
    pid: int = os.getpid()
    print(f"\ndo_busy_work, pid={pid}, enter")
    st = time.perf_counter()
    time.sleep(time_in_seconds)
    elapsed_time = time.perf_counter() - st
    print(f"do_busy_work, pid={pid}, exit, elapsed_time={elapsed_time:0.2f} seconds")
    return elapsed_time