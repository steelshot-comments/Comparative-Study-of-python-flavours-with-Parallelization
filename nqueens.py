import cProfile
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Resource-intensive function: Solving the N-Queens problem
def solve_n_queens(n, row=0, queens=(), solutions=[]):
    if row == n:
        solutions.append(queens)
        return solutions
    for col in range(n):
        if all(col != q and abs(col - q) != len(queens) - i for i, q in enumerate(queens)):
            solve_n_queens(n, row + 1, queens + (col,), solutions)
    return solutions

# Helper function for multiprocessing (global function)
def solve_n_queens_for_multiprocessing(n):
    return solve_n_queens(n)

# Sequential execution of the N-Queens algorithm
def benchmark_sequential_n_queens(n, iterations):
    print("Running sequential N-Queens...")
    start = time.time()
    for _ in range(iterations):
        solve_n_queens(n)
    end = time.time()
    print(f"Sequential N-Queens Time: {end - start:.2f} seconds")

# Parallel execution using multiprocessing
def benchmark_parallel_n_queens_multiprocessing(n, iterations):
    print("Running multiprocessing N-Queens...")
    with ProcessPoolExecutor() as executor:
        start = time.time()
        list(executor.map(solve_n_queens_for_multiprocessing, [n] * iterations))
        end = time.time()
    print(f"Multiprocessing N-Queens Time: {end - start:.2f} seconds")

# Parallel execution using multithreading
def benchmark_parallel_n_queens_multithreading(n, iterations):
    print("Running multithreading N-Queens...")
    with ThreadPoolExecutor() as executor:
        start = time.time()
        list(executor.map(lambda _: solve_n_queens(n), range(iterations)))
        end = time.time()
    print(f"Multithreading N-Queens Time: {end - start:.2f} seconds")

# Run all benchmarks
if __name__ == "__main__":
    n = 12  # Size of the N-Queens board
    iterations = 4  # Number of iterations for computation tasks

    # Profile sequential benchmarks
    print("Profiling sequential execution...")
    cProfile.run("benchmark_sequential_n_queens(n, iterations)", "sequential_n_queens.prof")

    # Profile parallel benchmarks
    print("Profiling parallel execution...")
    cProfile.run("benchmark_parallel_n_queens_multiprocessing(n, iterations)", "parallel_multiprocessing.prof")
    cProfile.run("benchmark_parallel_n_queens_multithreading(n, iterations)", "parallel_multithreading.prof")
