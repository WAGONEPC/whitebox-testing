from paths import classify

def test_pp(): assert classify(1,1) == "++"
def test_pn(): assert classify(1,-1) == "+-"
def test_np(): assert classify(-1,1) == "-+"
def test_nn(): assert classify(-2,-3) == "--"
