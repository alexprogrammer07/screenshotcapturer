from tkinter import *
from tkinter import messagebox
import pyautogui
import pyperclip

root = Tk()
time = IntVar()
time.set(1)
c = 1
cnt = 1
path = r"Your Path Here"



def take_shot():
    global c, cnt
    pyperclip.copy(c)
    count_final = pyperclip.paste()
    c = count_final
    timeleft = time.get()
    if timeleft > 0:
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
Button(root, text=f"Take Shot 1 sec", command=take_shot).pack()

root.mainloop()
