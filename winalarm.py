#import threading 
import time  
import os
from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from ttkthemes import themed_tk as tk
from tkinter.messagebox import _show
from playsound import playsound

#from beeply import notes
#mybeep = notes.beeps(4000)

start = time.time()
ent = False

root = tk.ThemedTk()
root.get_themes()
root.set_theme('equilux')

root.geometry("400x300")
root.title("Alarm Clock")

style = ThemedStyle(root)
style.set_theme("equilux")

songs = []
#drop down

def show():
    songname = clicked.get()
    labl = ttk.Label(root,text=songname).pack()
    songs.append(songname)

options = [
        "music.mp3",
        "music(2).mp3",
        "music(3).mp3"]

clicked  = StringVar()
clicked.set("Select Alarm tone")

drop = ttk.OptionMenu(root,clicked,*options)
drop.pack()

songs_button = ttk.Button(root,text="Alarm tone selected",command=show).pack()

e = ttk.Entry(root,width=50)
e.pack()
e.insert(10,"Please Enter Time in 24 HH:MM")

"""
d = ttk.Entry(root,width=50)
d.pack()
d.insert(10,"delete an alarm")
"""

def playalarm(t,ind):
    ent = True
    localtime = time.localtime()
    res = time.strftime('%H:%M',localtime)
    while res != t :
        localtime = time.localtime()
        res = time.strftime('%H:%M',localtime)
        time.sleep(1)
    playsound(options[ind])

def click():
    data = e.get()     
    print("alarms set are : ", data)
    li = [x for x in data.split()]
    labl = Label(root,text = data)
    labl.pack()
    print("Alarm to be set at " , li , "HH:MM")
    for ind in range(len(li)):
        t = li[ind]
        #t1 = threading.Thread(target=playalarm,args=(t,ind,))
        #t1.start()
        #t1.join()
        playalarm(t,ind)


addalarm = ttk.Button(root,text="Set Alarm",command = click)
addalarm.pack()
"""
delalarm = ttk.Button(root,text="Del Alarm")
delalarm.pack()
"""
def check():
    if ent == False:
        root.after(15000, lambda : _show('Title', 'Please enter alarm'))
#        #root.after(200000, root.destroy)

root.after(5000, check)
root.mainloop()
