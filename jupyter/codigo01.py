import cv2

carrega=cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

imagem= cv2.imread('fotos/image6.jpeg')

imagem_cinza=cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)

faces=carrega.detectMultiScale(imagem_cinza,scaleFactor=1.08,minNeighbors=3,minSize=(30,30))

print(faces)

for(x,y,i,a) in faces:
    cv2.rectangle(imagem,(x,y),(x+i,y+a),(0,255,0), 2)

cv2.imshow("fotos",imagem)
cv2.waitKey()