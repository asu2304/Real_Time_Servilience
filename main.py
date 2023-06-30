import cv2
from ultralytics import YOLO
import cvzone

video_capture = cv2.VideoCapture(0)

model = YOLO('Yolo-Weights/yolov8l.pt')

while True:
    
    ret, frame = video_capture.read()
    
    frame = cv2.flip(frame, 1)
    cv2.imshow('Webcam', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

    

    
    
    
    
video_capture.release()
cv2.destroyAllWindows()








    
    
    