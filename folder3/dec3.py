print("This is fourth branch")

def double_number(func):
    def wrapper(*args, **kwargs):
        return func(*args)*2
    return wrapper


@double_number
def sum_numbers(*args):
    ss = 0
    for arg in args:
        ss+=arg
    return ss

print(sum_numbers(1,5,6))