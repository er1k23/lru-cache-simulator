from lru_cache import LRUCache


def test_smoke_put_get():
    cache = LRUCache(2)
    cache.put(1, 10)
    assert cache.get(1) == 10


def test_get_missing_returns_minus_one():
    cache = LRUCache(2)
    assert cache.get(99) == -1


def test_eviction_order_lru():
    # capacity=2
    cache = LRUCache(2)
    cache.put(1, 10)   # cache: 1
    cache.put(2, 20)   # cache MRU->LRU: 2,1
    cache.put(3, 30)   # evict LRU=1, cache: 3,2

    assert cache.get(1) == -1
    assert cache.get(2) == 20
    assert cache.get(3) == 30


def test_get_makes_item_mru():
    cache = LRUCache(2)
    cache.put(1, 10)   # [1]
    cache.put(2, 20)   # [2,1]
    cache.get(1)       # access 1 -> [1,2]
    cache.put(3, 30)   # evict LRU=2 -> [3,1]

    assert cache.get(2) == -1
    assert cache.get(1) == 10
    assert cache.get(3) == 30


def test_put_updates_existing_key():
    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(1, 999)   # update
    assert cache.get(1) == 999


def test_capacity_one():
    cache = LRUCache(1)
    cache.put(1, 10)
    cache.put(2, 20)  # evicts 1
    assert cache.get(1) == -1
    assert cache.get(2) == 20