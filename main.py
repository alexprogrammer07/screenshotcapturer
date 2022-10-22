from tkinter import *
from tkinter import messagebox
import pyautogui
import pyperclip
import os

root = Tk()  # Initialize the main window
time = IntVar()
time.set(1)
c = 1
cnt = 1
path = "os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')"



def take_shot():
    """
    A method to capture the screen and save the result in desired location
    """
    global c
    global cnt
    pyperclip.copy(c)
    count_final = pyperclip.paste()
    c = count_final
    timeleft = time.get()
    if (timeleft > 0):
        timeleft -= 1
        time.set(timeleft)
        root.after(1000, take_shot)

    else:
        s = pyautogui.screenshot()
        s.save(path+"("+str(c)+").png")
        messagebox.showinfo("Shot", "shot saved!")
        cnt += 1
        c = cnt


l = Label(root, textvariable=time, fg="red")
l.pack()
Button(root, text=f"Take Shot 1 sec", command=take_shot).pack(). # Create a shortcut to capture the shot

root.mainloop() #initatiating the tkinter window
