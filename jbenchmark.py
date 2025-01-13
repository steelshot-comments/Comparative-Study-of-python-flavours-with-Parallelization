import time
from threading import Thread

# CPU-bound task
def cpu_bound_task(n):
    return sum(i * i for i in range(n))

# Thread worker function for CPU-bound tasks
def thread_worker(results, idx, n):
    results[idx] = cpu_bound_task(n)

# Benchmark CPU-bound tasks using threading
def benchmark_cpu():
    print("Benchmarking CPU-bound tasks with threading...")
    num_threads = 4
    n = 10**7
    threads = []
    results = [0] * num_threads
    start = time.time()

    for i in range(num_threads):
        thread = Thread(target=thread_worker, args=(results, i, n))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = time.time()
    print(f"Result: {sum(results)}, Time taken: {end - start:.2f} seconds")

# Simulate an I/O-bound task
def io_bound_task():
    time.sleep(1)  # Simulate I/O delay
    return "Completed"

# Benchmark I/O-bound tasks using threading
def benchmark_io():
    print("Benchmarking I/O-bound tasks with threading...")
    num_threads = 10
    threads = []
    results = [None] * num_threads
    start = time.time()

    for i in range(num_threads):
        thread = Thread(target=lambda idx: results.__setitem__(idx, io_bound_task()), args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = time.time()
    print(f"Result: {results}, Time taken: {end - start:.2f} seconds")

if __name__ == "__main__":
    print("Running benchmarks in Jython...")
    benchmark_cpu()
    benchmark_io()
