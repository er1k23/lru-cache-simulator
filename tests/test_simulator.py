from __future__ import annotations

from pathlib import Path

from lru_cache.simulator import run_workload


def test_simulator_basic_workload(tmp_path: Path) -> None:
    # capacity=2
    # Workload:
    # PUT 1 10
    # PUT 2 20
    # GET 1  -> hit (10), makes 1 MRU: [1,2]
    # PUT 3 30 -> evicts LRU=2, cache: [3,1]
    # GET 2  -> miss (-1)
    workload_text = "\n".join(
        [
            "# comment line",
            "PUT 1 10",
            "PUT 2 20",
            "GET 1",
            "PUT 3 30",
            "GET 2",
            "",
        ]
    )

    workload_file = tmp_path / "workload.txt"
    workload_file.write_text(workload_text, encoding="utf-8")

    stats = run_workload(str(workload_file), capacity=2)

    assert stats.total_gets == 2
    assert stats.hits == 1
    assert stats.misses == 1
    assert stats.hit_rate_percent == 50.0

    # final cache (MRU->LRU) should be: 3=30, 1=10
    assert stats.final_cache_mru_to_lru == [(3, 30), (1, 10)]