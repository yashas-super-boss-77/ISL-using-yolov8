from tkinter import ttk
from tkinter import *
import tkinter as tk
import cv2
from PIL import ImageTk, Image
import sys
sys.path.append("Backend/YOLO/ultralytics/")
import yolo_run

def create_dashboard():
    def start_yolo():
        root.configure(bg = "yellow")
        yolo_run.run_yolo()
        root.configure(bg = "white")


    root = Tk()

    root.title("ISL using YOLOv8 and word recoginition")

    # root.geometry("1024x1024")

    
    # set the window to full screen
    root.attributes("-fullscreen", True)

    start_button = Button(root, text = "START", font = ("rockwell", 30))
    start_button.place(relx=0.5, rely=0.5, anchor=CENTER)
    start_button['command'] = start_yolo
    
    cap = cv2.VideoCapture(0)

    success, img = cap.read()   


    dashboard_label = tk.Label(root, text="Indian Sign Language using YOLOv8", font= ("Rockwell", 20))
    dashboard_label.pack(side = TOP)

    root.mainloop()

