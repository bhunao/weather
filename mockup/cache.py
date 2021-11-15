from functools import wraps
class My_Cache:
    def __init__(self, cache):
        self.keys = tuple()
        self.cache = cache.cache

    def keys(self) -> dict:
        for key in self.keys:
            if not self.cache.has(key):
                self.keys.discard(key)
        return [*self.keys]

    def get(self, k): # _ should  be private?
        if not self.cache.has(k):
            return None
        return self.cache.get(k)

    def set(self, k, v): # _ should  be private?
        if not self.cache.has(k):
            self.keys += k,
            self.cache.set(k, v)

    def wrapper(func):
        @wraps(func)
        def wrap(self, *args, **kwargs):
            a = (*args, *kwargs)
            if not self.get(a):
                self.set(k)
            return func(*args, **kwargs)
        return wrap
