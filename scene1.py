
import time
def U1():
    print("hi")

def U2():
    print("hello")

def U3():
    print("hey")

def ex():
    print("wass up")


def upgrade():#this is the main state
    print("text goes here")
    time.sleep(2)
    print("what will you do?")
    user_input = input()
    if user_input == "1":
        U1()
    elif user_input == "2":
        U2()
    elif user_input == "3":
        U3()
upgrade()
