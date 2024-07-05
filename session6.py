"""
This is assignment 6, where we will be implementing the following functions:
1. `docstring_checker`: A closure that validates whether a function has a docstring longer than a specified minimum length (`min_length`).

2. `fibonacci`: Generates Fibonacci numbers sequentially using a closure.

3. `exec_tracker_v1`: Tracks the number of times functions are executed using a global dictionary `fn_timed`.

4. `exec_tracker_v2`: Tracks the number of times functions are executed using a user-defined dictionary `count_dict`.
"""
fn_timed = {}

def docstring_checker():
    """
    This function checks if a given function has a docstring.

    Parameters:
    func (function): The function to be checked.

    Returns:
    bool: True if the function has a docstring, False otherwise.
    """
    min_length = 50

    def validation(fn):
        nonlocal min_length
        if fn.__doc__ and len(fn.__doc__) > min_length:
            return True
        return False
    return validation

def fibonacci():
    """
    The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones.
    It starts with 0 and 1, and each subsequent number is the sum of the previous two.
    This sequence is widely used in mathematics and computer science, as it has various applications such as
    generating random numbers, analyzing algorithms, and solving optimization problems.
    The sequence is defined by the recursive formula: F(n) = F(n-1) + F(n-2), with F(0) = 0 and F(1) = 1.
    """
    a, b = 0, 1

    def next():
        nonlocal a, b
        a, b = b, a+b
        return a
    return next

def exec_tracker_v1():
    """
    This function returns a closure that can be used as a decorator to track the number of times a function is called.
    The closure function, when applied as a decorator to another function, keeps track of the number of times the decorated function is called.
    It uses a global dictionary `fn_timed` to store the number of times each function is called.
    The closure function returns the result of the decorated function after updating the count in the `fn_timed` dictionary.
    """
    def track_operation(fn):
        from functools import wraps

        @wraps(fn)
        def inner(*args, **kwargs):
            # global scoped dictionary to store the number of times a function is called
            global fn_timed

            fn_timed[fn.__name__] = fn_timed.get(fn.__name__, 0) + 1

            # executes the function and returns the result
            return fn(*args, **kwargs)
        return inner
    return track_operation

def exec_tracker_v2(count_dict):
    """
    This function returns a closure that can be used as a decorator to track the number of times a function is called.
    """
    def track_operation(fn):
        from functools import wraps

        @wraps(fn)
        def inner(*args, **kwargs):
            # checks if the function name is in the dictionary
            # if it is, then increment the value by 1 else set it to 1
            count_dict[fn.__name__] = count_dict.get(fn.__name__, 0) + 1

            # executes the function and returns the result
            return fn(*args, **kwargs)
        return inner
    return track_operation
