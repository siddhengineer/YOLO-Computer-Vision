from ultralytics import YOLO
import cv2

model= YOLO("../weights/yolov8m.pt")
results=model("YOLO/Images/2.png",show=True)
cv2.waitKey(0)
