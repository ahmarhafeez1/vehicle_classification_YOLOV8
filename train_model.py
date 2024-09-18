import cv2
from ultralytics import YOLO
from roboflow import Roboflow
import os


# Initialize YOLOv8 model
model = YOLO("yolov8n.pt")  # 'n' version is lighter, switch to 's' or 'm' for larger models

# Train the model on the dataset
model.train(data=f"/Users/aleemahmad/Python Projects/vehicle_classification/datasets/VehiclesDetectionDataset/dataset.yaml", epochs=60, batch=16, imgsz=640, device="mps")
