import cv2 as cv
import os
ruidos=cv.CascadeClassifier('./haarcascade_frontalface_default.xml')
camara=cv.VideoCapture(0)

modelo="fotosJack"
ruta1="."
rutaCompleta=ruta1+ "/" +modelo
if not os.path.exists(rutaCompleta):
    os.makedirs(rutaCompleta)
id=0
while True:
    respuesta,captura=camara.read()
    if respuesta==False:break
    grises=cv.cvtColor(captura,cv.COLOR_BGR2GRAY)
    idCaptura=captura.copy()
    
    cara=ruidos.detectMultiScale(grises,1.3,5)
    for(x,y,e1,e2) in cara:
        cv.rectangle(captura,(x,y),(x+e1,y+e2),(255,0,0),2)
        rostroCapturado=idCaptura[y:y+e2,x:x+e1]
        rostroCapturado=cv.resize(rostroCapturado,(360,360),interpolation=cv.INTER_CUBIC)
        cv.imwrite(rutaCompleta+"/imagen_{}.jpg".format(id),rostroCapturado)
        id=id+1
        
    cv.imshow("resultado rostro", captura)
    if  cv.waitKey(1)==ord("s") or id == 351:
        break
camara.release()
cv.destroyAllWindows()