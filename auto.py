from pynput.keyboard import Key, Controller
import time

string = "magicl2Love "

keyboard = Controller()
while True:
    amount = int(input("size of triangle ")) + 1
    print("attends 3 secondes")
    time.sleep(3)
    # keyboard.press(Key.ctrl)
    for i in range(amount):
        time.sleep(0.5)
        for a in range(i):
            keyboard.type(string)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    for i in reversed(range(amount - 1)):
        time.sleep(0.5)
        for a in range(i):
            keyboard.type(string)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    # keyboard.release(Key.ctrl)
    print("finished")
