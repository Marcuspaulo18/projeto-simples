import cv2

carregaFace=cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
carregaOlho=cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')


imagem= cv2.imread('fotos/image6.jpeg')

imagem_cinza=cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
#faces=carregaFace.detectMultiScale(imagem_cinza,scaleFactor=1.08,minNeighbors=3,minSize=(30,30))

faces=carregaFace.detectMultiScale(imagem_cinza)

print(faces)

for(x,y,i,a) in faces:
   imagem= cv2.rectangle(imagem,(x,y),(x+i,y+a),(0,255,0), 2)
   localOlho= imagem[y:y+a, x:x+i ]
   localOlhoCinza=cv2.cvtColor(localOlho,cv2.COLOR_BGR2GRAY)
   detectado= carregaOlho.detectMultiScale(localOlhoCinza,scaleFactor=1.3,minNeighbors=9)

   for(ox,oy,oi,oa) in detectado:
    cv2.rectangle(localOlho, (ox,oy),(ox+oi,oy+oa),(0,255,0),2)

cv2.imshow("fotos",imagem)
cv2.waitKey()