import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #   print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS,
                                  mpDraw.DrawingSpec(color=(25, 117, 66), thickness=2, circle_radius=1),
                                  mpDraw.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2))

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 120, 120), 3)

    cv2.imshow("Learning to make a fist", img)
    cv2.waitKey(1)
