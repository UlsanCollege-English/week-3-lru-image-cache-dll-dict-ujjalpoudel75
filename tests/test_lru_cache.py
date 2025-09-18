from src.lru_cache import LRUCache

def test_put_get_evict_order():
    c = LRUCache(2)
    c.put("A", 1); c.put("B", 2)
    assert c.get("A") == 1   # A becomes most recent
    c.put("C", 3)            # evicts least recent: B
    assert c.get("B") is None
    assert c.get("A") == 1
    assert c.get("C") == 3
    c.put("D", 4)            # evicts least recent: A
    assert c.get("A") is None and c.get("D") == 4
