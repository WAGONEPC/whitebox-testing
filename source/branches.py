# branches.py
def fee(amount, is_member):
    if amount >= 100:
        if is_member:
            return 0
        else:
            return 5
    else:
        return 10
