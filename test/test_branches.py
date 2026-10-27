from source.branches import fee

def test_big_member(): assert fee(150, True) == 0
def test_big_nonmember(): assert fee(150, False) == 5
def test_small(): assert fee(50, False) == 10
