class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count

def test_counter_initial_state():
    counter = Counter()
    assert counter.get_count() == 0

def test_counter_increment():
    counter = Counter()
    counter.increment()
    assert counter.get_count() == 1
    counter.increment()
    assert counter.get_count() == 2

def test_counter_reset():
    counter = Counter()
    counter.increment()
    counter.reset()
    assert counter.get_count() == 0