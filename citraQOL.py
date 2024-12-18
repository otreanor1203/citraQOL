import signal
import sys
import keyboard
import pygetwindow as gw

from inputs import get_gamepad

SPEED_BUTTON = "BTN_TR"             # Change these values to whatever button you want
FULLSCREEN_BUTTON = "BTN_TL"

SPEED_INCREASE_KEY = "+"            # Change these to whatever you have them set to in Citra
SPEED_DECREASE_KEY = "-"
TOGGLE_FULLSCREEN_KEY = "F11"

SPEED_MULTIPLIER = 3        # Change this number to whatever speed multiplier you want

TOGGLE = False                # Change this to True/False whether you want the speed to be a toggle or not

citraWindow = None

def getCitraWindow():       # Get the Citra Window from all windows on the PC
    global citraWindow    
    windows = gw.getAllWindows()
    for window in windows:
        if "Citra " == window.title[:6]:
            citraWindow = window
    if not citraWindow:
        print("Could not find the Citra window")
    else:
        print("Found the Citra window")
    return citraWindow


def eventloop():                                # Loop to handle button presses
    global citraWindow, TOGGLE
    normalSpeed = True
    numClicks = int(20*(SPEED_MULTIPLIER-1))    # Function to determine number of needed keyboard presses
    while True:
        events = get_gamepad()
        for event in events:
            if event.ev_type == "Key" and event.code == SPEED_BUTTON and citraWindow.isActive:
                if TOGGLE:
                    if event.state == 1:
                        if(normalSpeed):
                            for i in range(numClicks):
                                keyboard.send(SPEED_INCREASE_KEY)
                            print("Speed increased")
                            normalSpeed = False
                        else:
                            for i in range(numClicks):
                                keyboard.send(SPEED_DECREASE_KEY)
                            print("Speed decreased")
                            normalSpeed = True
                else:
                    if event.state == 1:
                        for i in range(numClicks):
                            keyboard.send(SPEED_INCREASE_KEY)
                        print("Speed increased")
                    else:
                        for i in range(numClicks):
                            keyboard.send(SPEED_DECREASE_KEY)
                        print("Speed decreased")
            if event.ev_type == "Key" and event.code == FULLSCREEN_BUTTON and citraWindow.isActive:
                if event.state == 1:
                    keyboard.send(TOGGLE_FULLSCREEN_KEY)
                    print("Fullscreen state changed")

def activateAndResetSpeed():                # Activate the window and normalize the speed
    global citraWindow
    citraWindow.restore()
    citraWindow.activate()
    for i in range(1000):
        keyboard.send(SPEED_DECREASE_KEY)
    for i in range(19):             # Set the speed to 100%
        keyboard.send(SPEED_INCREASE_KEY)


def signalHandler(signum, frame):   #Exit normally on Ctrl-C
    print("Exiting program")
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signalHandler)
    try:
        print("Program Starting. Ctrl+C to exit")
        citraWindow = getCitraWindow()
        if not citraWindow:
            sys.exit(0)
        activateAndResetSpeed()
        eventloop()
    except SystemExit:
        pass
    except:
        print("Something went wrong. Perhaps the Citra window was closed or your controller isn't on.")
        sys.exit(1)