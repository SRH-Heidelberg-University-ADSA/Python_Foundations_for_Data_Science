# Python Coding Assignments : 100 points

## Assignment 1 — Easy/Medium: Fibonacci Staircase (30 points)

**Problem Statement**

You are climbing a staircase with `n` steps. At each step you can climb either **1 step** or **2 steps**. Your task is to find how many distinct ways you can reach the top.

**Examples**
```
n = 2  →  2 ways:  [1+1, 2]
n = 3  →  3 ways:  [1+1+1, 1+2, 2+1]
n = 5  →  8 ways
```

**Tasks**

1. mention the best time and space complexity of the program achieved.
2. if you have multiple ways to solve the problem then keep all approaches in the code.

**Constraints**
- `1 <= n <= 40`
- Do not use any external libraries

**What to submit**
- Your Python file with all all implementations
- A short paragraph explaining the difference in time complexity between the the different approaches

---

## Assignment 2 — Hard: Travelling Salesman Problem (70 points)

**Problem Statement**

A salesman needs to visit `n` cities exactly once and return to the starting city. Given a matrix of distances between every pair of cities, find the **shortest possible route** that visits all cities and returns to the origin.

**Input format**
```python
# dist[i][j] = distance from city i to city j
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
# Expected output: 80  (route: 0 → 1 → 3 → 2 → 0)
```

**Tasks**

1. Implement a **brute force** solution `tsp_brute(dist)` that tries all permutations of cities and returns the minimum distance. What is the time complexity?
2. Implement a **dynamic programming** solution `tsp_dp(dist)` using bitmask DP. This is the Held-Karp algorithm — research it and implement it. What is the time complexity compared to brute force?
3. Test both solutions on the following inputs and compare their runtimes:
   - 4 cities
   - 8 cities (random distances)
   - 12 cities (random distances)
4. *(Bonus)* Implement a **greedy nearest-neighbour heuristic** `tsp_greedy(dist)`. It won't always find the optimal route — show a case where it fails.

**Constraints**
- `2 <= n <= 15` for the DP solution
- Cities are numbered `0` to `n-1`
- Distance matrix is symmetric: `dist[i][j] == dist[j][i]`
- Do not use any TSP libraries

**What to submit**
- Your Python file with all implementations
- A short write-up comparing the three approaches (brute force, DP, greedy) in terms of correctness and performance

---
