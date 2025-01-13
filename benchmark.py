import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import asyncio


# CPU-bound task
def cpu_bound_task(n):
    return sum(i * i for i in range(n))


# I/O-bound task simulation
async def io_bound_task():
    await asyncio.sleep(1)  # Simulates I/O delay
    return "Completed"


# Benchmark CPU-bound tasks
def benchmark_cpu():
    print("Benchmarking CPU-bound tasks...")
    with ThreadPoolExecutor(max_workers=4) as executor:
        start = time.time()
        results = list(executor.map(cpu_bound_task, [10**7] * 4))
        end = time.time()
        print(f"Result: {sum(results)}, Time taken: {end - start:.2f} seconds")


# Benchmark I/O-bound tasks
def benchmark_io():
    print("Benchmarking I/O-bound tasks...")
    async def run_io_tasks():
        tasks = [io_bound_task() for _ in range(10)]
        start = time.time()
        results = await asyncio.gather(*tasks)
        end = time.time()
        print(f"Result: {results}, Time taken: {end - start:.2f} seconds")

    asyncio.run(run_io_tasks())


# Benchmark ProcessPool for multiprocessing
def benchmark_process():
    print("Benchmarking multiprocessing...")
    with ProcessPoolExecutor(max_workers=4) as executor:
        start = time.time()
        results = list(executor.map(cpu_bound_task, [10**7] * 4))
        end = time.time()
        print(f"Result: {sum(results)}, Time taken: {end - start:.2f} seconds")


if __name__ == "__main__":
    print("Running benchmarks...")
    benchmark_cpu()
    benchmark_io()
    benchmark_process()
