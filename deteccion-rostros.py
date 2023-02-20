import cv2 
class dectectors:
    def __init__(self):
        #call the clasfifier
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')


    def submitImage(self, image):
            #open image
            img = cv2.imread(image)

            #convert image to scale gray
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            #detect faces
            faces = self.face_cascade.detectMultiScale(gray,
                                              scaleFactor=1.1,
                                              minNeighbors=5,
                                              minSize=(30, 30),
                                              maxSize=(200, 200))
            #print faces in the imagw
            for (x,y,w,h) in faces:

                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
               

            return img



def main():
    dectector= dectectors()
    img  = input("ingresa el nombre de la imagen : \n")
    img = img+".png"
    picture = dectector.submitImage(img)
    cv2.imshow('imagen', picture)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
