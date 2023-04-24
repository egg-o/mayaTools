# requires opencv-python

import OpenCV as cv2

cap = cv2.VideoCapture('path/to/video.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    key = cv2.waitKey(0)
    if key == ord('q'):
        break

frame_pos = 0
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
while True:
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_pos)
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    key = cv2.waitKey(0)
    if key == ord('q'):
        break
    elif key == ord('n') and frame_pos < total_frames - 1:
        frame_pos += 1
    elif key == ord('p') and frame_pos > 0:
        frame_pos -= 1

cap.release()
cv2.destroyAllWindows()