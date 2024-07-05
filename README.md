  # Assignment 6


This document serves as a comprehensive README for assignment 6, which explores various functionalities through Python functions and closures. Here, we'll delve into the code's purpose, implementation details, and usage examples.

### Function Overview

The provided code implements four distinct functions:

1. **`docstring_checker`**: This function acts as a factory for closures that validate the presence and length of a function's docstring.
2. **`fibonacci`**: This function utilizes closures to generate the Fibonacci sequence iteratively.
3. **`exec_tracker_v1`**: This function creates a decorator closure to track how many times a decorated function is executed using a global dictionary.
4. **`exec_tracker_v2`**: This function creates a decorator closure similar to `exec_tracker_v1`, but it utilizes a user-provided dictionary for execution tracking.

The code imports necessary modules like `time`, `math`, and `functools` for specific functionalities.


### Function Details

**1. `docstring_checker`**

This function constructs a closure that validates a function's docstring based on a minimum length requirement. 

* **Functionality:**
    - It defines a closure `validation` that takes a function (`fn`) as input.
    - Inside `validation`, a minimum docstring length (`min_length`) is set (default: 50 characters).
    - The closure checks if the function (`fn`) has a docstring (`fn.__doc__`) and its length exceeds the `min_length`.
    - It returns `True` if the docstring meets the criteria, otherwise `False`.
* **Usage:**
    ```python
    check_docstring = docstring_checker()

    def my_function():
        """This is a docstring with more than 50 characters."""
        pass

    if check_docstring(my_function):
        print("Function has a valid docstring")
    else:
        print("Function lacks a valid docstring")
    ```

**2. `fibonacci`**

This function employs closures to generate the Fibonacci sequence iteratively. 

* **Functionality:**
    - It defines two initial variables `a` and `b` with values 0 and 1, representing the starting numbers in the Fibonacci sequence.
    - An inner function `next` is created as a closure.
        - Inside `next`, the values of `a` and `b` are updated based on the Fibonacci formula (a becomes the previous b, and b becomes the sum of previous a and b).
        - It returns the new value of `a` which represents the next number in the sequence.
    - The function returns the `next` closure, allowing for iterative generation of Fibonacci numbers.
* **Usage:**
    ```python
    fibonacci_gen = fibonacci()

    for i in range(10):
        print(fibonacci_gen())  # Calls the next function in the closure chain
    ```

**3. `exec_tracker_v1`**

This function constructs a decorator closure to track execution counts of decorated functions using a global dictionary (`fn_timed`).

* **Functionality:**
    - It defines a closure `track_operation` that takes a function (`fn`) as input.
    - Inside `track_operation`:
        - `functools.wraps` decorator is used to preserve the original function's metadata.
        - An inner function `inner` is created to handle decoration.
            - It checks the global dictionary `fn_timed` for the decorated function's name (`fn.__name__`).
            - If the name exists, it increments the corresponding count by 1, otherwise, it initializes the count to 1.
            - It executes the decorated function (`fn`) with provided arguments (`*args`, `**kwargs`).
            - Finally, it returns the result of the function execution.
    - The function returns the `track_operation` closure, which can be used as a decorator.
* **Usage:**
    ```python
    @exec_tracker_v1()
    def my_function():
        # Function implementation
        pass

    my_function()
    my_function()

    # Access execution count from the global dictionary
    print(fn_timed["my_function"])  # Prints the number of times my_function was called
    ```

**4. `exec_tracker_v2`**
    - It defines a closure `track_operation` that takes a dictionary (`count_dict`) as input for execution tracking.
    - Inside `track_operation`:
        - `functools.wraps` decorator is again used to preserve the original function's metadata.
        - An inner function `inner` is created to handle decoration.
            - It retrieves the function name (`fn.__name__`).
            - It checks the provided `count_dict` for the function's name.
            - If the name exists in the dictionary, it increments the corresponding count by 1, otherwise, it initializes the count to 1 in the dictionary.
            - It executes the decorated function (`fn`) with provided arguments (`*args`, `**kwargs`).
            - Finally, it returns the result of the function execution.
    - The function returns the `track_operation` closure, which can be used as a decorator with a custom dictionary.
* **Usage:**
    ```python
    # Create a dictionary to store execution counts
    my_count_dict = {}

    # Use the dictionary with the decorator
    @exec_tracker_v2(my_count_dict)
    def my_function():
        # Function implementation
        pass

    my_function()
    my_function()

    # Access execution count from the user-provided dictionary
    print(my_count_dict["my_function"])  # Prints the number of times my_function was called
    ```

**Key Differences between `exec_tracker_v1` and `exec_tracker_v2`**

* `exec_tracker_v1` relies on a global dictionary `fn_timed`, making the execution counts accessible from anywhere in the program. This might lead to unintended side effects if multiple functions modify the same dictionary.
* `exec_tracker_v2` offers more flexibility by using a user-provided dictionary. This allows for isolated tracking of function executions within specific parts of the codebase. You can have multiple dictionaries for different purposes.

I hope this comprehensive explanation clarifies the functionalities of `exec_tracker_v2` and its distinction from `exec_tracker_v1`.