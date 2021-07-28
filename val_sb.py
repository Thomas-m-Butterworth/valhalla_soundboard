from tkinter import *
import winsound

root = Tk()

def play_1():
    return winsound.PlaySound(r"sounds/val_intro.wav", winsound.SND_ASYNC)
def play_2():
    return winsound.PlaySound(r"sounds/01_tom.wav", winsound.SND_ASYNC)
def play_3():
    return winsound.PlaySound(r"sounds/02_balth.wav", winsound.SND_ASYNC)
def play_4():
    return winsound.PlaySound(r"sounds/03_kat.wav", winsound.SND_ASYNC)
# def play_5():
#     return winsound.PlaySound(r" ", winsound.SND_ASYNC)
def play_6():
    return winsound.PlaySound(r"sounds/05_tony.wav", winsound.SND_ASYNC)

def blobby_friend():
    return winsound.PlaySound(r"sounds/blobby_friend.wav", winsound.SND_ASYNC)
def blobby_evil():
    return winsound.PlaySound(r"sounds/blobby_evil.wav", winsound.SND_ASYNC)

def stop_sound():
    return winsound.PlaySound(None, winsound.SND_ASYNC)

sound_1 = Button(root, text="01 - INTRO", command = play_1)
sound_2 = Button(root, text="TOM SHORT", command = play_2)
sound_3 = Button(root, text="BALTHAZAR DARK", command = play_3)
sound_4 = Button(root, text="KAT MOLINARI", command = play_4)
# sound_5 = Button(root, text="DAVID STANIER", command = play_5)
sound_6 = Button(root, text="TONY BASNETT", command = play_6)

blobby_1 = Button(root, text="NICE BLOBBY", command = blobby_friend)
blobby_2 = Button(root, text="EVIL BLOBBY", command = blobby_evil)

stop_snd = Button(root, text="!!STOP!!", command=stop_sound)

sound_1.grid(row=0, column=1)
blobby_1.grid(row=2, column=1)
blobby_2.grid(row=3, column=1)
sound_2.grid(row=5, column=1)
sound_3.grid(row=6, column=1)
sound_4.grid(row=7, column=1)
# sound_5.grid(row=0, column=1)
sound_6.grid(row=8, column=1)
stop_snd.grid(row=9, column=0)


root.mainloop()