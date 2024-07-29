#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[ ]:


#to capture facial features(eyes, nose, mouth)
face_cap = cv2.CascadeClassifier("C:/Users/Supravo/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml") 



#enable camera, capture video, face detection
video_cap = cv2.VideoCapture(0) #enabling camera  

#keep the camera on always until a particular key is pressed. when the 
#key is pressed, the camera is disabled
#while True permanently switches on the camera until a particular condition
#turns true 

while True:
    ret, video_data = video_cap.read()  #read the video images
    
    #convert images to black and white to capture the muscles
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    
    #CREATING THE BOX THAT WILL CAPTURE THE FACE
    for (x,y,w,h) in faces: 
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow("Video Live",video_data) # giving a name to the video captured. name - Video Live
    #this name will be visible on top of the video window
    if cv2.waitKey(10) == ord("a"): #a press korle video bondho hobe
        break
video_cap.release()


# In[ ]:


#if you only want to justswitch on the video

# video_cap = cv2.VideoCapture(0) #enabling camera
# while True:
#     ret, video_data = video_cap.read()  #read the video images
#     cv2.imshow("Video Live",video_data) # giving a name to the video captured. name - Video Live
#     if cv2.waitKey(10) == ord("a"):
#         break
# video_cap.release()

