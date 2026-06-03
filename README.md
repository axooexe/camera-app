# 📸 camera-app
A simple aesthetic and cozy desktop camera app built with Python, CustomTkinter, and OpenCV. It has a clean, minimalist UI with a warm pastel color theme instead of the usual boring gray window. 

You can use it to view your webcam feed and snap quick photos that save automatically to a folder on your computer. It's lightweight, easy to set up, and just a fun little side project to get working. 📸

##  Installation & Running

Follow the instructions below depending on your operating system to set up your environment and run the app.

### 📦 1. Base Python Libraries
No matter what operating system you are on, you will need to install the core Python packages that power the interface, video processing, and image rendering. Open your terminal or command prompt and run:

pip install customtkinter opencv-python pillow

### 📦 2.Other System Packages
Depending on the operating system, some users might need a quick one-line command to make sure Python can talk to their webcam and open windows properly.Open your terminal or command prompt and run:

★ On linux(Debian based):

sudo apt update && sudo apt install python3-tk python3-opencv libv4l-dev -y

★ On Macos:

brew install python-tk

★ On windows:
no need to run anything since Python on Windows handles everything automatically right out of the box
