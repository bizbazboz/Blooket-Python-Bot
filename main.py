import time
import ctypes
import keyboard
import threading
import webbrowser
import pyautogui
import subprocess
# Bot stopping module
def stop_program():
    while True:
        if keyboard.is_pressed('esc'):
            exit()

#clicking module
def click(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0) # left mouse down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0) # left mouse up

def double_click(x,y):
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0) # left mouse down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0) # left mouse up
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0) # left mouse down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0) # left mouse up


#stop program threading initialisation
t = threading.Thread(target=stop_program)
t.start()
for x in range(0,18):
    #opens blooket
    subprocess.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe", "https://dashboard.blooket.com/my-sets", "--new-window", "/m"])
    time.sleep(2)
    click(1831,36)
    time.sleep(2)
    click(604,703)
    time.sleep(3)
    click(1673,916)
    time.sleep(3)
    click(1202,965)
    time.sleep(1)
    keyboard.press_and_release("Backspace")
    time.sleep(2)
    click(1037,474)
    time.sleep(2)
    double_click(1284,218)
    time.sleep(1)
    keyboard.press_and_release("ctrl+c")
    webbrowser.open_new("https://play.blooket.com")
    time.sleep(2)
    keyboard.press_and_release("ctrl+v")
    time.sleep(1)
    keyboard.press_and_release("Enter")
    time.sleep(3)
    keyboard.write("Test")
    time.sleep(1)
    keyboard.press_and_release("Enter")
    time.sleep(2)
    click(482,13)
    time.sleep(1)
    click(1552,409)
    time.sleep(1)
    click(1877,255)###
    time.sleep(1)
    click(754,0)
    time.sleep(1)
    click(486,684)#locationofbutton
    click(486,684)#locationofbutton
    x=0
    while True:
        time.sleep(0.1)
        if x==374:
            break
        click(1039,653)
        x=x+1
    print(x)
    time.sleep(10)
    for x in range(1,4):
        keyboard.press_and_release("ctrl+w")
        print(x)
    time.sleep(3)
