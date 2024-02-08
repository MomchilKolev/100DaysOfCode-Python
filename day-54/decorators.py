# import time


# # With Decorator
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#     return wrapper_function
#
# @delay_decorator
# def say_hello():
#     print("Hello")
#
# @delay_decorator
# def say_bye():
#     print("Bye")
#
# @delay_decorator
# def say_morning():
#     print("Morning")


# # Without Decorator
# def say_hello():
#     time.sleep(2)
#     print("Hello")
#
#
# def say_bye():
#     time.sleep(2)
#     print("Bye")
#
#
# def say_morning():
#     time.sleep(2)
#     print("Morning")