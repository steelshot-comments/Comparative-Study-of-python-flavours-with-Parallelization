# Intro

## Algorithm used
We will use the N Queens problem because of it's

1. CPU and memory intensive nature
The N-Queens problem requires finding all the ways to place n queens on an n×n chessboard such that no two queens threaten each other. This involves:
- Exploring large solution spaces
- Performing checks for valid queen placements
- Recursive backtracking, which is computationally expensive for higher n.

The algorithm also uses memory for storing partial board states and managing the recursive call stack.
Thus, it tests the ability of Python flavors to handle both computation and memory management efficiently.

2. Well-Defined Parallelization Opportunities
Placing a queen in column i doesn't affect placing one in column j, as long as constraints are respected.
This independence allows us to explore branches concurrently.

3. Adjustable Complexity
The problem's difficulty can be adjusted simply by changing n, making it suitable for lightweight or heavy benchmarking.

1. CPU-Intensive Parts

The CPU-intensive sections of the N-Queens algorithm are:
Constraint Checking: Each queen placement involves checking:
Column conflicts: O(1)O(1) per placement.
Diagonal conflicts: O(n)O(n) per placement (depends on board size nn).

Recursive Backtracking: For each queen placement, recursive calls are made to explore solutions for the subsequent rows. This results in an exponential number of calls as nn increases.

For example, the number of recursive calls grows roughly as n!n! for nn-queens because of the factorial growth in permutations.

2. Parallelizable Parts

The main opportunity for parallelism lies in the independence of branches:

For each row (starting at the root level of recursion), placing a queen in different columns spawns independent subproblems. These can be computed in parallel.
Example: For the first row, placing a queen in column 00, 11, 22, ..., n−1n−1 are all separate recursive branches that can run concurrently.

In terms of implementation:
Sequential Algorithm: Processes one branch at a time.
Parallel Algorithm: Uses multiprocessing or multithreading to explore multiple branches simultaneously.

## Flavours used for comparisn
CPython: The base flavour of python, which is the most common.
PyPy: Optimized JustInTime interpretation which makes it faster and more compliant than python
RustPython: Compiles the python code to rust whcih handles cpu intensive tasks better
Jython: Compiles python to Java which has better threading capabilites as it is not restricted by a global interpreter lock
Grumpy: Compiles python to Go which has better threading capabilities

# **Expected Outcomes**
- **CPython**: Best performance for multiprocessing but limited for multithreading.
- **PyPy**: Better multithreading performance than CPython.
- **MicroPython**: Minimal concurrency, designed for embedded systems.
- **Stackless Python**: Excels in lightweight concurrency with tasklets.
- **RustPython**: Early-stage support, expect slower performance.
- **Grumpy**: Efficient for I/O-bound tasks due to Go’s goroutines.
- **Pyston**: Comparable to CPython with slight performance improvements.
- Jython : The CPU-bound task will use threads but may not achieve true parallelism due to the JVM's GIL. The I/O-bound task will benefit from threading, as it primarily involves waiting.

# Actual output


# Does big O' notation hold up in parallel processing
Algorithms that work well in single core processing may not be efficient in dividing the work among cores as the time taken to retrieve data from the cores may cause significant overhead compared to the faster processing time. So we need to use algorithms that are optimized for parallel processing.
However, multi-core programs are dividing the work among a constant number of cores and thus the big O' notation is still valid for parallel programs.
Once quantum computers become practical, the complexity of algorithms may change as one qubit can be in a superposition of multiple states simultaneously.
