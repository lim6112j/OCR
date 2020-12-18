import cv2
import tkinter as tk
from tkinter import filedialog, Text
import os
cap = cv2.VideoCapture('images/IMG_3130.MOV')
frames = []
while cap.isOpened():

    # Capture frame-by-frame
    read_success, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if not read_success:
        break
    cv2.imshow('frame', gray)
    # frames.append(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
# print('Grabbed ', len(frames), ' frames')
# root = tk.Tk()
# canvas = tk.Canvas(root, height=700, width=500, bg="#263d42")
# canvas.pack()
# frame = tk.Frame(root, bg="white")
# frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)
# openFile = tk.Button(root, text="open file", padx=10, pady=5, fg="white", bg="#263d42")
# openFile.pack()
# runApp = tk.Button(root, text="Run", padx=10, pady=5, fg="white", bg="#263d42")
# runApp.pack()
# root.mainloop()