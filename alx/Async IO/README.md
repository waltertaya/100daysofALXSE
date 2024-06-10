# Asynchrous IO

- **Parallelism** -> consists of performing multiple operations at the same time.

- **Multiprocessing** -> is a means to effect parallism, and it entails spreadding tasks over a computer's CPUs or cores. Multiprocessing is well-suited for CPU-bound tasks:

- **Concurrency** -> is slightly broader term than parallelism. It suggests that multiple tasks have the ability to run in an overlapping manner. (There's saying that concurrency does not imply parallelism)

- **Threading** -> is a concurrent execution model whereby multiple `threads` take turns executing tasks. One process can contain multiple threads.

The difference between CPU-bound and I/O-bound tasks lies in what part of the system resources they primarily consume or wait on.

### CPU-bound Tasks
- **Definition**: CPU-bound tasks are those that require a lot of computation and processing power. They spend most of their time using the CPU to perform calculations, process data, or run algorithms.
- **Characteristics**:
  - Heavy computation.
  - Little time waiting for other resources.
  - Examples include image processing, video encoding, complex mathematical calculations, simulations, and data analysis.

### I/O-bound Tasks
- **Definition**: I/O-bound tasks are those that spend most of their time waiting for input/output operations to complete. These operations include reading from or writing to disk, network communication, user input, and database queries.
- **Characteristics**:
  - Frequent waiting for external resources.
  - Often blocked while waiting for I/O operations to complete.
  - Examples include web scraping, reading/writing files, network requests, and interacting with databases.

### Why Threading is More Suitable for I/O-bound Tasks
1. **Concurrency**:
   - I/O-bound tasks spend a lot of time waiting. During this waiting time, the CPU is idle and can be utilized to run other threads.
   - By using threading, multiple I/O-bound tasks can run concurrently, making better use of the CPU while waiting for I/O operations to complete.

2. **Blocking Operations**:
   - In an I/O-bound task, the program often blocks waiting for I/O to finish. Threads allow other tasks to progress while one is blocked.
   - With threading, when one thread is waiting for I/O, other threads can continue to execute, leading to improved overall efficiency.

3. **Simpler Implementation**:
   - For I/O-bound tasks, threading can be simpler to implement than using multiprocessing or asynchronous I/O.
   - Threading libraries in many programming languages provide straightforward abstractions to manage concurrent execution.

### Example Scenarios

#### I/O-bound Example:
Imagine you are writing a program that reads data from multiple files, processes them, and writes results to new files. Without threading, the program might read one file at a time, process it, and then write the result before moving to the next file. This sequential approach would be slow due to the waiting times for file I/O operations. With threading, you can read multiple files concurrently, process them in parallel, and write the results independently, thereby reducing the total time spent waiting for I/O operations.

#### CPU-bound Example:
Consider a program that performs heavy image processing. Each image requires significant computation. Using threading here might not yield significant performance improvements because the CPU is the bottleneck. Instead, using multiple processes (multiprocessing) could be more effective, as it allows the program to take advantage of multiple CPU cores.

### Summary
- **CPU-bound tasks** benefit more from multiprocessing due to the need for more CPU resources.
- **I/O-bound tasks** benefit more from threading since it allows the program to handle multiple I/O operations concurrently, making better use of the CPU while waiting for I/O operations to complete.

## Notes

- Concurrency encompasses both multiprocessing (ideal for CPU-bound tasks) and threading (suited for IO-bound tasks). Multiprocessing is a form of parallelism, with parallelism being a specific type (subset) of concurrency.

- Over the last few years, a separate design has been more comprehensively built into CPython: asynchronous IO, enabled through the standard library’s asyncio package and the new async and await language keywords. To be clear, async IO is not a newly invented concept, and it has existed or is being built into other languages and runtime environments, such as Go, C#, or Scala.

- The asyncio package is billed by the Python documentation as a library to write concurrent code. However, async IO is not threading, nor is it multiprocessing. It is not built on top of either of these.


## Subroutine and coroutine

- **Subroutine**: A block of code that can be called as needed, When is called control of the program is transferred to that sub routine. When the work is done, control is return back to the main program/thread. `Subroutine can not be paused and resumed, they run until done.`

- **Coroutine**: Is a special kin of function that can have its executions paused and resumed. This is possible because they maintain there states between there pauses. Applications -> I/O Operations, Database Queries, HTTP Requests.