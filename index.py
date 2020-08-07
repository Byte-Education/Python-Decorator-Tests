import sys
from contextlib import contextmanager
from io import StringIO


def test_equals(output, printer=True, *args, **kwargs):
    def inner_test(func):
        def wrapper(*args, **kwargs):
            if(func(*args, **kwargs) == output):
                print(f"{func.__name__} Successful")
            else:
                print(f"{func.__name__} Unsuccessful")
            if(printer):
                print(f"Expected Output of {func.__name__}: {output}")
                print(
                    f"Actual Output of {func.__name__}: {func(*args, **kwargs)}")
            return func(*args, **kwargs)
        return wrapper
    return inner_test


def test_true(printer=True, *args, **kwargs):
    def inner_test(func):
        def wrapper(*args, **kwargs):
            if(func(*args, **kwargs)):
                print(f"{func.__name__} Successful")
            else:
                print(f"{func.__name__} Unsuccessful")
            if(printer):
                print(f"Expected Output of {func.__name__}: {True}")
                print(
                    f"Actual Output of {func.__name__}: {func(*args, **kwargs)}")
            return func(*args, **kwargs)
        return wrapper
    return inner_test


def test_false(printer=True, *args, **kwargs):
    def inner_test(func):
        def wrapper(*args, **kwargs):
            if(not func(*args, **kwargs)):
                print(f"{func.__name__} Successful")
            else:
                print(f"{func.__name__} Unsuccessful")
            if(printer):
                print(f"Expected Output of {func.__name__}: {False}")
                print(
                    f"Actual Output of {func.__name__}: {func(*args, **kwargs)}")
            return func(*args, **kwargs)
        return wrapper
    return inner_test


def test_raise(error, printer=True, *args, **kwargs):
    def inner_test(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except error:
                print(
                    f"{func.__name__} with {error.__name__} was Successfully Raised")
                if(printer):
                    print(
                        f"Expected exception raised by {func.__name__}: {error.__name__}")
                    print(
                        f"Actual exception raised by {func.__name__}: {error.__name__}")
            except Exception as e:
                print(
                    f"{func.__name__} with {error.__name__} was Unsuccesffuly Raised")
                if(printer):
                    print(
                        f"Expected exception raised by {func.__name__}: {error.__name__}")
                    print(
                        f"Actual exception raised by {func.__name__}: {type(e).__name__}")
            else:
                print(
                    f"{func.__name__} with {error.__name__} was Unsuccessfully raised as no exceptions were raised!")
                if(printer):
                    print(
                        f"Expected exception raised by {func.__name__}: {error.__name__}")
                    print(
                        f"Actual exception raised by {func.__name__}: No Exception Raised")
        return wrapper
    return inner_test


def test_no_raise(printer=True, *args, **kwargs):
    def inner_test(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                print(
                    f"{func.__name__} raised {type(e).__name__}, when it wasn't supposed to raise any error!")
                if(printer):
                    print(
                        f"Expected Error Raised for {func.__name__}: No Exception")
                    print(
                        f"Actual Error Raised for {func.__name__}: {type(e).__name__}")
            else:
                print(f"{func.__name__} succesfully didn't raise any error!")
                if(printer):
                    print(
                        f"Expected Error Raised for {func.__name__}: No Exception")
                    print(
                        f"Actual Error Raised for {func.__name__}: No Exception")
        return wrapper
    return inner_test


class NullIO(StringIO):
    def write(self, text):
        pass


@contextmanager
def replace_stdin(target):
    orig = sys.stdin
    sys.stdin = target
    yield
    sys.stdin = orig


@contextmanager
def disable_print():
    sys.stdout = NullIO()
    yield
    sys.stdout = sys.__stdout__


def test_input(inputValue, printer=True, returns=False, *args, **kwargs):
    def inner_test(func):
        def wrapper(*args, **kwargs):
            with replace_stdin(StringIO(inputValue)):
                if(returns):
                    return func(*args, **kwargs)
                else:
                    func(*args, **kwargs)
        return wrapper
    return inner_test
