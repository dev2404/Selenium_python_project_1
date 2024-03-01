def add_two_numbers(a, b):
    return a + b

def test_small_numbers():
    assert add_two_numbers(1, 2) == 30, "the sum of 1 and 2 is 3"

def test_large_numbers():
    assert add_two_numbers(100, 300) == 400, "the sum of 100 and 300 is 400"

