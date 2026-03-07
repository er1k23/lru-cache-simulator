# Complexity Analysis (LRU Cache)

## Data structures used
- **HashMap (custom)**: maps `key -> node` for O(1) average lookup.
- **Doubly Linked List**: stores nodes in usage order (MRU near head, LRU near tail).

Because the HashMap stores direct references to list nodes, the cache never scans the list.

## `get(key)` complexity
Steps:
1) HashMap lookup `map.get(key)` → **O(1)** average  
2) If found, move node to front in DLL:
   - `remove(node)` updates a constant number of pointers → **O(1)**
   - `add_front(node)` updates a constant number of pointers → **O(1)**

Total: **O(1)** average time.

## `put(key, value)` complexity
Two cases:

### A) Key already exists
1) HashMap lookup → **O(1)** average
2) Update `node.value` → **O(1)**
3) Move node to front in DLL (`remove` + `add_front`) → **O(1)**

Total: **O(1)** average time.

### B) Key is new
1) HashMap lookup → **O(1)** average
2) If capacity reached, evict LRU:
   - `pop_tail()` removes tail node in DLL → **O(1)**
   - `map.delete(lru.key)` → **O(1)** average
3) Insert new node:
   - `add_front(new_node)` → **O(1)**
   - `map.put(key, new_node)` → **O(1)** average

Total: **O(1)** average time.

## Space complexity
- HashMap stores up to `capacity` entries.
- Doubly linked list stores up to `capacity` nodes.

Total space: **O(capacity)**.