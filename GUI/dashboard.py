from tkinter import ttk
from tkinter import *
import tkinter as tk



def create_dashboard():
    root = Tk()

    root.title("ISL using YOLOv8 and word recoginition")
    
    # set the window to full screen
    root.attributes("-fullscreen", True)

    title_frame = tk.Frame(root, height = 700, width = 800,  bg = 'black',  relief = 'sunken')
    title_frame.place(x = 50, y = 100)

    dashboard_label = tk.Label(root, text="Indian Sign Language using YOLOv8", font= ("Rockwell", 20))
    dashboard_label.pack(side = TOP)

    root.mainloop()

