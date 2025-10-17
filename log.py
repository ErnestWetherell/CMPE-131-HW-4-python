import time

def timestamp(func):
    def wrapper():
        print(time.ctime())  # print the current time
        func()               # call the original function
    return wrapper
