# Lab: Parallelization with Python

## Overview

This lab introduces parallel and asynchronous processing in Python, essential skills for handling big data workloads efficiently. You'll learn to leverage multiple CPU cores and implement concurrent operations to significantly reduce computation time.

## Learning Objectives

Upon completion of this lab, you will be able to:
- Implement parallel processing using Python's `multiprocessing` library
- Build asynchronous operations using Python's `asyncio` library
- Compare performance between serial, parallel, and asynchronous execution
- Apply map-reduce concepts as preparation for distributed computing with Spark
- Optimize data science computations through effective parallelization strategies

## Prerequisites

### Technical Requirements
- **Python**: Version 3.8 or higher
- **Package Manager**: UV package manager installed ([Installation Guide](https://github.com/astral-sh/uv))
  - macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Windows: `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`
- **Development Environment**: 
  - VSCode with Remote-SSH extension
  - Jupyter extension for VSCode
  - Git for version control

### AWS Environment
- Active AWS account with appropriate permissions
- Amazon EC2 instance (t2.medium or larger recommended for multiprocessing)
- Security group configured for SSH access
- If on campus, use Saxanet wifi for AWS connectivity

### Required Python Libraries
- `multiprocessing` (built-in)
- `asyncio` (built-in)
- `requests` (for API calls)
- `numpy` (for data manipulation)
- `time` (built-in, for performance measurement)

## Environment Setup

**Important**: This lab is performed on an Amazon EC2 instance that you will connect to via VSCode Remote-SSH. All development and execution happens on the EC2 instance, not on your local machine.

### 1. Connect to EC2 via VSCode
1. Open VSCode on your local machine
2. Install Remote-SSH extension if not already installed
3. Connect to your EC2 instance using the Remote-SSH extension
4. Once connected, you'll be working directly on the EC2 instance

### 2. Clone and Set Up Repository
Once connected to your EC2 instance via VSCode:
```bash
# Clone this repository to your EC2 instance
git clone <your-assignment-repo-url>
cd <your-assignment-repo>

# Install dependencies using UV
uv sync

# Activate the virtual environment
source .venv/bin/activate  # On Linux/macOS
```

### 3. Jupyter Setup
```bash
# Install Jupyter kernel for the virtual environment
uv pip install ipykernel
python -m ipykernel install --user --name=parallel-python
```

**Important**: When opening the notebook files in Jupyter or VSCode, make sure to select the `parallel-python` kernel that you just created. This ensures you're using the correct virtual environment with all required dependencies.

### 4. Verify Installation
Run this verification script to ensure your environment is properly configured:

```bash
# Create and run a verification script
python -c "
import multiprocessing as mp
import asyncio
import requests
import numpy as np
print(f'Multiprocessing available cores: {mp.cpu_count()}')
print(f'NumPy version: {np.__version__}')
print(f'Requests version: {requests.__version__}')
print('Environment setup complete!')
"
```

## Grading Rubric (Total: 50 Points)

### Part 1: Multiprocessing Notebook (30 Points)
- **Problem 1** - Pool.starmap() Implementation (8 points)
  - Correct implementation of row-wise common items: 6 points
  - Proper use of Pool.starmap(): 2 points

- **Problem 2** - CPU-Intensive Work Performance Comparison (12 points)
  - Part A - Serial execution with map(): 3 points
  - Part B - Parallel with CPU count pool: 4 points
  - Part C - Parallel with optimal pool size: 4 points
  - Performance analysis and speedup calculation: 1 point

- **Problem 3** - Large-Scale Data Processing (10 points)
  - Correct normalization function with edge case handling: 3 points
  - Serial processing implementation: 2 points
  - Parallel processing with Pool.map(): 3 points
  - Performance comparison and speedup analysis: 2 points

### Part 2: Asynchronous Programming (20 Points)
- **Brewery API Implementation** (20 points)
  - `get_brewery_count()` function: 6 points
  - `async_get_brewery_count()` wrapper: 5 points
  - `get_brewery_counts_for_states()` orchestration: 5 points
  - Performance improvement demonstration: 2 points
  - Clean code and proper JSON output format: 2 points

## Assignment Components

### 1. Multiprocessing Notebook
Complete the exercises in [`parallelization-with-python.ipynb`](./parallelization-with-python.ipynb):
- Learn synchronous vs asynchronous execution models
- Implement solutions using Pool.map(), Pool.starmap(), and async variants
- Complete three problems demonstrating different parallelization techniques
- Results are automatically saved to `soln.json`

### 2. Asynchronous Brewery API Script
Complete the implementation in [`brewery-async.py`](./brewery-async.py):
- Implement serial and async versions of brewery data fetching
- Use the OpenBrewery DB API to retrieve brewery counts by state
- Compare performance between serial and async approaches
- Results are automatically saved to `async.json`

## Submission Instructions

1. **Development Environment**
   - Complete all work on your EC2 instance
   - Use VSCode with Jupyter extension for notebook development
   - Test all code thoroughly before submission

2. **Required Files**
   Your repository must contain:
   - `parallelization-with-python.ipynb` (completed notebook)
   - `soln.json` (auto-generated from notebook)
   - `brewery-async.py` (completed script)
   - `async.json` (auto-generated from script)
   - `script.py` (provided helper file)
   - `README.md` (this file)
   - `.gitignore`

3. **Submission Process**
   - Ensure all code runs without errors
   - Verify JSON output files are properly formatted
   - Commit all changes to your GitHub repository
   - Create a final commit with message: `"final-submission"`
   - **IMPORTANT**: Do not modify the repository after the final submission commit

## Output File Formats

### `soln.json` Format
The notebook automatically generates this file with your results:
```json
{
  "prob1": "[[2, 3], [6], [11, 12], [21]]",
  "prob2": {
    "part1": 6.012491918998421, 
    "part2": 3.060048302002542, 
    "part3": 7.091866148999543
  },
  "prob3": "[[0.0, 0.33, 0.67, 1.0], ...]",
  "host": "your-ec2-hostname"
}
```

### `async.json` Format
The brewery script automatically generates this file:
```json
{
  "result": "async version was 49.92% faster than the serial version",
  "host": "your-ec2-hostname"
}
```

## Tips for Success

1. **Multiprocessing Best Practices**
   - Use `mp.cpu_count()` to determine available cores
   - Remember that parallelization has overhead - it's not always faster for small tasks
   - Close pools properly to avoid resource leaks

2. **Async Programming Tips**
   - Use `asyncio.gather()` for concurrent execution
   - Remember that async is beneficial for I/O-bound operations (like API calls)
   - Handle API rate limits appropriately

3. **Debugging Strategies**
   - Test with small datasets first
   - Use print statements to track execution flow
   - Verify intermediate results before full-scale runs

## Additional Resources

- [Python Multiprocessing Documentation](https://docs.python.org/3/library/multiprocessing.html)
- [Python Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [OpenBrewery DB API Documentation](https://www.openbrewerydb.org/documentation)


