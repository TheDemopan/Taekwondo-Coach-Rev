import cv2
import time
import os
import uuid

IMAGE_PATH = 'C:\\Users\\srisu\\OneDrive\\Documents\\Laptop-tkd-dev\\Taekwondo-Coach-Rev'

# labels, which I will be using as statuses,
# describe common errors made when making a fist
labels = ['correct', 'tuck-in-your-thumb', 'your-thumb-should-be-under-your-fingers']
numberOfImages = 30

for status in labels:
    c = 0
    os.mkdir('C:\\Users\\srisu\\OneDrive\\Documents\\Laptop-tkd-dev\\Taekwondo-Coach-Rev' + status) # makes directory with name of status/labels
    cap = cv2.VideoCapture(0) # 0 for built in webcam, 1 for external
    time.sleep(5) # wait 5 seconds
    for img in range(numberOfImages): # for every image in the predefined range (30)
        print("Image " + str(c) + "/30 for status {}".format(status)) # print the status log
        ret, frame = cap.read()
        fileName = os.path.join(IMAGE_PATH, status, status + '.' + '{}.jpg'.format(str(uuid.uuid1()))) # save the image with this name
        cv2.imwrite(fileName, frame)
        cv2.imshow('frame', frame)
        time.sleep(3) # wait 3 seconds

        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break

    cap.release