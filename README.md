# Robot Detection and Tracking
## Overview

This repository contains two Python scripts, `RobotDetection.py` and `RobotTracking.py`, designed to analyze videos and visualize the path of a robot. 

- `RobotDetection.py`: Generates a visualization of the robot's path overlayed on top of the video.
- `RobotTracking.py`: Displays the video alongside the detected path in separate windows.

## Installation

To run the scripts, you need to have OpenCV and matplotlib.pyplot installed on your system. You can install them via pip in your terminal. If you're using VS Code, you can open the Terminal and execute the following commands:

```bash
pip install opencv-python
pip install matplotlib
```
# Usage
Prepare Your Environment: Place your video file into the same folder as the Python scripts.

Modify Script: Open the Python script you want to use (RobotDetection.py or RobotTracking.py) and change the name of the video file within the script to match your file's name.

Run the Script: Execute the Python script. This will initiate the analysis and visualization process.

Example
python
Copy code

# Example code snippet to modify in the script
`cap = cv2.VideoCapture("Untitled video.mp4")`
Change "Untitled viedo.mp4" to match your video file's name
