# Data Structures
|Name|Code|Strength|Weakness|Use case|
|--|--|--|--|--|
|Dynamic Arrays|[C](./src/c/vector.c), [Python](./src/python/_vector.py)| **O(1)** read/write at index, add/remove at end| **O(N)** search, insert/delete at middle|random access, memory efficient, rapid sort O(nlogn)|
|Stack|||||
|Linked-Lists|[C](./src/c/singly-linked-list.c), [Python](./src/python/_singly-linked-list.py)| **O(1)** add or pop end/front, insert to middle if already there, no shifting | **O(N)** find, insert/remove middle if starting from head |maleability and changes in the middle|
|Queues|||||
|Hash Tables|||||
|Binary Trees|||||
|Graph|||||
|Tries|||||
|Heaps|||||

#### Concepts
|Title|Definition|
|-|-|
|Bit manipulation|Bit manipulation involves using bitwise operators to modify individual bits within a binary number. This can include operations like shifting bits left or right, setting a specific bit to 1 or 0, or flipping bits. It's often used for tasks that require high performance, compact storage, or direct hardware control.|
|Recursion|Recursion is a programming technique where a function calls itself to solve smaller parts of a problem, until it reaches a condition that stops further calls. This is useful for problems that can be broken down into similar, smaller problems.|
|Memoization/dynamic programming|Memoization is a technique where you store the results of expensive function calls and return the cached result when the same inputs occur again. This avoids repeated calculations and speeds up the program. <br><br> Dynamic programming is an approach that breaks down a complex problem into simpler subproblems and solves each of these subproblems just once, storing their solutions. When a larger problem depends on the solutions of these smaller problems, it uses these stored solutions directly, optimizing the overall computation process. Both techniques are useful for improving performance in problems that involve many repeated calculations.|
|Memory (stack/heap)|A stack is a region of memory where data is added or removed in a last-in, first-out order. It's used for static memory allocation, such as for function call management and local variables.<br><br>A heap is a region of memory used for dynamic memory allocation, where blocks of memory can be allocated and freed in any order. This flexibility supports more complex data structures like trees, graphs, and dynamically resized arrays. Both the stack and the heap help manage memory in programs, but they do so in different ways and for different types of data.|
|Big O Notation|Big O notation is a way to describe the efficiency of an algorithm, specifically how its runtime or space requirements grow as the size of the input increases. It focuses on the worst-case scenario, ignoring constants and less significant terms to give a simplified understanding of an algorithm's performance as the input becomes very large. For example, an algorithm with a time complexity of O(n) means its runtime increases linearly with the input size|