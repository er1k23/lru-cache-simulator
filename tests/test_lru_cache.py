from lru_cache import LRUCache

def test_smoke_put_get():
    cache = LRUCache(2)
    cache.put(1, 10)
    assert cache.get(1) == 10