# Python Decorator Tests

A Python file that utilizes Decorators as Unit Tests rather than unittest and its assertions.

## Description

The functions from this repository serve as Python Decorators. It also works best on functions that don't print but rather return values. Having said that, there are decorators available to help with disabling the printing of a function and only printing values from the decorator itself.

## Testing Decorators

|     Name      | Function / Decorator |                                                                                       Description                                                                                       |               Use Case                |
| :-----------: | :------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------: |
|  test_equals  |      Decorator       |                                                 A way to test the output of a function to see if the output matches the desired output                                                  |       @test_equals(output = 5)        |
|   test_true   |      Decorator       |                                                                A way to test if the function returns true when it should                                                                |              @test_true               |
|  test_false   |      Decorator       |                                                               A way to test if the function returns false when it should                                                                |              @test_false              |
|  test_raise   |      Decorator       |                 A way to test if a function raises a specific exception. If the test notices a different exception is thrown, it will state what exception was thrown.                  |        @test_raise(ValueError)        |
| test_no_raise |      Decorator       |                                          A way to see if a function catches all exceptions. If not, it will say what exception wasn't caught.                                           |            @test_no_raise             |
| replace_stdin |       Function       | A way to override the input function, used mainly in `test_input`. Replaces input function with specified value in parameter. After usage, will return input to original functionality. | with replace_stdin(StringIO("Hello")) |
| disable_print |       Function       |                                                                 Disable a functions ability to print out to the console                                                                 |         with disable_print()          |
|  test_input   |      Decorator       |             A way to test a function with a user input. Utilizes `replace_stdin` to override the natural input function before resetting it to its original functionality.              |         @test_input("Hello")          |

## Code Usage Example

    @test_equals(1)
    def testOutput():
      return 1
    testOutput() # Will print out: "testOutput Successful"

    @test_raise(ValueError)
    def raiseError():
      return int("A") 
    raiseError() # Will print out "raiseError with ValueError Successfully Raised" 

## Notes

Feel free to clone this and use this when testing. It works similarly to the `unittest` package, but as decorators instead of assertion statements.
