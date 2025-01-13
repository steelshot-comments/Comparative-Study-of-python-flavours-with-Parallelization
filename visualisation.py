import pstats
import matplotlib.pyplot as plt
import os

def get_total_time(prof_file):
    """
    Extract the total execution time from a .prof file.
    """
    if os.path.exists(prof_file):  # Check if the file exists
        stats = pstats.Stats(prof_file)
        return stats.total_tt  # total_tt is the total time in seconds
    else:
        print(f"File {prof_file} not found!")
        return None

# List of Python flavors and their corresponding .prof files
flavors = {
    "CPython": "sequential_n_queens.prof",
    "PyPy": "sequential_n_queens_pypy.prof",
    "Jython": "sequential_n_queens_jython.prof",
    "RustPython": "sequential_n_queens_rustpython.prof",
    "Grumpy": "sequential_n_queens_grumpy.prof",
}

# Extract times from each .prof file
times = []
for flavor, prof_file in flavors.items():
    total_time = get_total_time(prof_file)
    if total_time is not None:
        times.append(total_time)
    else:
        times.append(0)  # Add 0 if the file is missing or not found

# Prepare data for visualization
categories = list(flavors.keys())

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, times, color=['blue', 'green', 'orange', 'red', 'purple'])
plt.ylabel("Execution Time (seconds)")
plt.title("N-Queens Performance by Python Flavor")
plt.xticks(rotation=45)
plt.tight_layout()

# Display the chart
plt.show()