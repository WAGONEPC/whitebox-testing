from dataflow import compute

def test_positive_returns_y(): assert compute(5) == 12
def test_nonpositive_returns_x(): assert compute(-1) == 0
