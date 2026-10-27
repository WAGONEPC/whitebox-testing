from statements import sign_label

def test_positive(): assert sign_label(5) == "positive"
def test_zero(): assert sign_label(0) == "zero"
def test_negative(): assert sign_label(-3) == "negative"
