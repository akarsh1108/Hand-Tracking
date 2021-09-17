import cv2
import mediapipe as mp
import time

cap =cv2.VideoCapture(0)

mpHands= mp.solutions.hands
hands=mpHands.Hands()
# for accessing drawing utilities
mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0

while True:
    success,rot=cap.read()
    img= cv2.flip(rot,90)
    imgRGB =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
               # print(id,lm)
               h, w, c=img.shape
               # we can find the positons
               cx,cy=int(lm.x*w),int(lm.y*h)
               print(id,cx,cy)
               # if id==4:
               cv2.circle(img,(cx,cy),5,(255,0,255),cv2.FILLED)
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps= 1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,(str(int(fps))),(10,70),cv2.FONT_HERSHEY_SIMPLEX,2,
                (255,0,255),2)

    cv2.imshow("Image",img)
    cv2.waitKey(1)

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    while True:
        success, rot = cap.read()
        img = cv2.flip(rot, 90)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, (str(int(fps))), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2,
                    (255, 0, 255), 2)

        cv2.imshow("Image", img)
        cv2.waitKey(1)




if __name__ =="__main__":
    main()
# So whatever we wite in the main part lika a dummy code that would be used to showcase what can a module do
