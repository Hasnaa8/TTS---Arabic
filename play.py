from tkinter import *
from tkinter import ttk
from main import run


root = Tk()
root.title("Standard Interface for TTS - Arabic")
root.geometry("500x200")
ttk.Label(root, text="TTS - Arabic").pack(pady = (0,10))
ttk.Label(root, text="Enter text with tashkeel:").pack(pady = (0,15))
g = ttk.Entry(root, width=30, font=("Helvetica", 12))
g.pack(pady = (0,8))
ttk.Button(root, text="convert to audio", command=lambda:run(g)).pack(pady = (0,15))

root.mainloop()

