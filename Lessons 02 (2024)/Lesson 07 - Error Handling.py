"""
How to properly handel errors in python.
Key takeaways:
    * Always expect the type of error and handel it accordingly.
    * If a broader exception is used, make sure to log using the "logging" module.
    * logging.exception() is ideal for capturing complete error details directly from an exception block.
    * You can use "pass" to ignore the error. "continue", or "break" if you are in a loop.
    * Use "raise" if you want to raise the error, but want to do stuff before raising it.
    * Use "raise Exception('')" to print a custom message.
    * Use "finally" to run a code, whether an exception is raised or not.
    * Use "else" to run a code if amn exception is not raised.
    * You can also use custom exceptions.
"""


import logging


class MyCustomException(Exception):
    def __init__(self, item):
        # Save item for later use:
        self.item = item
        self.message = f"Value {value} is either ValueError or ZeroDivisionError"
        # Call the initializer of the base Exception class, passing in the message attribute:
        super().__init__(self.message)
    pass


values = [10, 5, 0, "Hello", None]

for value in values:
    try:
        print(10 / int(value))
    except (ValueError, ZeroDivisionError) as e:
        print("ValueError or ZeroDivisionError has occurred")
        raise MyCustomException(value)
    except AttributeError as e:
        print("AttributeError has occurred")
        pass
    except Exception as e:
        logging.exception(e)
    else:
        print("No errors")
    finally:
        print("Finished value\n")
