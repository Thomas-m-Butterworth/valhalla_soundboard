from tkinter import *
import winsound

root = Tk()

def play():
    return winsound.PlaySound(r"sounds/val_intro.wav", winsound.SND_ASYNC)

sound_1 = Button(root, text="01 - INTRO", command = play)

sound_1.pack()

root.mainloop()