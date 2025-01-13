
| Program | Feature                   | PyPy | Stackless python | RustPython | Grumpy | Pyston |
| ------- | ------------------------- | ---- | ---------------- | ---------- | ------ | ------ |
|         | Multithreading            |      |                  |            |        |        |
|         | Multiprocessing           |      |                  |            |        |        |
|         | Async programming         |      |                  |            |        |        |
|         | Custom concurrency models |      |                  |            |        |        |
|         |                           |      |                  |            |        |        |
### CPU work
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def sum_of_squares(n):
    return sum(i * i for i in range(n))

def benchmark(pool_executor):
    with pool_executor(max_workers=4) as executor:
        results = list(executor.map(sum_of_squares, [10**7] * 4))
    return sum(results)

if __name__ == "__main__":
    print("ThreadPool:", benchmark(ThreadPoolExecutor))
    print("ProcessPool:", benchmark(ProcessPoolExecutor))

### i/o work
import asyncio
import time

async def download_file(file_id):
    await asyncio.sleep(1)  # Simulate I/O delay
    return f"File {file_id} downloaded"

async def benchmark():
    tasks = [download_file(i) for i in range(10)]
    results = await asyncio.gather(*tasks)
    return results

if __name__ == "__main__":
    start = time.time()
    asyncio.run(benchmark())
    print("Time:", time.time() - start)

### Custom concurrency
import stackless

def tasklet_function(n):
    return sum(i * i for i in range(n))

def benchmark():
    tasklets = [stackless.tasklet(tasklet_function)(10**7) for _ in range(4)]
    stackless.run()
    return "Completed"

if __name__ == "__main__":
    print(benchmark())

### **Tools for Timing and Profiling**

- **Timing**: Use Python's `time` or `timeit` module to measure execution time.
- **Resource Usage**: Use `psutil` to measure CPU and memory utilization.
- **Concurrency Profiling**: Tools like `py-spy` or `cProfile`.
### **Expected Outcomes**

- **CPython**: Best performance for multiprocessing but limited for multithreading.
- **PyPy**: Better multithreading performance than CPython due to JIT optimizations.
- **MicroPython**: Minimal concurrency, designed for embedded systems.
- **Stackless Python**: Excels in lightweight concurrency with tasklets.
- **RustPython**: Early-stage support, expect slower performance.
- **Grumpy**: Efficient for I/O-bound tasks due to Go’s goroutines.
- **Pyston**: Comparable to CPython with slight performance improvements.
- Jython : The CPU-bound task will use threads but may not achieve true parallelism due to the JVM's GIL. The I/O-bound task will benefit from threading, as it primarily involves waiting.


### Cpython
- I/O : 2.97
- cpu : 1
- multiprocessing : 0.43
### PyPy
- I/O : 0.60
- cpu : 1
- multiprocessing : 0.38
### Jython
- I/O : 
- cpu : 
- multiprocessing
### RustPython
- I/O
- cpu
- multiprocessing
### Grumpy
- I/O
- cpu
- multiprocessing

### Does big O' notation hold up in parallel processing
Algorithms that work well in single core processing may not be efficient in dividing the work among cores as the time taken to retrieve data from the cores may cause significant overhead compared to the faster processing time. So we need to use algorithms that are optimized for parallel processing.

However, multi-core programs are dividing the work among a constant number of cores and thus the big O' notation is still valid for parallel programs.
Once quantum computers become practical, the complexity of algorithms may change as one qubit can be in a superposition of multiple states simultaneously.
