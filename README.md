# LRU Cache Simulator

A clean, from-scratch implementation of an **LRU (Least Recently Used) Cache** with a built-in workload simulator and a simple web-based visualization.

## Overview

This project demonstrates how an LRU cache achieves **O(1)** time complexity for both `get` and `put` operations by combining a doubly linked list (to maintain usage order) and a hash map (to enable fast key lookup). The system also includes a simulator to run realistic workloads and measure cache performance.

## Features

- LRU cache implemented from scratch (no built-in map/queue)
- `get(key)` — returns value or `-1` and updates recency
- `put(key, value)` — inserts/updates and handles eviction
- Configurable cache capacity
- Workload simulation from input files
- Performance metrics: total operations, cache hits/misses, and hit rate (%)
- Unit tests for validation
- Simple HTML visualization of cache behavior

## Project Structure

```
├── data/           # Workload input files
├── docs/           # Complexity notes and explanations
├── src/
│   └── lru_cache/
│       ├── doubly_linked_list.py
│       ├── hashmap.py
│       ├── lru_cache.py
│       └── simulator.py
├── tests/          # Unit tests
└── web/            # HTML visualizer
```

## How It Works

The cache internally maintains:

- **HashMap** — maps `key → node`
- **Doubly Linked List** — head is most recently used, tail is least recently used

**`get(key)`** looks up the key in the hashmap and moves the node to the front.

**`put(key, value)`** updates the node if the key exists, otherwise inserts a new one. If the cache is full, the tail (LRU node) is evicted first.

This guarantees O(1) time complexity for all operations.

## Usage

### Run the Simulator

```bash
python -m src.lru_cache.simulator data/sample_workload.txt
```

Other available workload files:

- `data/empty_workload.txt`
- `data/manual_trace.txt`

### Web Visualization

Open `web/lru_cache_visualizer.html` in a browser for a visual representation of cache state and operations.

### Run Tests

```bash
pytest tests/
```

Test coverage includes hashmap correctness, linked list behavior, LRU cache logic, and simulator output.

## Complexity

| Operation | Time Complexity |
|-----------|----------------|
| `get`     | O(1)           |
| `put`     | O(1)           |

## Notes

- Designed for learning and clarity
- Emphasizes understanding of data structure interaction
- Can be extended (e.g., LFU cache, performance graphs)
