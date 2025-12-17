# Jayanth

import asyncio
import time

async def task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} completed")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 2),
        task("C", 2)
    )

start_time = time.time()

asyncio.run(main())

end_time = time.time()

print("Total Execution Time (Async):", end_time - start_time, "seconds")

