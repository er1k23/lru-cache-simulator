from lru_cache.hashmap import HashMap


def test_put_and_get():
    hm = HashMap(10)

    hm.put(1, "A")
    hm.put(2, "B")

    assert hm.get(1) == "A"
    assert hm.get(2) == "B"


def test_update_existing_key():
    hm = HashMap(10)

    hm.put(1, "A")
    hm.put(1, "B")   # update same key

    assert hm.get(1) == "B"


def test_get_nonexistent_key():
    hm = HashMap(10)

    assert hm.get(99) is None


def test_delete_key():
    hm = HashMap(10)

    hm.put(1, "A")
    hm.delete(1)

    assert hm.get(1) is None


def test_collision_handling():
    hm = HashMap(5)

    # these collide when capacity = 5
    hm.put(1, "A")
    hm.put(6, "B")
    hm.put(11, "C")

    assert hm.get(1) == "A"
    assert hm.get(6) == "B"
    assert hm.get(11) == "C"