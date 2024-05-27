import cv2

webcam=cv2.VideoCapture(0)
classVideoFace=cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
classVideoOlho=cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
while True:
    camera,frame=webcam.read()

    cinza=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    detecta=classVideoFace.detectMultiScale(cinza)
    for(x,y,i,a) in detecta:
     cv2.rectangle(frame,(x,y),(x+i,y+a),(0,255,0),2)
     localOlho = frame[y:y + a, x:x + i]
     localOlhoCinza = cv2.cvtColor(localOlho, cv2.COLOR_BGR2GRAY)
     detectado = classVideoOlho.detectMultiScale(localOlhoCinza, scaleFactor=1.3, minNeighbors=9)

     for (ox, oy, oi, oa) in detectado:
         cv2.rectangle(localOlho, (ox, oy), (ox + oi, oy + oa), (0, 255, 0), 2)

    cv2.imshow("webcam",frame)

    if cv2.waitKey(1) == ord('f'):
        break

webcam.release()
cv2.destroyAllWindows()