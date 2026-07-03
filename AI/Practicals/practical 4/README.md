# Practical 4: Informed Search Algorithms

This practical implements two informed (heuristic-based) search algorithms:
1. **Greedy Best-First Search**
2. **A* Search Algorithm**

## Files

- `greedy_search` - Implementation of Greedy Best-First Search algorithm
- `a_star.py` - Implementation of A* Search algorithm

---

## 1. Greedy Best-First Search (`greedy_search`)

### Algorithm Overview
Greedy Best-First Search is an informed search algorithm that uses a heuristic function h(n) to estimate the cost from the current node to the goal. It always expands the node that appears to be closest to the goal.

### Graph Structure
The graph is represented as a dictionary where each node maps to a tuple:
- **First element**: Dictionary of neighbors with edge costs
- **Second element**: Heuristic value h(n) - estimated cost to goal

```python
graph = {
    'S': ({'A': 2, 'E': 3}, 6),  # Node S: neighbors {A:2, E:3}, h(n)=6
    'A': ({'S': 2, 'D': 1}, 3),  # Node A: neighbors {S:2, D:1}, h(n)=3
    ...
}
```

### How It Works
1. Start from the source node
2. Explore all neighbors and add them to queue with their h(n) values
3. Select the node with minimum h(n) (greedy choice)
4. Repeat until destination is reached or no path exists

### Usage
```bash
python greedy_search
```

**Input Example:**
```
Enter Source Vertex: S
```

**Output Example:**
```
A -> 3
E -> 5
Taking minimum h(n) vertex: A
D -> 4
Taking minimum h(n) vertex: D
B -> 2
G -> 0
Taking minimum h(n) vertex: G
Resulting Path: ['S', 'A', 'D', 'G']
```

### Key Characteristics
- **Time Complexity**: O(b^m) where b is branching factor, m is maximum depth
- **Space Complexity**: O(b^m)
- **Optimal**: No (can find suboptimal paths)
- **Complete**: No (can get stuck in loops)

---

## 2. A* Search Algorithm (`a_star.py`)

### Algorithm Overview
A* is an informed search algorithm that uses both:
- **g(n)**: Actual cost from start to current node
- **h(n)**: Heuristic cost from current node to goal
- **f(n) = g(n) + h(n)**: Total estimated cost

A* expands the node with the lowest f(n) value, guaranteeing an optimal path if the heuristic is admissible.

### Graph Structure
Same structure as Greedy Search:
```python
graph = {
    "a": ({"b":1, "d":2, "e":3}, 4),  # Node a: neighbors, h(n)=4
    "b": ({"c":2, "d":1}, 3),         # Node b: neighbors, h(n)=3
    ...
}
```

### How It Works
1. Calculate f(n) = g(n) + h(n) for each neighbor
2. Select node with minimum f(n)
3. Update path cost g(n) as we traverse
4. Continue until goal is reached

### Usage
```bash
python a_star.py
```

**Input Example:**
```
Enter source vertex: a
Enter destination vertex: f
```

### Key Characteristics
- **Time Complexity**: O(b^d) where d is depth of optimal solution
- **Space Complexity**: O(b^d)
- **Optimal**: Yes (if heuristic is admissible: h(n) ≤ actual cost)
- **Complete**: Yes (finds solution if one exists)

---

## Comparison: Greedy vs A*

| Feature | Greedy Best-First | A* Search |
|---------|------------------|-----------|
| **Evaluation Function** | f(n) = h(n) only | f(n) = g(n) + h(n) |
| **Optimality** | Not guaranteed | Guaranteed (if h(n) admissible) |
| **Completeness** | No | Yes |
| **Speed** | Faster (less nodes) | Slower (more thorough) |
| **Use Case** | When speed matters more than optimality | When optimal path is required |

---

## Heuristic Function (h(n))

The heuristic function estimates the cost from a node to the goal:
- **Admissible**: h(n) ≤ actual cost (never overestimates)
- **Consistent**: h(n) ≤ cost(n, n') + h(n')

**Examples:**
- Manhattan distance for grid-based problems
- Euclidean distance for geometric problems
- Straight-line distance for map navigation

---

## Running the Programs

### Prerequisites
- Python 3.x

### Execution
```bash
# Run Greedy Search
python greedy_search

# Run A* Search
python a_star.py
```

---

## Learning Objectives

1. Understand informed search strategies
2. Compare greedy vs optimal search
3. Implement heuristic-based algorithms
4. Analyze time and space complexity
5. Recognize when to use each algorithm

---

## Notes

⚠️ **Note**: The `a_star.py` file contains some syntax errors that need correction:
- Line 8: `A` should be `prev`
- Line 10: `O` should be `0`
- Line 16: Function call should be `a_star` not `greedy_search_rec`

The implementation logic is sound but requires these fixes for execution.

---

## References

- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach*
- Heuristic Search Algorithms
- Graph Search Strategies
