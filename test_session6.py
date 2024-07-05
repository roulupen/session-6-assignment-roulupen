import pytest
import os
import inspect
import re
import math
import random
import string
import math

import session6
from session6 import fn_timed, exec_tracker_v1, exec_tracker_v2

README_CONTENT_CHECK_FOR = [
    'docstring',
    'fibonacci',
    'exec_tracker_v1',
    'exec_tracker_v2'
]

def test_session6_readme_exists():
    """ Test if ReadMe file exists for session6 """
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_session6_readme_500_words():
    """ Test if ReadMe file has atleast 500 words"""
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_session6_readme_proper_description():
    """ Checks if Readme file has contents mentioned in READMELOOKSGOOD variable or else throw error"""
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_session6_readme_file_for_more_than_10_hashes():
    """ Test to check if Readme file has atleast 10 #"""
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10, "Your ReadMe file needs to have at least 10 #"


def test_session6_indentations():
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_session6_function_name_had_cap_letter():
    """Test to check if any function names have any capital letters"""
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_session6_module_doc_string():
    """Test to check if the module has a docstring"""
    docstring = session6.__doc__
    assert docstring is not None, "Module does not have a docstring!"

def test_example_func_without_docstring():
    def example_func_without_docstring():
        pass

    assert session6.docstring_checker()(example_func_without_docstring) == False, "The function should not have a docstring or it should be less than 50 characters"

def test_example_func_with_short_docstring():
    def example_func_with_short_docstring():
        """Short docstring."""
        pass

    assert session6.docstring_checker()(example_func_with_short_docstring) == False, "The function should have a docstring of length less than 50 characters"

def test_example_func_with_exactly_50_char_docstring():
    def example_func_with_exactly_50_char_docstring():
        """This is a docstring that has exactly 50 characters"""
        pass

    assert session6.docstring_checker()(example_func_with_exactly_50_char_docstring) == False, "The function should have a docstring of exactly 50 characters and should return False"

def test_example_func_with_more_than_50_char_docstring():
    def example_func_with_more_than_50_char_docstring():
        """This is a docstring that has more than fifty characters, making it valid for the test. This is a dummy content......"""
        pass

    assert session6.docstring_checker()(example_func_with_more_than_50_char_docstring) == True, "The function should have a docstring of length greater than 50 characters"

def test_fibonacci_first_call():
    fib_gen = session6.fibonacci()
    assert fib_gen() == 1, "The first call should return the first Fibonacci number, which is 1"

def test_fibonacci_third_call():
    fib_gen = session6.fibonacci()
    fib_gen()  # First call
    fib_gen()  # Second call
    assert fib_gen() == 2, "The third call should return the third Fibonacci number, which is 2"

def test_add_function_once():
    global fn_timed
    fn_timed.clear()

    @exec_tracker_v1()
    def add(a, b):
        return a + b
    
    add(2, 3)
    assert fn_timed['add'] == 1, "The add function should have been called once."

def test_mul_function_once():
    global fn_timed
    fn_timed.clear()

    @exec_tracker_v1()
    def mul(a, b):
        return a * b
    
    mul(2, 3)
    assert fn_timed['mul'] == 1, "The mul function should have been called once."

def test_div_function_once():
    global fn_timed
    fn_timed.clear()

    @exec_tracker_v1()
    def div(a, b):
        return a / b if b != 0 else 'Division by zero'
    
    div(6, 2)
    assert fn_timed['div'] == 1, "The div function should have been called once."

def test_add_function_multiple_times():
    global fn_timed
    fn_timed.clear()

    @exec_tracker_v1()
    def add(a, b):
        return a + b
    
    add(1, 2)
    add(3, 4)
    add(5, 6)

    assert fn_timed['add'] == 3, "The add function should have been called three times."
    assert fn_timed.get('mul', 0) == 0, "The mul function should not have been called."

def test_mul_function_multiple_times():
    global fn_timed
    fn_timed.clear()

    @exec_tracker_v1()
    def mul(a, b):
        return a * b
    
    mul(2, 3)
    mul(4, 5)
    assert fn_timed['mul'] == 2, "The mul function should have been called twice."
    assert fn_timed.get('add', 0) == 0, "The add function should not have been called."

def test_div_function_division_by_zero():
    global fn_timed
    fn_timed.clear()

    @exec_tracker_v1()
    def add(a, b):
        return a + b
    
    @exec_tracker_v1()
    def mul(a, b):
        return a * b

    @exec_tracker_v1()
    def div(a, b):
        return a / b if b != 0 else 'Division by zero'
    
    add(1, 2)
    add(3, 4)
    add(5, 6)
    mul(2, 3)
    mul(4, 5)
    div(6, 4)
    assert fn_timed['add'] == 3, "The add function should have been called three times."
    assert fn_timed['mul'] == 2, "The mul function should have been called twice."
    assert fn_timed['div'] == 1, "The div function should have been called once."

def test_add_function_once_v2():
    fn_timed = {}

    @exec_tracker_v2(fn_timed)
    def add(a, b):
        return a + b
    
    add(2, 3)
    assert fn_timed['add'] == 1, "The add function should have been called once."

def test_mul_function_once_v2():
    fn_timed = {}

    @exec_tracker_v2(fn_timed)
    def mul(a, b):
        return a * b
    
    mul(2, 3)
    assert fn_timed['mul'] == 1, "The mul function should have been called once."

def test_div_function_once_v2():
    fn_timed = {}

    @exec_tracker_v2(fn_timed)
    def div(a, b):
        return a / b if b != 0 else 'Division by zero'
    
    div(6, 2)
    assert fn_timed['div'] == 1, "The div function should have been called once."

def test_add_function_multiple_times_v2():
    fn_timed = {}

    @exec_tracker_v2(fn_timed)
    def add(a, b):
        return a + b
    
    add(1, 2)
    add(3, 4)
    add(5, 6)

    assert fn_timed['add'] == 3, "The add function should have been called three times."
    assert fn_timed.get('mul', 0) == 0, "The mul function should not have been called."

def test_mul_function_multiple_times_v2():
    fn_timed = {}

    @exec_tracker_v2(fn_timed)
    def mul(a, b):
        return a * b
    
    mul(2, 3)
    mul(4, 5)
    assert fn_timed['mul'] == 2, "The mul function should have been called twice."
    assert fn_timed.get('add', 0) == 0, "The add function should not have been called."

def test_div_function_division_by_zero_v2():
    fn_timed = {}

    @exec_tracker_v2(fn_timed)
    def add(a, b):
        return a + b
    
    @exec_tracker_v2(fn_timed)
    def mul(a, b):
        return a * b

    @exec_tracker_v2(fn_timed)
    def div(a, b):
        return a / b if b != 0 else 'Division by zero'
    
    add(1, 2)
    add(3, 4)
    add(5, 6)
    mul(2, 3)
    mul(4, 5)
    div(6, 4)
    assert fn_timed['add'] == 3, "The add function should have been called three times."
    assert fn_timed['mul'] == 2, "The mul function should have been called twice."
    assert fn_timed['div'] == 1, "The div function should have been called once."