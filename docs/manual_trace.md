# Manual Trace (By Hand) — Required Verification

This section verifies correctness **by hand** on a small workload and confirms the expected final cache state and hit/miss counts.

## Setup
- Cache policy: **LRU**
- Capacity: **2**
- Cache order shown as: **MRU → LRU**
- `GET` returns `-1` on miss, otherwise the value.
- On every successful `GET` and any `PUT` (insert/update), the key becomes **MRU**.
- On overflow, evict **LRU** (the tail item).

## Workload

PUT 1 10
PUT 2 20
GET 1
PUT 3 30
GET 2
GET 3

## Step-by-step
1) PUT 1 10  -> cache: 1=10
2) PUT 2 20  -> cache: 2=20, 1=10
3) GET 1 = 10 (hit) -> cache: 1=10, 2=20
4) PUT 3 30 -> evict LRU=2 -> cache: 3=30, 1=10
5) GET 2 = -1 (miss) -> cache: 3=30, 1=10
6) GET 3 = 30 (hit) -> cache: 3=30, 1=10

## Expected
- total_gets=3
- hits=2
- misses=1
- hit_rate=66.67%
- final_cache(MRU->LRU)=3=30, 1=10

## Confirm with simulator
Run:
PYTHONPATH=src python -m lru_cache.simulator --capacity 2 --workload data/manual_workload.txt

Result matches expected stats and final cache.