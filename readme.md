# Comparing the parallelization capabilities of different python flavours

## Intro
Benchmarking tool: cProfile
Algorithm used: N Queens problem
Why the algorithm was chosen: The N Queens problem spends a lot of time performing operations on the CPU

### **Tools for Timing and Profiling**

### **Expected Outcomes**
- **CPython**: Best performance for multiprocessing but limited for multithreading.
- **PyPy**: Better multithreading performance than CPython due to JIT optimizations.
- **MicroPython**: Minimal concurrency, designed for embedded systems.
- **Stackless Python**: Excels in lightweight concurrency with tasklets.
- **RustPython**: Early-stage support, expect slower performance.
- **Grumpy**: Efficient for I/O-bound tasks due to Go’s goroutines.
- **Pyston**: Comparable to CPython with slight performance improvements.
- Jython : The CPU-bound task will use threads but may not achieve true parallelism due to the JVM's GIL. The I/O-bound task will benefit from threading, as it primarily involves waiting.

## Actual output
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
