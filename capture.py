import cv2
import time
import os
import uuid

IMAGE_PATH = '/home/suyash/Images/raw-set'

labels = ['correct', 'incorrect']
numberOfImages = 15

for status in labels:
    c = 0
    os.mkdir('/home/suyash/Images/raw-set/' + status)
    cap = cv2.VideoCapture(0) #0 for built in webcam, 1 for external
    time.sleep(5)
    for img in range(numberOfImages):
        print("Image " + str(c) + "/15 for status {}".format(status))
        ret, frame = cap.read()
        fileName = os.path.join(IMAGE_PATH, status, status + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(fileName, frame)
        cv2.imshow('frame', frame)
        time.sleep(3)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release