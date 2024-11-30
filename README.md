# Project Title
Real-Time Object Detection with YOLO and OpenCV
This project performs real-time object detection using the YOLO (You Only Look Once) model with OpenCV's dnn module. It captures video from a webcam, detects objects within each frame, and highlights them with bounding boxes and confidence scores.

## Project Overview
Using YOLOv3, this project detects multiple object classes in real time, leveraging a pre-trained model trained on the COCO dataset. This project showcases basic object detection capabilities, applying bounding boxes and labels to detected objects within each video frame.

## Features
- Real-time detection of 80 classes (from the COCO dataset) using YOLOv3.
- Displays bounding boxes and confidence scores for each detected object.
- Configurable to run on a webcam feed or on pre-recorded videos.

## Requirements
- Python 3.x
- OpenCV (cv2)
- NumPy

## Setup
Clone this repository (or download the project files manually):
```bash
git clone https://github.com/YourUsername/object-detection.git
cd object-detection
```
## Install dependencies:
```bash
pip install opencv-python numpy
```
## Download YOLOv3 model files:
- [YOLOv3 weights](https://pjreddie.com/media/files/yolov3.weights)
- [YOLOv3 configuration](https://raw.githubusercontent.com/pjreddie/darknet/refs/heads/master/cfg/yolov3.cfg)
- [COCO names](https://raw.githubusercontent.com/pjreddie/darknet/refs/heads/master/data/coco.names)
- Place the downloaded files (yolov3.weights, yolov3.cfg, coco.names) in the same directory as the project file (ObjDet.py).

# Usage
Run the object detection script:
```bash
python ObjDet.py
```
## Code Breakdown
- Loading YOLO Model: The YOLO model is loaded with pre-trained weights and a configuration file, and the COCO dataset’s class names are read into the program.
- Processing Video Frames: Each frame is captured from the webcam, pre-processed, and analyzed for object detections.
- Drawing Bounding Boxes: For each detected object with a confidence score above the threshold, a bounding box and label are displayed.

## Example Output
- Detected objects in real-time video feed are highlighted with bounding boxes, and each object has a label and confidence percentage.
![Screenshot](https://github.com/SandeepKalla/object-detection/blob/main/Sample.png?raw=true)

# Notes
- Make sure to adjust the confidence threshold as needed for better performance.
- Ensure the model files are placed in the same directory as the script to avoid file path issues.

# References
- [YOLO: You Only Look Once](https://pjreddie.com/darknet/yolo/)
- [OpenCV DNN Module](https://modelzoo.co/model/keras-yolov3)
