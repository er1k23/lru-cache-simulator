from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import List, Tuple, Optional

from .lru_cache import LRUCache


@dataclass
class SimulationStats:
    total_gets: int
    hits: int
    misses: int
    hit_rate_percent: float
    final_cache_mru_to_lru: List[Tuple[int, int]]


def _parse_line(line: str) -> Optional[Tuple[str, List[int]]]:
    """
    Parse one workload line.
    Supports:
      - PUT <key:int> <value:int>
      - GET <key:int>

    Returns:
      ("PUT", [key, value]) or ("GET", [key]) or None for comments/empty lines.
    """
    s = line.strip()
    if not s or s.startswith("#"):
        return None

    parts = s.split()
    op = parts[0].upper()

    if op == "GET":
        if len(parts) != 2:
            raise ValueError(f"Invalid GET line: {line!r}")
        key = int(parts[1])
        return ("GET", [key])

    if op == "PUT":
        if len(parts) != 3:
            raise ValueError(f"Invalid PUT line: {line!r}")
        key = int(parts[1])
        value = int(parts[2])
        return ("PUT", [key, value])

    raise ValueError(f"Unknown operation {op!r} in line: {line!r}")


def run_workload(workload_path: str, capacity: int) -> SimulationStats:
    """
    Run an LRUCache on the workload file and return stats + final cache contents.

    Keys/values are parsed as ints (fits your HashMap: key % capacity).
    A "hit" is a GET where cache.get(key) != -1.
    """
    cache = LRUCache(capacity)

    total_gets = 0
    hits = 0
    misses = 0

    with open(workload_path, "r", encoding="utf-8") as f:
        for raw_line in f:
            parsed = _parse_line(raw_line)
            if parsed is None:
                continue

            op, args = parsed

            if op == "GET":
                total_gets += 1
                key = args[0]
                result = cache.get(key)
                if result == -1:
                    misses += 1
                else:
                    hits += 1

            elif op == "PUT":
                key, value = args
                cache.put(key, value)

    hit_rate = (hits / total_gets * 100.0) if total_gets > 0 else 0.0
    final_cache = cache.items_mru_to_lru()  # [(key,value), ...] MRU->LRU

    return SimulationStats(
        total_gets=total_gets,
        hits=hits,
        misses=misses,
        hit_rate_percent=hit_rate,
        final_cache_mru_to_lru=final_cache,
    )


def _format_cache_inline(items: List[Tuple[int, int]]) -> str:
    """
    Format cache items in one line:
      k=v, k=v, ...
    Example:
      3=30, 1=10
    """
    if not items:
        return "<empty>"
    return ", ".join(f"{k}={v}" for k, v in items)


def _format_cache_multiline(items: List[Tuple[int, int]]) -> str:
    """
    Format cache items as multiple lines with positions:
      [0] key=... value=...
      [1] key=... value=...
    """
    if not items:
        return "  <empty>\n"
    lines = []
    for i, (k, v) in enumerate(items):
        lines.append(f"  [{i}] key={k} value={v}")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Simulate an LRU cache on a workload file.")
    parser.add_argument("--capacity", type=int, required=True, help="Cache capacity (int >= 0)")
    parser.add_argument("--workload", type=str, required=True, help="Path to workload file")
    args = parser.parse_args()

    stats = run_workload(args.workload, args.capacity)

    print(f"workload: {args.workload}")
    print(f"capacity: {args.capacity}")
    print(
        f"gets={stats.total_gets} "
        f"hits={stats.hits} "
        f"misses={stats.misses} "
        f"hit_rate={stats.hit_rate_percent:.2f}%"
    )

    # удобный вывод финального кеша
    print(f"final_cache(MRU->LRU): {_format_cache_inline(stats.final_cache_mru_to_lru)}")
    print("final_cache_detailed(MRU->LRU):")
    print(_format_cache_multiline(stats.final_cache_mru_to_lru), end="")


if __name__ == "__main__":
    main()