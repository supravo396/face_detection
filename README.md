Facial Feature Detection Using OpenCV

This Python script captures video from your webcam and uses OpenCV to detect facial features such as eyes, nose, and mouth in real-time.

Features:
1.nReal-Time Face Detection: Detects and highlights faces in the video stream.
2. Configurable Parameters: Adjust scaleFactor and minNeighbors for detection accuracy.

Prerequisites
1. Python 3.x
2. OpenCV library

Installation:
1. Install OpenCV: pip install opencv-python
2. Download Haar Cascade Classifier: Ensure the Haar Cascade XML file for face detection is available. The file is typically located in the OpenCV package directory.

Usage:
1. Run the Script: python face_detection.py
2. Instructions:
   1. The video window titled "Video Live" will display the webcam feed with detected faces highlighted.
   2. Press the a key to stop the video and close the application.

Code Explanation
1. Enable Camera: cv2.VideoCapture(0) starts the webcam.
2. Face Detection: detectMultiScale() detects faces using the Haar Cascade.
3. Display: cv2.imshow("Video Live", video_data) shows the video with highlighted faces.
4. Stop Condition: if cv2.waitKey(10) == ord("a"): stops the loop when a is pressed.
