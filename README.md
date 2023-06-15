# Wireless_Soundcontroller

The "Wireless Sound Control" project implemented in Python offers a unique and intuitive way to control the volume of your computer's speakers. 
By utilizing computer vision and machine learning techniques, this project allows you to adjust the volume simply by using hand gestures.

Using a webcam, the project tracks and recognizes the movements of your hand in real-time.It identifies specific landmarks on the hand, such as the thumb and index finger, and calculates the distance between them. This distance is then mapped to the desired volume level.Moving your hand closer together increases the volume, while moving your hand farther apart decreases it.

To interact with the computer's audio system, the project employs the PyCaw library, which interfaces with the Windows Core Audio API.
This enables seamless control of the computer's speakers without the need for physical buttons or external devices. The volume changes are reflected in real-time, providing a convenient and hands-free way to adjust the audio output.

**Technologies used in this project:**

  * Python: The programming language used for implementing the project.
  * OpenCV: A computer vision library used for accessing the webcam, capturing frames, and performing image processing tasks.
  * Mediapipe: A library developed by Google that provides a framework for building various machine learning-based applications, including hand tracking and gesture    recognition.
  * PyCaw: A Python library that allows interaction with the Windows Core Audio API, used for controlling the volume of the computer's speakers.
  * ctypes: A Python library that provides low-level interfaces to C-based APIs, used for accessing the COM interface of the Windows Core Audio API.
