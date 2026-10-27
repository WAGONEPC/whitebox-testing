# paths.py
def classify(a, b):
    if a > 0:
        if b > 0:
            return "++"
        else:
            return "+-"
    else:
        if b > 0:
            return "-+"
        else:
            return "--"
