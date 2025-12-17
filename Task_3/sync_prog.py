# Jayanth

import time

def task(name, delay):
    print(f"Task {name} started")
    time.sleep(delay)
    print(f"Task {name} completed")

start_time = time.time()

task("A", 2)
task("B", 2)
task("C", 2)

end_time = time.time()

print("Total Execution Time (Sync):", end_time - start_time, "seconds")

