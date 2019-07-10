import cv2,time

video = cv2.VideoCapture(0)
video.set(3,1920)
video.set(4,1080)

check, frame = video.read()
print(check)
print(frame)

time.sleep(3)

video.release()
