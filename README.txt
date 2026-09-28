# Real-Time Object Detection System

A simple Computer Vision application that uses a webcam to detect objects in real time. The application uses a pretrained YOLO model with OpenCV and provides an interactive Streamlit interface.

## Features

- Real-time object detection using webcam
- Detects multiple objects in a single frame
- Displays object names
- Displays confidence scores
- Draws bounding boxes around detected objects
- Simple Streamlit interface
- Uses a pretrained YOLO model

## Tech Stack

- Python
- YOLO
- OpenCV
- Streamlit
- Ultralytics

## How It Works

```text
Webcam
   ↓
OpenCV
   ↓
YOLO Model
   ↓
Object Detection
   ↓
Bounding Boxes + Confidence
   ↓
Streamlit
