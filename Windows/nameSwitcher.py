from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

# Press and release space
print("Step 1:")
print("You must fix the first record yourself and then click in the 'given names' cell on the first record. Then come back here and follow the nest step.")
print()
print("Step 2:")
print("After answering this question please switch back into the family history tab and click on the first cell. This program will wait 5 seconds for you to switch after you press the 'enter' key on the next line.")
recordNum = input("How many records do you need to switch the names on? ")

def switchNames(wait = 0.05):
     sleep(wait)
     keyboard.press(Key.ctrl)
     sleep(wait)
     keyboard.press(Key.right)
     sleep(wait)
     keyboard.release(Key.right)
     sleep(wait)
     keyboard.release(Key.ctrl)
     sleep(wait)

     sleep(wait)
     keyboard.press(Key.ctrl)
     sleep(wait)
     keyboard.press('x')
     sleep(wait)
     keyboard.release('x')
     sleep(wait)
     keyboard.release(Key.ctrl)
     sleep(wait)

     sleep(wait)
     keyboard.press(Key.tab)
     sleep(wait)
     keyboard.press(Key.left)
     sleep(wait)
     keyboard.release(Key.left)
     sleep(wait)
     keyboard.release(Key.tab)
     sleep(wait)

     sleep(wait)
     keyboard.press(Key.ctrl)
     sleep(wait)
     keyboard.press('v')
     sleep(wait)
     keyboard.release('v')
     sleep(wait)
     keyboard.release(Key.ctrl)
     sleep(wait)

     sleep(wait)
     keyboard.press(Key.shift)
     sleep(wait)
     keyboard.press(Key.end)
     sleep(wait)
     keyboard.release(Key.shift)
     sleep(wait)
     keyboard.release(Key.end)
     sleep(wait)

     sleep(wait)
     keyboard.press(Key.ctrl.value)
     sleep(wait)
     keyboard.press('x')
     sleep(wait)
     keyboard.release('x')
     sleep(wait)
     keyboard.release(Key.ctrl.value)
     sleep(wait)

     sleep(wait)
     keyboard.press(Key.shift)
     sleep(wait)
     keyboard.press(Key.tab)
     sleep(wait)
     keyboard.release(Key.tab)
     sleep(wait)
     keyboard.release(Key.shift)
     sleep(wait)

     sleep(wait)
     keyboard.press(Key.ctrl)
     sleep(wait)
     keyboard.press('v')
     sleep(wait)
     keyboard.release('v')
     sleep(wait)
     keyboard.release(Key.ctrl)
     sleep(wait)

try:
    recordNum = int(recordNum)
    sleep(5)
    for x in range(0, recordNum):
        switchNames()

except ValueError:
    print("Please enter a number. Exiting program...")

