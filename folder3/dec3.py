print("This is fourth branch")

def double_number(func):
    def wrapper(*args, **kwargs):
        return func(*args)*2
    return wrapper

@double_number
def sum_numbers(*args):
    s = 0
    for arg in args:
        s+=arg
    return s