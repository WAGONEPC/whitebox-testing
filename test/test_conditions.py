from conditions import eligible

def test_both_true(): assert eligible(20, True)
def test_age_true_perm_false(): assert not eligible(20, False)
def test_age_false_perm_true(): assert not eligible(17, True)
def test_both_false(): assert not eligible(17, False)
