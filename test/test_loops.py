from loops import sum_first

def test_zero(): assert sum_first(0) == 0
def test_one(): assert sum_first(1) == 1
def test_five(): assert sum_first(5) == 15
def test_negative(): assert sum_first(-2) == 0
