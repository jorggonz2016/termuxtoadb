#I'll take me a little while for a version
#that works for both linux and windows. Linux
#doesnt have a consistant way to bring up a terminal.
import platform
import os
import subprocess
import sys
import time
import tkinter as tk
from tkinter import ttk

def btext(newbdtext):
    body["text"]=newbdtext
def button1():
    inputtext.pack(side="top")
    if platform.system() == "Windows":
        btext("Where is the adb executable stored?\n List the full DIR path.")
    if platform.system() == "Linux":
        btext('Where is adb? If it is in your /bin folder just\n type "adb"')
    button["command"]=button2
def button2():
    adb=inputtext.get('1.0', 'end')
    inputtext.pack_forget()
    btext("Keep your phone plugged in\n with sshd -p8022 on termux.")
    button["command"]=button3
def button3():
    btext("Writing start script")
    button["text"]="Stop"
    firstfile = open("PhoneSSH.bat", "w")
    firstfile.write("adb forward tcp:8022 tcp:8022 \nssh 127.0.0.1 -p8022")
    btext("Now Writing SSH keys")
    os.system("ssh-keygen -t rsa -b 4096")
    btext("Seting up the ssh link")
    os.system("adb forward tcp:8022 tcp:8022")
    btext("Copying the key though ssh")
    os.system("ssh-copy-id 127.0.0.1 -p8022")
    btext("Finished")
    button["text"]="Done"
    button["command"]=button4
def button4():
    btext("Now you can close this window")
    button["command"]=sys.exit("Done with setup")
    
root=tk.Tk()
root.title('Tkinter Window Demo')
root.geometry('500x300+100+100')
root.resizable(False, False)


title=tk.Label(root, text="Termux Setup",height="2",font=("Arial", 25))
title.pack(side="top")

inputtext=tk.Text(root,height="4", width="100")
inputtext.pack_forget()

button=tk.Button(root,text="Continue",command=button1)
button.pack(side="bottom")

body=tk.Label(root, text="loading...",width="100", height="3")
body.pack(side="bottom")



if platform.system() == "Windows":
    btext("This adb setup is running under Windows.")
else:
    yourplat=platform.system()
    btext("Well your platform is " + yourplat + " and that isn't Windows.")
    time.sleep(5)
    sys.exit("Not supported")



root.mainloop()






