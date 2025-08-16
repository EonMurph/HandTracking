import cv2 as cv
from time import time

def calculate_fps(start_time, num_frames, fps):
    num_frames += 1
    current_time = time()
    if (current_time - start_time) >= 1:
        fps = num_frames / (current_time - start_time)
        num_frames = 0
        start_time = current_time
    return start_time, num_frames, fps

videoCap = cv.VideoCapture(0)
num_frames = 0
start_time = time()
fps = 0

while True:
    success, img = videoCap.read()
    start_time, num_frames, fps = calculate_fps(start_time, num_frames, fps)
    if success:
        cv.putText(img, f"{fps:.1f}", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv.imshow("CamOutput", img)
        if (cv.waitKey(25) & 0xFF) == ord("q"):
            cv.destroyAllWindows()
            break
