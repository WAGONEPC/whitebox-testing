# conditions.py
def eligible(age, has_permission):
    if age >= 18 and has_permission:
        return True
    return False
