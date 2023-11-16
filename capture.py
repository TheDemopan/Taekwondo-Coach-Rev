import cv2
import time
import os

# labels, which I will be using as statuses,
# describe common errors made when making a fist
labels = ['correct', 'tuck-in-your-thumb', 'your-thumb-should-be-under-your-fingers']
numberOfImages = 16
parentDir = 'C:/Users/User/Documents/GitHub/Taekwondo-Coach/raw-capture'

for status in labels:
    c = 0
    dir = os.path.join(parentDir, status) # makes directory with name of status/labels
    os.mkdir(dir)
    os.chdir(dir)
    cap = cv2.VideoCapture(0) # 0 for built in webcam, 1 for external
    time.sleep(5) # wait 5 seconds
    for img in range(numberOfImages): # for every image in the predefined range
        print("Image " + str(c) + "/16 for status [{}]".format(status)) # print the status log
        ret, frame = cap.read()
        fileName = dir + '-' + '{}.jpg'.format(str(c)) # save the image with this name
        cv2.imwrite(fileName, frame)
        cv2.imshow('frame', frame)
        c+=1
        time.sleep(3) # wait 3 seconds

        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break

    cap.release
