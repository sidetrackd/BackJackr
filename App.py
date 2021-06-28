#!/usr/bin/env python3

import io
from tkinter import *
from tkinter import filedialog, ttk

import numpy as np
from PIL import Image
from rembg.bg import remove


class BackJackr:
    def __init__(self, root):
        root.title("BackJackr")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text='Input Image').grid(column=1, row=1, sticky=(N, E))

        self.input_path = StringVar()
        ttk.Button(mainframe, text="Select", command=self.get_inputfilename).grid(column=2, row=1, sticky=(N, E))

        ttk.Label(mainframe, text='Output Image').grid(column=1, row=2, sticky=(N, E))

        self.output_path = StringVar()
        ttk.Button(mainframe, text="Select", command=self.get_outputfilename).grid(column=2, row=2, sticky=(N, E))

        ttk.Button(mainframe, text="Process", command=self.process).grid(column=2, row=3, sticky=(N, E))

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        root.bind("<Return>", self.process)

    def get_inputfilename(self, *args):
        self.input_path.set(filedialog.askopenfilename())

    def get_outputfilename(self, *args):
        self.output_path.set(filedialog.asksaveasfilename())
    
    def process(self, *args):
        try:
            print(self.input_path.get())
            print(self.output_path.get())
            f = np.fromfile(self.input_path.get())
            result = remove(f)
            img = Image.open(io.BytesIO(result)).convert("RGBA")
            img.save(self.output_path.get())
        except Exception: 
            pass

root = Tk()
BackJackr(root)
root.mainloop()
