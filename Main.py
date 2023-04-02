import cv2
import mediapipe as mp
import time

cam = cv2.VideoCapture(0)

mpFaceDetection = mp.solutions.face_detection
faceDetection = mpFaceDetection.FaceDetection()

startTime = time.time()

while True:
    Success, frame = cam.read()

    h, w, c = frame.shape

    rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
   
    results = faceDetection.process(rgbFrame)

    if results.detections:

        elapsedTime = time.time() - startTime
        elapsedTime = int(elapsedTime)

        if elapsedTime > 10:
            cv2.rectangle(frame, (0, 0), (w, h), (0, 0, 255), 4)

        cv2.putText(frame, f"{str(elapsedTime)} seconds", (460,40), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    1, (0, 255, 255), 1)

        print("Face detected")
    else:
        startTime = time.time()
        print("Not detected")

    cv2.imshow("Face Detection", frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break