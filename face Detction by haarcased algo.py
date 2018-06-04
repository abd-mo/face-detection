# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 21:07:17 2018

@author: abdelrahman
"""
"""  Estimate number of persons by haar cascade algorithm """
# importig libararies
import numpy as np 
import cv2
from tkinter import *
import tkinter as tk
from tkinter import filedialog
#read  image from file
def import_image_from_file():
    #import classifier (haarcascade classifier) #built in cv2 module
    face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    take_img = tk.Tk()
    take_img.withdraw()
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)#draw a rectangle around "img"
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = img[y:y+h, x:x+w]
         #eyes = eye.detectMultiScale(roi_gray)

    cv2.putText(img,("persons="+str(len(faces))),(5,30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)# image,text,postion,font type,font scale,colour,line type
    
    
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
#read   from camera
def import_from_camera():
    face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    while(True):  
          # Capture frame-by-frame
          ret,img = cap.read()
          # Our operations on the frame come here
          gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
          faces = face.detectMultiScale(img)  
          # Display the resulting frame
          for (x,y,w,h) in faces: 
               cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)#draw a rectangle around "img"
               roi_gray = gray[y:y+h, x:x+w] #region of intersting (rectangle)
               roi_color = img[y:y+h, x:x+w]
               cv2.putText(img,("persons="+str(len(faces))),(5,30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)# image,text,postion,font type,font scale,colour,line type
               cv2.imshow('img',img)
               if cv2.waitKey(1) == ord('q'):
                  break     
     # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
#design
gui = Tk()    
gui.geometry('500x200+700+100')
gui.title('abdelrahman')

button3= Button(gui, text=" exit ", font=("Ariel", 12, "bold"),command=lambda:gui.destroy()).place(x=300,y=100)
button1= Button(gui, text="image ", font=("Ariel", 12, "bold"),command=lambda:import_image_from_file()).place(x=200,y=100)
button2= Button(gui, text="camera", font=("Ariel",12, "bold"),command=lambda:import_from_camera()).place(x=100,y=100)
gui.mainloop()



